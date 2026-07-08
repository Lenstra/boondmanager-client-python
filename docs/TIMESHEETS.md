# Timesheet module

The timesheet module provides a domain-level API for reading and editing
BoondManager time reports. It hides the sharp edges of the wire format behind
a grid model: a `Timesheet` has rows (one per activity), each row has one
duration per calendar day.

## Concepts

### Term
A time report covers exactly one calendar month, identified by `"YYYY-MM"`.
Each resource has at most one report per month per project contract (BoondManager
creates them automatically when a project is assigned; you can also create an
empty one via `client.create_times_report(resource_id, term)`).

### Row
A row groups all time entries that share the same activity: the same
`(project, delivery, work_unit_type)` combination. A row has at most one entry
per day. BoondManager identifies rows by a positive integer `row_id`
(`TAB_LIGNETEMPS.ID_LIGNETEMPS`). New rows are created by sending a negative
`row` value in the PUT body; all entries with the same negative value land on
the same new row.

### Entry
A single time entry on one day: `(date, duration)` attached to a row. Duration
is a fraction of a day (0.5 = half-day, 1.0 = full day). Sending duration 0 or
omitting an entry from the PUT body deletes it.

### Exceptional time
An event-based entry with explicit start/end datetimes (type `exceptionalTime`,
e.g. on-call shifts measured in hours) or a date range (type
`exceptionalCalendar`, e.g. astreinte measured in calendar days). These live in
`exceptionalTimes`, not `regularTimes`. BoondManager also mirrors them as
day-entries in `regularTimes` for the activity totals — the domain layer
filters those duplicates out of `rows()` and `editable_rows()`.

### Work unit type (WUT)
The category of the time being reported. References are per-customer
configuration (reference 2 means "CP" for one customer, something else for
another). Never hardcode WUT references. Read them from
`Timesheet.work_unit_types_for(activity_type)` or
`client.get_absence_types(resource_id)`.

Activity types used in `workUnitTypesAllowed`:

| `activityType`       | Meaning                                   |
|----------------------|-------------------------------------------|
| `production`         | Billable time on a project                |
| `internal`           | Internal / structure time (no project)    |
| `absence`            | Paid leave, sick leave, etc.              |
| `exceptionalTime`    | Timed on-call / interventions (hours)     |
| `exceptionalCalendar`| On-call periods counted in calendar days  |

---

## The `Timesheet` class

`Timesheet` is the primary editing surface. Always use it for timesheet edits;
never build PUT bodies by hand.

```python
from boondmanager import BoondManagerClient, Timesheet

async with BoondManagerClient(...) as client:
    ts = await client.fetch_timesheet("1652")

    # Edit regular time
    ts.row(project="23").set("2026-06-30", 0.5)          # get-or-create row, upsert day
    ts.row(project="23").set("2026-06-29", 0)            # remove a day
    ts.row(work_unit=7).set("2026-06-30", 1.0)           # internal row (no project)

    # Edit exceptional time
    ts.add_exceptional(
        start="2026-06-15T08:00:00+0200",
        end="2026-06-15T10:00:00+0200",
        duration=7200,          # seconds
        work_unit=11,
        activity_type="exceptionalTime",
        description="CHG-1234",
    )

    await ts.save()             # validate, PUT, silent-drop guard, refresh
```

### `Timesheet.fetch(client, report_id)`

Class method. Fetches the full report and its `included` section (projects,
deliveries, resource WUTs) in one GET.

### `Timesheet.row(*, project, delivery, work_unit, batch)`

Get or create the matching activity row. If the project has exactly one
delivery in the report, `delivery` can be omitted. Raises `ValueError` when
a project has multiple deliveries and none is specified.

Returns the same `TimesheetRow` object on repeated calls with the same
arguments — safe to call multiple times.

### `Timesheet.reassign_row(row_id, *, project, delivery, work_unit)`

Change the activity of an existing row. All day entries are preserved; their
activity assignment changes. If a row with the new assignment already exists,
entries are merged (durations accumulated per day). Returns `False` when the
row is not found or already has the requested assignment.

### `Timesheet.add_exceptional(...)`

Append an exceptional time entry. When the report has exactly one project and
delivery, `project` and `delivery` can be omitted; they are filled in
automatically.

