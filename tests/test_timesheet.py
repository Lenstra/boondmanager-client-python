"""Tests for the high-level Timesheet editing API (no network)."""

import asyncio
import copy

import pytest

from boondmanager import (
    BoondManagerClient,
    Timesheet,
    TimesheetNotEditableError,
)

INCLUDED = [
    {
        "id": "23",
        "type": "project",
        "attributes": {"reference": "AZTech - Lead Consulting"},
        "relationships": {"deliveries": {"data": [{"id": "270", "type": "delivery"}]}},
    },
    {
        "id": "270",
        "type": "delivery",
        "attributes": {"title": "", "startDate": "2026-01-01", "endDate": "2026-12-31"},
    },
    {
        "id": "2",
        "type": "resource",
        "attributes": {
            "workUnitTypesAllowed": [
                {"reference": 1, "activityType": "production", "name": "Normale"},
                {"reference": 7, "activityType": "internal", "name": "Structure"},
                {"reference": 9, "activityType": "internal", "name": "Formation"},
                {"reference": 11, "activityType": "exceptionalCalendar", "name": "Astreinte"},
                {"reference": 2, "activityType": "absence", "name": "CP"},
            ]
        },
    },
]

EMPTY_REPORT = {
    "id": "1652",
    "type": "timesreport",
    "attributes": {
        "term": "2026-06",
        "state": "savedAndNoValidation",
        "closed": False,
        "regularTimes": [],
        "exceptionalTimes": [],
        "absencesTimes": [],
    },
}


def server_echo(sent_attributes: dict) -> dict:
    """Simulate BoondManager persisting a PUT: assign real ids and rows."""
    data = copy.deepcopy(EMPTY_REPORT)
    row_map: dict = {}
    for i, e in enumerate(sent_attributes.get("regularTimes", [])):
        saved = copy.deepcopy(e)
        saved["id"] = str(33000 + i)
        row = saved.get("row")
        if row is not None and row < 0:
            row_map.setdefault(row, 2900 + len(row_map))
            saved["row"] = row_map[row]
        data["attributes"]["regularTimes"].append(saved)
    for i, e in enumerate(sent_attributes.get("exceptionalTimes", [])):
        saved = copy.deepcopy(e)
        saved["id"] = str(44000 + i)
        saved.setdefault("duration", 1)
        data["attributes"]["exceptionalTimes"].append(saved)
    return data


def make_client(report_data=None):
    """Real client with the HTTP layer replaced by an echoing fake server."""
    client = BoondManagerClient(client_token="t", client_key="k")
    state = {"report": copy.deepcopy(report_data or EMPTY_REPORT), "puts": []}
    real_request = client.request

    async def fake_request(method, endpoint, *, validate=True, **kwargs):
        if method == "GET":
            return {"data": copy.deepcopy(state["report"]), "included": INCLUDED}
        if method == "PUT":
            if validate and kwargs.get("json") is not None:
                # run the real pre-send validation
                from boondmanager.client import _validate_request_body

                _validate_request_body(method, endpoint, kwargs["json"])
            sent = kwargs["json"]["data"]["attributes"]
            state["puts"].append(sent)
            state["report"] = server_echo(sent)
            return {"data": copy.deepcopy(state["report"])}
        raise AssertionError(f"unexpected {method} {endpoint}")

    client.request = fake_request
    client._state = state
    return client


def fetch(client) -> Timesheet:
    return asyncio.run(Timesheet.fetch(client, "1652"))


def test_row_autopicks_single_delivery():
    ts = fetch(make_client())
    row = ts.row(project="23")
    assert row.delivery.id == "270"
    assert row.is_new and row.row_id < 0
    assert row.label == "AZTech - Lead Consulting"


def test_row_is_get_or_create():
    ts = fetch(make_client())
    assert ts.row(project="23") is ts.row(project="23", delivery="270")
    assert len(ts.rows) == 1
    internal = ts.row(work_unit=7)
    assert internal is not ts.row(project="23")
    assert len(ts.rows) == 2


def test_set_and_remove_days():
    ts = fetch(make_client())
    row = ts.row(project="23")
    row.set("2026-06-30", 0.5)
    row.set("2026-06-29", 1)
    assert row.total == 1.5
    row.set("2026-06-29", 0)
    assert row.days == {"2026-06-30": 0.5}


def test_save_sends_valid_body_and_refreshes_ids():
    client = make_client()
    ts = fetch(client)
    ts.row(project="23").set("2026-06-30", 0.5)
    asyncio.run(ts.save())

    sent = client._state["puts"][0]
    assert sent["regularTimes"][0]["row"] == -1  # create-row semantics
    assert "id" not in sent["regularTimes"][0]  # new entry: no id
    assert sent["regularTimes"][0]["batch"] == {"data": None}

    # after refresh, server-assigned ids replace the synthetic ones
    row = ts.rows[0]
    assert not row.is_new and row.row_id == 2900
    assert ts.entry("33000").duration == 0.5


def test_save_existing_entry_updates_by_id():
    client = make_client()
    ts = fetch(client)
    ts.row(project="23").set("2026-06-30", 0.5)
    asyncio.run(ts.save())

    ts.set_entry_duration("33000", 1.0)
    asyncio.run(ts.save())
    sent = client._state["puts"][1]
    assert sent["regularTimes"][0]["id"] == "33000"
    assert sent["regularTimes"][0]["duration"] == 1.0
    assert sent["regularTimes"][0]["row"] == 2900


