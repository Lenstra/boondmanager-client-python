"""Pydantic models for the BoondManager API."""

from __future__ import annotations

from collections import defaultdict

from pydantic import BaseModel, ConfigDict, Field, field_validator

_CFG = ConfigDict(populate_by_name=True, extra="ignore")


# ---------------------------------------------------------------------------
# Shared primitives
# ---------------------------------------------------------------------------


class WorkUnitType(BaseModel):
    model_config = _CFG

    reference: int
    activity_type: str = Field("", alias="activityType")
    name: str = ""


class ProjectRef(BaseModel):
    model_config = _CFG

    id: str
    reference: str | None = None
    title: str | None = None


class DeliveryRef(BaseModel):
    model_config = _CFG

    id: str
    title: str | None = None
    start_date: str | None = Field(default=None, alias="startDate")
    end_date: str | None = Field(default=None, alias="endDate")


# ---------------------------------------------------------------------------
# Time entries
# ---------------------------------------------------------------------------


class BatchRef(BaseModel):
    model_config = _CFG

    id: str
    title: str | None = None


class TimeEntry(BaseModel):
    """A single day-level time entry inside a times report."""

    model_config = _CFG

    id: str
    start_date: str = Field(alias="startDate")
    end_date: str | None = Field(default=None, alias="endDate")
    duration: float
    row: int | None = None
    work_unit_type: WorkUnitType | None = Field(default=None, alias="workUnitType")
    project: ProjectRef | None = None
    delivery: DeliveryRef | None = None
    batch: BatchRef | None = None
    description: str = ""

    @field_validator("project", "delivery", "batch", mode="before")
    @classmethod
    def _none_relationship(cls, v):
        # JSON:API "no relationship" form: {"data": null}
        if isinstance(v, dict) and "id" not in v:
            return None
        return v

    @property
    def activity_name(self) -> str:
        """Human-readable name: project reference > delivery title > work unit name."""
        if self.project:
            return self.project.reference or self.project.title or ""
        if self.delivery:
            return self.delivery.title or ""
        return self.work_unit_type.name if self.work_unit_type else ""

    @property
    def activity_type(self) -> str:
        return self.work_unit_type.activity_type if self.work_unit_type else ""

    @property
    def is_existing(self) -> bool:
        """True for server-assigned entries (positive integer id)."""
        try:
            return int(self.id) > 0
        except (ValueError, TypeError):
            return False

    def _rel(self, ref) -> dict:
        # Relationships are mandatory in the PUT schema: {"id": ...} when set,
        # {"data": null} when absent. A bare null or a missing key fails the
        # server-side schema check and the whole entry is silently dropped.
        return {"id": ref.id} if ref else {"data": None}

    def to_api_regular(self) -> dict:
        """Serialize as a regularTimes item for PUT /times-reports/{id}.

        The schema (schemas/timesReports/bodyPut.json) allows exactly
        startDate, duration, row, workUnitType, project, delivery, batch
        (+ id when updating) with additionalProperties: false — any extra
        key makes BoondManager silently discard the entry.
        """
        d: dict = {
            "startDate": self.start_date,
            "duration": self.duration,
            # row < 0 tells BoondManager to create a new row (TAB_LIGNETEMPS);
            # row > 0 attaches the entry to that existing row. Entries sharing
            # the same negative value end up on the same new row.
            "row": self.row if self.row is not None else -1,
            "workUnitType": {
                "reference": self.work_unit_type.reference if self.work_unit_type else 1
            },
            "project": self._rel(self.project),
            "delivery": self._rel(self.delivery),
            "batch": self._rel(self.batch),
        }
        # New entries must be sent without id so BoondManager creates them.
        if self.is_existing:
            d["id"] = self.id
        return d

    def to_api_exceptional(self) -> dict:
        """Serialize as an exceptionalTimes item for PUT /times-reports/{id}.

        The schema allows exactly startDate, endDate, description,
        workUnitType, project, delivery, batch (+ optional recovering,
        + id when updating). No duration and no row — duration is derived
        server-side from startDate/endDate.

        Unlike regular times, project and delivery are mandatory relationships
        here ({"data": null} is not accepted): callers must set both or the
        server will silently drop the entry.
        """
        d: dict = {
            "startDate": self.start_date,
            "endDate": self.end_date or self.start_date,
            "description": self.description or "",
            "workUnitType": {
                "reference": self.work_unit_type.reference if self.work_unit_type else 1
            },
            "project": self._rel(self.project),
            "delivery": self._rel(self.delivery),
            "batch": self._rel(self.batch),
        }
        if self.is_existing:
            d["id"] = self.id
        return d


