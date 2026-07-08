"""Tests for curated client helpers built on the generated API (no network)."""

import asyncio

import pytest

from boondmanager import BoondManagerClient
from boondmanager.exceptions import BoondManagerError
from boondmanager.models import TimesReport


def make_client(response: dict) -> BoondManagerClient:
    client = BoondManagerClient(client_token="t", client_key="k")

    async def fake_request(method, endpoint, **kwargs):
        client.last_call = (method, endpoint, kwargs.get("params"))
        client.last_body = kwargs.get("json")
        return response

    client.request = fake_request
    return client


def test_get_absence_types_filters_and_sorts():
    client = make_client(
        {
            "data": {},
            "included": [
                {
                    "id": "2",
                    "type": "resource",
                    "attributes": {
                        "workUnitTypesAllowed": [
                            {"reference": 5, "activityType": "absence", "name": "Maladie"},
                            {"reference": 2, "activityType": "absence", "name": "CP"},
                            {"reference": 1, "activityType": "production", "name": "Normale"},
                        ]
                    },
                }
            ],
        }
    )
    types = asyncio.run(client.get_absence_types("2"))
    assert [(w.reference, w.name) for w in types] == [(2, "CP"), (5, "Maladie")]
    assert client.last_call == (
        "GET",
        "/absences-reports/default",
        {"resource": "2"},
    )


def test_count_working_days_excludes_weekends_and_holidays():
    client = make_client(
        {
            "data": [
                {"date": "2026-07-13", "weekend": False, "bankHoliday": False},
                {"date": "2026-07-14", "weekend": False, "bankHoliday": True},
                {"date": "2026-07-15", "weekend": False, "bankHoliday": False},
                {"date": "2026-07-18", "weekend": True, "bankHoliday": False},
            ]
        }
    )
    assert asyncio.run(client.count_working_days("2026-07-13", "2026-07-18")) == 2.0


def test_create_times_report_posts_correct_body():
    client = make_client(
        {
            "data": {
                "id": "999",
                "type": "timesreport",
                "attributes": {
                    "term": "2026-08",
                    "state": "savedAndNoValidation",
                    "closed": False,
                    "regularTimes": [],
                    "exceptionalTimes": [],
                    "absencesTimes": [],
                },
            }
        }
    )
    report = asyncio.run(client.create_times_report("42", "2026-08"))
    assert report.id == "999"
    assert report.term == "2026-08"
    assert client.last_call[:2] == ("POST", "/times-reports")
    body = client.last_body
    assert body["data"]["attributes"]["term"] == "2026-08"
    assert body["data"]["relationships"]["resource"]["data"] == {
        "id": "42",
        "type": "resource",
    }


# ---------------------------------------------------------------------------
# _item
# ---------------------------------------------------------------------------


def test_item_returns_dict():
    d = {"id": "1", "type": "resource"}
    assert BoondManagerClient._item({"data": d}) is d


def test_item_raises_on_null_data():
    with pytest.raises(BoondManagerError, match="NoneType"):
        BoondManagerClient._item({"data": None})


def test_item_raises_on_missing_data():
    with pytest.raises(BoondManagerError, match="NoneType"):
        BoondManagerClient._item({})


def test_item_raises_on_list_data():
    with pytest.raises(BoondManagerError, match="list"):
        BoondManagerClient._item({"data": [{"id": "1"}]})


# ---------------------------------------------------------------------------
# _list
# ---------------------------------------------------------------------------


def test_list_returns_list_unchanged():
    items = [{"id": "1"}, {"id": "2"}]
    assert BoondManagerClient._list({"data": items}) == items


def test_list_wraps_single_dict():
    d = {"id": "1"}
    assert BoondManagerClient._list({"data": d}) == [d]


def test_list_returns_empty_on_null_data():
    assert BoondManagerClient._list({"data": None}) == []


def test_list_returns_empty_on_missing_data():
    assert BoondManagerClient._list({}) == []


# ---------------------------------------------------------------------------
# TimesReport.is_editable — allowlist behaviour
# ---------------------------------------------------------------------------


def _report(state: str, closed: bool = False) -> TimesReport:
    return TimesReport.model_validate(
        {"id": "1", "attributes": {"term": "2026-07", "state": state, "closed": closed}}
    )


def test_is_editable_known_editable_states():
    assert _report("savedAndNoValidation").is_editable is True
    assert _report("savedAndWaitingForValidation").is_editable is True


def test_is_editable_known_terminal_states():
    for state in ("validated", "approved", "refused"):
        assert _report(state).is_editable is False, f"state {state!r} should be non-editable"


def test_is_editable_unknown_state_treated_as_non_editable():
    assert _report("someNewStateFromBoondManager").is_editable is False


def test_is_editable_closed_flag_overrides_state():
    assert _report("savedAndNoValidation", closed=True).is_editable is False
