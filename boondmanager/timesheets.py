"""High-level timesheet editing.

Hides the sharp edges of PUT /times-reports/{id} (negative row ids to create
rows, entry id lifecycle, relationship shapes, deletion-by-omission) behind a
grid model: a Timesheet has rows (one per activity), a row has one duration
per day.

Usage::

    ts = await client.fetch_timesheet("1652")

    row = ts.row(project="23")          # get-or-create; delivery auto-picked
    row.set("2026-06-30", 0.5)          # upsert a day
    row.set("2026-06-29", 0)            # remove a day

    ts.add_exceptional(
        start="2026-06-15T08:00:00+0200", end="2026-06-15T10:00:00+0200",
        work_unit=12, project="23", description="astreinte",
    )

    await ts.save()                     # validate, PUT, silent-drop guard, refresh
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from .exceptions import TimesheetNotEditableError
from .models import (
    BatchRef,
    DeliveryRef,
    ProjectRef,
    TimeEntry,
    TimesReport,
    WorkUnitType,
)

if TYPE_CHECKING:
    from .client import BoondManagerClient


class TimesheetRow:
    """One activity row: a (work unit, project, delivery, batch) combination
    with one duration per day."""

    def __init__(
        self,
        timesheet: Timesheet,
        row_id: int,
        work_unit_type: WorkUnitType,
        project: ProjectRef | None = None,
        delivery: DeliveryRef | None = None,
        batch: BatchRef | None = None,
    ) -> None:
        self._timesheet = timesheet
        self.row_id = row_id
        self.work_unit_type = work_unit_type
        self.project = project
        self.delivery = delivery
        self.batch = batch
        self._entries: dict[str, TimeEntry] = {}  # ISO date -> entry

    @property
    def is_new(self) -> bool:
        """True until saved — negative row ids tell the API to create the row."""
        return self.row_id < 0

    @property
    def label(self) -> str:
        if self.project:
            return (
                self.project.reference
                or self.project.title
                or self._timesheet.project_label(self.project.id)
                or f"Project {self.project.id}"
            )
        return self.work_unit_type.name or f"Activity {self.work_unit_type.reference}"

    @property
    def days(self) -> dict[str, float]:
        """ISO date -> duration, for all days with time on this row."""
        return {d: e.duration for d, e in sorted(self._entries.items())}

    @property
    def total(self) -> float:
        return sum(e.duration for e in self._entries.values())

    def get(self, date: str) -> float:
        entry = self._entries.get(date)
        return entry.duration if entry else 0.0

    def set(self, date: str, duration: float) -> None:
        """Upsert the duration for a day; 0 (or less) removes the day.

        Removed entries are omitted from the next save, which is how the API
        deletes them.
        """
        if duration <= 0:
            self._entries.pop(date, None)
            return
        entry = self._entries.get(date)
        if entry is not None:
            entry.duration = duration
            return
        self._entries[date] = TimeEntry(
            id=self._timesheet._next_entry_id(),
            start_date=date,
            duration=duration,
            row=self.row_id,
            work_unit_type=self.work_unit_type,
            project=self.project,
            delivery=self.delivery,
            batch=self.batch,
        )

    def clear(self) -> None:
        """Remove every day on this row (deletes the row on save)."""
        self._entries.clear()

    def _matches(
        self, project_id: str | None, delivery_id: str | None, work_unit: int
    ) -> bool:
        return (
            (self.project.id if self.project else None) == project_id
            and (self.delivery.id if self.delivery else None) == delivery_id
            and self.work_unit_type.reference == work_unit
        )

    def _adopt(self, entry: TimeEntry) -> None:
        self._entries[entry.start_date] = entry

    def __repr__(self) -> str:
        return f"<TimesheetRow {self.row_id} {self.label!r} total={self.total}>"


class Timesheet:
    """Editable view of one times report (a month for one resource)."""

    def __init__(
        self,
        client: BoondManagerClient,
        report: TimesReport,
        included: list[dict] | None = None,
    ) -> None:
        self._client = client
        self._entry_id_counter = 0
        self._row_id_counter = 0
        self._load(report, included or [])

    # -- loading -------------------------------------------------------------

    @classmethod
    async def fetch(cls, client: BoondManagerClient, report_id: str) -> Timesheet:
        report, included = await client.get_times_report_with_included(report_id)
        return cls(client, report, included)

    def _load(self, report: TimesReport, included: list[dict]) -> None:
        self.report = report
        self._included = included
        self.rows: list[TimesheetRow] = []
        by_row: dict[int | None, TimesheetRow] = {}
        for entry in report.attributes.regular_times:
            row = by_row.get(entry.row)
            if row is None:
                row = TimesheetRow(
                    self,
                    # Entries missing a row id should not exist, but if the
                    # API ever returns one, treat it as a new row to recreate.
                    entry.row if entry.row is not None else self._next_row_id(),
                    entry.work_unit_type or WorkUnitType(reference=1),
                    project=entry.project,
                    delivery=entry.delivery,
                    batch=entry.batch,
                )
                by_row[entry.row] = row
                self.rows.append(row)
            row._adopt(entry)

        # Work-unit types the resource may book time on, from the report's
        # included resource (workUnitTypesAllowed) — production, internal,
        # exceptional and absence types, with names.
        self.work_unit_types: list[WorkUnitType] = []
        for item in included:
            if item.get("type") == "resource":
                allowed = item.get("attributes", {}).get("workUnitTypesAllowed")
                if allowed:
                    self.work_unit_types = [
                        WorkUnitType.model_validate(w) for w in allowed
                    ]
                    break

        # project id -> deliveries, from the JSON:API included section
        self._projects: dict[str, dict] = {}
        deliveries: dict[str, dict] = {
            i["id"]: i for i in included if i.get("type") == "delivery"
        }
        for item in included:
            if item.get("type") != "project":
                continue
            attrs = item.get("attributes", {})
            refs = item.get("relationships", {}).get("deliveries", {}).get("data", [])
            self._projects[item["id"]] = {
                "label": attrs.get("reference") or attrs.get("title") or f"Project {item['id']}",
                "deliveries": [deliveries.get(r["id"], r) for r in refs],
            }

    async def refresh(self) -> None:
        """Reload from the API (picks up server-assigned entry and row ids)."""
        report, included = await self._client.get_times_report_with_included(
            self.report.id
        )
        self._load(report, included)

    # -- introspection ---------------------------------------------------------

    @property
    def id(self) -> str:
        return self.report.id

    @property
    def term(self) -> str:
        return self.report.term

    @property
    def state(self) -> str:
        return self.report.state

    @property
    def is_editable(self) -> bool:
        return self.report.is_editable

    @property
    def total(self) -> float:
        return sum(r.total for r in self.rows)

    @property
    def project_options(self) -> list[dict]:
        """Selectable project/delivery pairs for this report.

        [{"project_id", "delivery_id", "label"}] — from the report's
        relationships, present even when the report has no entries yet.
        """
        return [
            {"project_id": pid, "delivery_id": d.get("id", ""), "label": info["label"]}
            for pid, info in self._projects.items()
            for d in info["deliveries"]
        ]

    def project_label(self, project_id: str) -> str:
        return self._projects.get(project_id, {}).get("label", "")

    def work_unit_types_for(self, *activity_types: str) -> list[WorkUnitType]:
        """Allowed work-unit types filtered by activity type, sorted by name.

        Activity types: "production", "internal", "absence",
        "exceptionalTime", "exceptionalCalendar".
        """
        return sorted(
            (w for w in self.work_unit_types if w.activity_type in activity_types),
            key=lambda w: w.name,
        )

    def row_by_id(self, row_id: int | None) -> TimesheetRow | None:
        for row in self.rows:
            if row.row_id == row_id:
                return row
        return None

    def reassign_row(
        self,
        row_id: int,
        *,
        project: str | None,
        delivery: str | None,
        work_unit: int,
    ) -> bool:
        """Change the project/delivery/work-unit of an existing row.

        All day entries are preserved; only their activity assignment changes.
        If a row with the new assignment already exists, entries are merged into it.
        Returns False when the row is not found or already has the requested assignment.
        """
        row = self.row_by_id(row_id)
        if row is None:
            return False
        if row._matches(project, delivery, work_unit):
            return False

        days = dict(row.days)
        row.clear()
        self.rows = [r for r in self.rows if r is not row]

        target = self.row(project=project, delivery=delivery, work_unit=work_unit)
        for date, duration in days.items():
            target.set(date, target.get(date) + duration)
        return True

    def entry(self, entry_id: str) -> TimeEntry | None:
        """Find a regular or exceptional entry by its server id."""
        for row in self.rows:
            for e in row._entries.values():
                if e.id == entry_id:
                    return e
        for e in self.report.attributes.exceptional_times:
            if e.id == entry_id:
                return e
        return None

    def set_entry_duration(self, entry_id: str, duration: float) -> bool:
        """Update (or remove, when duration <= 0) an entry by id."""
        for row in self.rows:
            for date, e in list(row._entries.items()):
                if e.id == entry_id:
                    row.set(date, duration)
                    return True
        for e in self.report.attributes.exceptional_times:
            if e.id == entry_id:
                e.duration = duration
                return True
        return False

    # -- editing ---------------------------------------------------------------

    def row(
        self,
        *,
        project: str | None = None,
        delivery: str | None = None,
        work_unit: int = 1,
        batch: str | None = None,
    ) -> TimesheetRow:
        """Get the matching activity row, creating it if needed.

        ``project``/``delivery``/``batch`` are BoondManager ids. When the
        project has exactly one delivery in this report, ``delivery`` can be
        omitted; ambiguity raises ValueError with the options.
        """
        if project and not delivery:
            deliveries = self._projects.get(project, {}).get("deliveries", [])
            if len(deliveries) == 1:
                delivery = deliveries[0]["id"]
            elif len(deliveries) > 1:
                options = ", ".join(d["id"] for d in deliveries)
                raise ValueError(
                    f"project {project} has several deliveries ({options}); "
                    "pass delivery= explicitly"
                )

        for row in self.rows:
            if row._matches(project, delivery, work_unit):
                return row

        row = TimesheetRow(
            self,
            self._next_row_id(),
            self._resolve_wut(work_unit),
            project=ProjectRef(id=project) if project else None,
            delivery=DeliveryRef(id=delivery) if delivery else None,
            batch=BatchRef(id=batch) if batch else None,
        )
        self.rows.append(row)
        return row

    def add_exceptional(
        self,
        *,
        start: str,
        end: str,
        duration: float,
        work_unit: int,
        activity_type: str = "",
        project: str | None = None,
        delivery: str | None = None,
        description: str = "",
    ) -> TimeEntry:
        """Add an exceptional time (astreinte, intervention...).

        ``start``/``end`` are dates (exceptionalCalendar) or datetimes
        (exceptionalTime). The API requires a project and delivery for
        exceptional times; when the report has exactly one project/delivery
        they are filled in automatically.
        """
        if not project and len(self._projects) == 1:
            project = next(iter(self._projects))
        if project and not delivery:
            deliveries = self._projects.get(project, {}).get("deliveries", [])
            if len(deliveries) == 1:
                delivery = deliveries[0]["id"]
        entry = TimeEntry(
            id=self._next_entry_id(),
            start_date=start,
            end_date=end,
            duration=duration,
            work_unit_type=WorkUnitType(reference=work_unit, activityType=activity_type),
            project=ProjectRef(id=project) if project else None,
            delivery=DeliveryRef(id=delivery) if delivery else None,
            description=description,
        )
        self.report.attributes.exceptional_times.append(entry)
        return entry

    # -- persistence -------------------------------------------------------------

    async def save(self) -> None:
        """PUT the grid and reload server-assigned ids.

        Raises TimesheetNotEditableError before touching the API when the
        report is validated/closed, BoondManagerValidationError when the
        payload breaks BoondManager's schema, and BoondManagerSilentDropError
        when the server acknowledged but discarded entries.
        """
        if not self.is_editable:
            raise TimesheetNotEditableError(self.report.id, self.report.state)
        self.report.attributes.regular_times = [
            e for row in self.rows for e in row._entries.values()
        ]
        self.report.attributes.exceptional_times = [
            e for e in self.report.attributes.exceptional_times if e.duration > 0
        ]
        await self._client.update_times_report(self.report)
        await self.refresh()

    # -- internals -----------------------------------------------------------------

    def _resolve_wut(self, reference: int) -> WorkUnitType:
        """Look up a WorkUnitType by reference from the report's allowed list.

        Falls back to a name-less placeholder when not found (e.g. the reference
        exists but the resource's workUnitTypesAllowed list was not included).
        """
        for wut in self.work_unit_types:
            if wut.reference == reference:
                return wut
        return WorkUnitType(reference=reference)

    def _next_entry_id(self) -> str:
        self._entry_id_counter -= 1
        return str(self._entry_id_counter)

    def _next_row_id(self) -> int:
        self._row_id_counter -= 1
        return self._row_id_counter

    def __repr__(self) -> str:
        return (
            f"<Timesheet {self.id} {self.term} state={self.state!r} "
            f"rows={len(self.rows)} total={self.total}>"
        )