class TimesReportRow(BaseModel):
    """One aggregated activity row for a full month (grouped by row ID)."""

    name: str
    activity_type: str
    total_days: float


class EditableRow(BaseModel):
    """A timesheet row with its per-day entries, used for the edit grid."""

    model_config = _CFG

    row_id: int | None
    name: str
    activity_type: str = ""
    is_editable: bool = True
    entries: dict[str, TimeEntry] = Field(default_factory=dict)  # ISO date -> TimeEntry

    @property
    def total_days(self) -> float:
        return sum(e.duration for e in self.entries.values())


# ---------------------------------------------------------------------------
# Times reports
# ---------------------------------------------------------------------------


class TimesReportAttributes(BaseModel):
    model_config = _CFG

    term: str
    state: str = ""
    closed: bool = False
    # Populated only on full report fetches (GET /times-reports/{id})
    regular_times: list[TimeEntry] = Field(default_factory=list, alias="regularTimes")
    exceptional_times: list[TimeEntry] = Field(default_factory=list, alias="exceptionalTimes")
    absences_times: list[TimeEntry] = Field(default_factory=list, alias="absencesTimes")
    workplace_times: list[TimeEntry] = Field(default_factory=list, alias="workplaceTimes")
    planned_times: list[TimeEntry] = Field(default_factory=list, alias="plannedTimes")

    def all_entries(self) -> list[TimeEntry]:
        """All billable + absence entries (excludes workplace/planned which are meta-data)."""
        return self.regular_times + self.exceptional_times + self.absences_times

    def absence_by_date(self) -> dict[str, float]:
        """ISO date -> total absence duration for that day (sum across all absence entries)."""
        result: dict[str, float] = {}
        for e in self.absences_times:
            result[e.start_date] = result.get(e.start_date, 0.0) + e.duration
        return result

    _EXCEPTIONAL_ACTIVITY_TYPES = {"exceptionalTime", "exceptionalCalendar"}

    def rows(self) -> list[TimesReportRow]:
        """Aggregate regular + absence day entries into one row per activity.

        Exceptional activities are excluded even when present in regularTimes — BoondManager
        duplicates them there alongside the event records in exceptionalTimes.
        Access them directly via ``exceptional_times``.
        """
        grouped: dict[int | None, dict] = defaultdict(
            lambda: {"name": "", "activity_type": "", "total_days": 0.0}
        )
        for entry in self.regular_times + self.absences_times:
            if entry.activity_type in self._EXCEPTIONAL_ACTIVITY_TYPES:
                continue
            g = grouped[entry.row]
            g["name"] = g["name"] or entry.activity_name
            g["activity_type"] = g["activity_type"] or entry.activity_type
            g["total_days"] += entry.duration
        return sorted(
            [TimesReportRow(**g) for g in grouped.values()],
            key=lambda r: r.total_days,
            reverse=True,
        )

    def editable_rows(self) -> list[EditableRow]:
        """Build edit-capable rows for the day-grid: regular times are editable, absences are read-only.

        Exceptional times are excluded — they have datetime ranges, not per-day durations, and
        are displayed separately outside the grid.
        """
        regular: dict[int | None, dict] = {}
        absences: dict[int | None, dict] = {}

        for entry in self.regular_times:
            if entry.activity_type in self._EXCEPTIONAL_ACTIVITY_TYPES:
                continue
            rk = entry.row
            if rk not in regular:
                regular[rk] = {
                    "row_id": rk,
                    "name": entry.activity_name,
                    "activity_type": entry.activity_type,
                    "is_editable": True,
                    "entries": {},
                }
            regular[rk]["name"] = regular[rk]["name"] or entry.activity_name
            regular[rk]["entries"][entry.start_date] = entry

        for entry in self.absences_times:
            rk = entry.row
            if rk not in absences:
                absences[rk] = {
                    "row_id": rk,
                    "name": entry.activity_name,
                    "activity_type": entry.activity_type,
                    "is_editable": False,
                    "entries": {},
                }
            absences[rk]["name"] = absences[rk]["name"] or entry.activity_name
            absences[rk]["entries"][entry.start_date] = entry

        regular_rows = sorted(
            [EditableRow(**v) for v in regular.values()],
            key=lambda r: r.total_days,
            reverse=True,
        )
        return regular_rows + [EditableRow(**v) for v in absences.values()]