def test_save_refuses_validated_report():
    data = copy.deepcopy(EMPTY_REPORT)
    data["attributes"]["state"] = "validated"
    ts = fetch(make_client(data))
    ts.row(project="23").set("2026-06-30", 1)
    with pytest.raises(TimesheetNotEditableError):
        asyncio.run(ts.save())


def test_add_exceptional_autofills_project_and_delivery():
    client = make_client()
    ts = fetch(client)
    entry = ts.add_exceptional(
        start="2026-06-15T08:00:00+0200",
        end="2026-06-15T10:00:00+0200",
        duration=7200,
        work_unit=12,
        activity_type="exceptionalTime",
        description="astreinte",
    )
    assert entry.project.id == "23"
    assert entry.delivery.id == "270"
    asyncio.run(ts.save())
    sent = client._state["puts"][0]
    assert sent["exceptionalTimes"][0]["description"] == "astreinte"
    assert "duration" not in sent["exceptionalTimes"][0]


def test_project_options_from_included():
    ts = fetch(make_client())
    assert ts.project_options == [
        {"project_id": "23", "delivery_id": "270", "label": "AZTech - Lead Consulting"}
    ]


def test_work_unit_types_from_included():
    ts = fetch(make_client())
    assert [w.name for w in ts.work_unit_types_for("internal")] == [
        "Formation",
        "Structure",
    ]
    exc = ts.work_unit_types_for("exceptionalTime", "exceptionalCalendar")
    assert [w.reference for w in exc] == [11]


def test_rows_excludes_exceptional_activity_types():
    # BoondManager mirrors exceptional entries into regularTimes; rows() must not count them.
    data = copy.deepcopy(EMPTY_REPORT)
    data["attributes"]["regularTimes"] = [
        {
            "id": "100",
            "startDate": "2026-06-10",
            "duration": 1.0,
            "row": 99,
            "workUnitType": {"reference": 11, "activityType": "exceptionalCalendar", "name": "Astreinte"},
            "project": {"data": None},
            "delivery": {"data": None},
            "batch": {"data": None},
        }
    ]
    from boondmanager.models import TimesReport
    report = TimesReport.model_validate({"id": "1652", "type": "timesreport", "attributes": data["attributes"]})
    assert report.rows() == []
    assert report.editable_rows() == []


def test_reassign_row_changes_activity_and_preserves_days():
    client = make_client()
    ts = fetch(client)
    ts.row(project="23").set("2026-06-30", 0.5)
    asyncio.run(ts.save())

    row_id = ts.rows[0].row_id
    ts.reassign_row(row_id, project=None, delivery=None, work_unit=7)

    assert ts.row_by_id(row_id) is None
    assert len(ts.rows) == 1
    new_row = ts.rows[0]
    assert new_row.work_unit_type.reference == 7
    assert new_row.days == {"2026-06-30": 0.5}


def test_reassign_row_merges_into_existing_row():
    # If the target activity already has a row, days are merged into it.
    client = make_client()
    ts = fetch(client)
    ts.row(project="23").set("2026-06-30", 0.5)
    ts.row(work_unit=7).set("2026-06-30", 0.5)
    asyncio.run(ts.save())

    proj_row_id = next(r.row_id for r in ts.rows if r.project)
    wut_row_id = next(r.row_id for r in ts.rows if not r.project)

    ts.reassign_row(proj_row_id, project=None, delivery=None, work_unit=7)

    # Merged into the existing wut:7 row; no orphaned rows remain.
    assert ts.row_by_id(proj_row_id) is None
    assert len(ts.rows) == 1
    merged = ts.rows[0]
    assert merged.row_id == wut_row_id
    assert merged.days == {"2026-06-30": 1.0}  # 0.5 + 0.5


def test_reassign_row_noop_when_already_matches():
    client = make_client()
    ts = fetch(client)
    ts.row(project="23").set("2026-06-30", 0.5)
    asyncio.run(ts.save())

    row_id = ts.rows[0].row_id
    result = ts.reassign_row(row_id, project="23", delivery="270", work_unit=1)
    assert result is False
    assert len(ts.rows) == 1


def test_drop_row_omits_entries_from_save():
    client = make_client()
    ts = fetch(client)
    ts.row(project="23").set("2026-06-30", 0.5)
    asyncio.run(ts.save())

    row = ts.rows[0]
    row.clear()
    ts.rows = [r for r in ts.rows if r is not row]

    asyncio.run(ts.save())
    sent = client._state["puts"][1]
    assert sent["regularTimes"] == []


def test_report_parses_absence_without_id():
    # A fresh report with a pending absence request returns absencesTimes without an id.
    from boondmanager.models import TimesReport

    report = TimesReport.model_validate({
        "id": "1", "type": "timesreport",
        "attributes": {"term": "2026-01", "state": "savedAndNoValidation", "absencesTimes": [
            {"startDate": "2026-01-15", "duration": 0.5,
             "workUnitType": {"reference": 2, "activityType": "absence", "name": "CP"}},
        ]},
    })
    assert report.absence_by_date() == {"2026-01-15": 0.5}
