# boondmanager

Async Python client for the [BoondManager API](https://doc.boondmanager.com/api-externe/).

## Why it's built this way

BoondManager validates write payloads against strict JSON schemas
(`additionalProperties: false`, all keys required) and **silently drops any
non-conforming item while returning HTTP 200**. A malformed timesheet entry
doesn't fail; it just never persists.

To make that class of bug impossible to reintroduce, the client is driven by
BoondManager's own published spec:

- `boondmanager/_spec/spec.json.gz` — vendored bundle: the full endpoint
  registry (598 endpoints, 844 methods) plus every published request-body
  JSON schema, extracted from their public RAML build.
- Every request body is validated against the matching schema **before
  sending**; mismatches raise `BoondManagerValidationError` with the exact
  violations instead of silently losing data.
- `update_times_report` additionally raises `BoondManagerSilentDropError`
  when the server returns 200 but persisted fewer entries than were sent
  (schema-valid but semantically rejected, e.g. a nonexistent row id).

## Three API layers

```python
from boondmanager import BoondManagerClient

async with BoondManagerClient(client_token=..., client_key=..., user_token=...) as client:
    # 1. High-level domain objects — no BoondManager quirks to know about
    ts = await client.fetch_timesheet("1652")
    ts.row(project="23").set("2026-06-30", 0.5)   # delivery auto-picked, rows managed
    await ts.save()                                # validated, silent-drop guarded

    # 2. Curated helpers returning pydantic models
    report = await client.get_times_report("1652")
    reports = await client.get_resource_times_reports(resource_id)
    projects = await client.get_resource_projects(resource_id)  # use .reference, not .title
    project = await client.get_project(projects[0].id)  # .company resolved
    types = await client.get_resource_type_dictionary()  # label -> id, cached

    # 3. Full generated surface — one namespace per resource, every endpoint
    doc = await client.api.times_reports.search(params={"period": "2026-06"})
    doc = await client.api.projects.get("23")
    await client.api.times_reports.validate("1652")
```

`client.api` (`boondmanager/api.py`, generated) covers the entire public API
as namespaces: `client.api.times_reports.update(id, body)`,
`client.api.resources.absences_reports(id)`, ... Its methods return
`Document` objects — dict-compatible JSON:API wrappers with navigation:

```python
doc = await client.api.times_reports.get("1652")
report = doc.one                       # Entity: report["term"], report.rel("projects")
for project in doc.included("project"):
    deliveries = doc.related(project, "deliveries")
```

`get_resource()` and `search_resources_by_email()` always resolve the
`mainManager`/`hrManager` relationships into full `Resource` objects,
including their email (one level deep, so a manager's own managers stay
`None`). Each manager can cost up to 2 extra GETs: one for the profile
(skipped if present in the response's `included` data) and one to
`/resources/{id}/information`, since the basic resource payload never
carries emails — up to 4 extra GETs per resource, up to 4N for a search
returning N results, though managers shared between results are only
resolved once per call. A dangling manager reference or a failed email
fetch (404) is logged and resolves to `None`/no email rather than failing
the whole call. That resolution runs concurrently, so the client caps
itself at 5 requests in flight at once by default — pass
`max_concurrent_requests=` to change it, or `semaphore=` to share one limit
across multiple client instances.

`api.ENDPOINT_INDEX` maps `("PUT", "/times-reports/{id}")` to
`("times_reports", "update")` for programmatic discovery, and
`client.request(method, path, json=..., params=..., validate=True)` is the
underlying escape hatch.

To find a method, grep [`docs/API.md`](docs/API.md) — one line per endpoint
method with its required query params. Each generated method's docstring
documents all query parameters (name, type, required, enum, default) and the
request-body schema name.

## Timesheet gotchas (learned the hard way)

`Timesheet` (layer 1) absorbs all of these; they only matter when using the
lower layers directly.

- `regularTimes` entries: `row <= -1` creates a new row (entries sharing the
  same negative value land on the same row); `row >= 1` must reference an
  existing row id. Unknown positive ids are silently discarded.
- Missing relationships are `{"data": null}`, never a bare `null` or an
  omitted key.
- `exceptionalTimes` have no `duration`/`row`, and `project`/`delivery` are
  mandatory there.
- BoondManager **mirrors `exceptionalTimes` entries into `regularTimes`** for
  activity totals. Always filter by `activity_type in {"exceptionalTime",
  "exceptionalCalendar"}` before iterating `regularTimes` — `rows()` and
  `editable_rows()` on `TimesReport` already do this.
- Keys that appear in GET responses (`calendar`, entry `id`s for new items)
  are not accepted in PUT bodies.

## Regenerating the spec and API surface

When BoondManager publishes API changes:

```bash
uv run scripts/fetch_spec.py     # re-download RAML + schemas -> _spec/spec.json.gz
uv run scripts/generate_api.py   # regenerate boondmanager/api.py + docs/API.md
uv run pytest                    # sanity: registry, validation, api surface
```

A handful of schemas are referenced by the RAML but not published (listed in
`scripts/fetch_spec.py`); those endpoints work but skip pre-send validation.