class TimesReport(BaseModel):
    """Times report — works for both summary (list) and full (detail) responses.

    When parsed from the list endpoint, time entry arrays are empty.
    Call ``client.get_times_report(report.id)`` to get the full version.
    """

    model_config = _CFG

    id: str
    attributes: TimesReportAttributes

    @property
    def term(self) -> str:
        return self.attributes.term

    @property
    def state(self) -> str:
        return self.attributes.state

    def rows(self) -> list[TimesReportRow]:
        return self.attributes.rows()

    def editable_rows(self) -> list[EditableRow]:
        return self.attributes.editable_rows()

    def absence_by_date(self) -> dict[str, float]:
        return self.attributes.absence_by_date()

    _EDITABLE_STATES: frozenset[str] = frozenset({
        "savedandnovalidation",
        "savedandwaitingforvalidation",
    })

    @property
    def is_editable(self) -> bool:
        """True when the report can still be edited.

        Allowlist-based: unknown states are treated as non-editable so that a
        new BoondManager terminal state never silently becomes writable.
        """
        if self.attributes.closed:
            return False
        return self.state.lower() in self._EDITABLE_STATES


# ---------------------------------------------------------------------------
# Absences reports
# ---------------------------------------------------------------------------


class AbsencePeriod(BaseModel):
    model_config = _CFG

    id: str | None = None
    start_date: str = Field(alias="startDate")
    end_date: str = Field(alias="endDate")
    duration: float
    title: str | None = None
    work_unit_type: WorkUnitType | None = Field(default=None, alias="workUnitType")


class AbsencesReportAttributes(BaseModel):
    model_config = _CFG

    state: str | None = None
    creation_date: str | None = Field(default=None, alias="creationDate")
    information_comments: str | None = Field(default=None, alias="informationComments")
    absences_periods: list[AbsencePeriod] = Field(default_factory=list, alias="absencesPeriods")


class AbsencesReport(BaseModel):
    model_config = _CFG

    id: str
    attributes: AbsencesReportAttributes

    @property
    def state(self) -> str | None:
        return self.attributes.state

    @property
    def periods(self) -> list[AbsencePeriod]:
        return self.attributes.absences_periods


# ---------------------------------------------------------------------------
# Create-absence input
# ---------------------------------------------------------------------------


class CreateAbsencePeriod(BaseModel):
    """One period to submit in an absence request (POST /absences-reports)."""

    start_date: str
    end_date: str
    duration: float
    title: str
    work_unit_type_reference: int

    def to_api(self) -> dict:
        return {
            "startDate": self.start_date,
            "endDate": self.end_date,
            "duration": self.duration,
            "title": self.title,
            "workUnitType": {"reference": self.work_unit_type_reference},
        }


# ---------------------------------------------------------------------------
# Resources
# ---------------------------------------------------------------------------


class ResourceAttributes(BaseModel):
    model_config = _CFG

    first_name: str = Field("", alias="firstName")
    last_name: str = Field("", alias="lastName")
    email1: str | None = None
    email2: str | None = None
    email3: str | None = None
    state: int | None = None
    type_of: int | None = Field(default=None, alias="typeOf")
    title: str | None = None

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}".strip()

    def emails(self) -> list[str]:
        return [e for e in [self.email1, self.email2, self.email3] if e]

    def has_email(self, email: str) -> bool:
        return email.lower() in [e.lower() for e in self.emails()]


class Resource(BaseModel):
    model_config = _CFG

    id: str
    attributes: ResourceAttributes

    @property
    def full_name(self) -> str:
        return self.attributes.full_name


# ---------------------------------------------------------------------------
# Current user
# ---------------------------------------------------------------------------


class CurrentUserAttributes(BaseModel):
    model_config = _CFG

    first_name: str = Field("", alias="firstName")
    last_name: str = Field("", alias="lastName")
    login: str | None = None
    email1: str | None = None

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}".strip()


class CurrentUser(BaseModel):
    """The authenticated user. ``id`` is their BoondManager resource ID."""

    model_config = _CFG

    id: str
    attributes: CurrentUserAttributes

    @property
    def resource_id(self) -> str:
        return self.id

    @property
    def full_name(self) -> str:
        return self.attributes.full_name