### `Timesheet.save()`

Validates the payload against BoondManager's vendored schemas, PUTs the full
report, checks that the server persisted every sent entry, then refreshes local
state with server-assigned IDs. Raises:

- `TimesheetNotEditableError` — report is validated/closed.
- `BoondManagerValidationError` — payload broke the schema (bug in serialization).
- `BoondManagerSilentDropError` — server accepted fewer entries than sent (e.g. unknown row id).

### `Timesheet.work_unit_types_for(*activity_types)`

Returns the WUTs the resource may book, filtered by activity type and sorted
by name. Read from the report's `included` section; does not make an extra API
call.

```python
regular_wuts = ts.work_unit_types_for("internal")
exc_wuts     = ts.work_unit_types_for("exceptionalTime", "exceptionalCalendar")
```

### `Timesheet.project_options`

Selectable project/delivery pairs for this report, from the `included`
section. Present even when the report has no entries yet.

---

## The `TimesheetRow` class

| Method / property | Description |
|---|---|
| `row.set(date, duration)` | Upsert a day; `duration <= 0` removes the entry |
| `row.get(date)` | Duration for a day, or 0.0 |
| `row.clear()` | Remove every entry (deletes the row on save) |
| `row.days` | `{ISO date: duration}` dict for all days with time |
| `row.total` | Sum of durations |
| `row.label` | Human-readable name (project reference or WUT name) |
| `row.is_new` | True until the first save |
| `row.row_id` | Negative before save, server-assigned positive after |

---

## `TimesReport` domain methods

These live on the model and can be used without a live `Timesheet` instance
(e.g. for read-only display):

| Method | Description |
|---|---|
| `report.rows()` | Aggregated rows for display (excludes exceptional) |
| `report.editable_rows()` | Per-day entry grid for editing (excludes exceptional) |
| `report.absence_by_date()` | `{date: duration}` map of absence entries |
| `report.is_editable` | False when validated, approved, refused, or closed |

---

## Wire format reference

BoondManager's PUT schema has several non-obvious constraints that cause
**silent entry discard** (HTTP 200, nothing saved) when violated. The
`Timesheet` class handles all of these; they are documented here for context.

### Negative row ids create rows

`row <= -1` in a PUT entry tells BoondManager to create a new row
(`TAB_LIGNETEMPS`). All entries sharing the same negative value land on the
same new row. `row >= 1` must reference an existing row ID; unknown positive
IDs are silently discarded.

### Relationships must use the null-object form

Absent relationships must be `{"data": null}`, not bare `null` or a missing
key. Both fail the server-side schema and cause the entry to be silently
dropped.

```json
{ "project": {"data": null}, "delivery": {"id": "270"}, "batch": {"data": null} }
```

### `calendar` is not accepted in PUT bodies

The GET response contains a `calendar` key on entries. It is not listed in the
PUT schema (`additionalProperties: false`) and causes silent drop if included.

### `exceptionalTimes` entries must not include `duration`

The PUT schema for exceptional entries does not accept a `duration` field.
Duration is computed server-side from `startDate`/`endDate`.

### Deletion by omission

Omitting an entry from the PUT body deletes it. The PUT body must always be
the complete desired state of the report, not a diff.

---

## Validation

The client validates every PUT/POST body against BoondManager's vendored JSON
schemas before sending:

```python
# Raises BoondManagerValidationError with field-level detail before any HTTP call
await client.request("PUT", f"/times-reports/{id}", json=body)
```

After a PUT, `Timesheet.save()` compares the persisted entry count against the
sent count and raises `BoondManagerSilentDropError` when they diverge. This
catches schema-valid but semantically rejected entries (e.g. an entry referencing
a project the resource is no longer assigned to).

To skip pre-send validation (only when the published schema itself is wrong):

```python
await client.request("PUT", endpoint, json=body, validate=False)
```

---

## Error types

| Exception | When |
|---|---|
| `BoondManagerValidationError` | PUT/POST body fails vendored schema check |
| `BoondManagerSilentDropError` | Server persisted fewer entries than sent |
| `TimesheetNotEditableError` | `save()` called on a validated/closed report |
| `BoondManagerAPIError` | Non-2xx HTTP response |
| `BoondManagerError` | Network-level failure |
