"""Tests for curated client helpers built on the generated API (no network)."""

import asyncio

import pytest

from boondmanager import BoondManagerClient, CreateAbsencePeriod
from boondmanager.exceptions import BoondManagerError, BoondManagerSilentDropError
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


def test_get_resource_times_reports_returns_summaries():
    client = make_client(
        {
            "data": [
                {
                    "id": "100",
                    "type": "timesreport",
                    "attributes": {"term": "2026-06", "state": "validated", "closed": True},
                },
                {
                    "id": "101",
                    "type": "timesreport",
                    "attributes": {"term": "2026-07", "state": "savedAndNoValidation"},
                },
            ]
        }
    )
    reports = asyncio.run(client.get_resource_times_reports("42"))
    assert [(r.id, r.term, r.is_editable) for r in reports] == [
        ("100", "2026-06", False),
        ("101", "2026-07", True),
    ]
    assert client.last_call == ("GET", "/resources/42/times-reports", None)


_FULL_REPORT = {
    "data": {
        "id": "100",
        "type": "timesreport",
        "attributes": {
            "term": "2026-06",
            "state": "savedAndNoValidation",
            "closed": False,
            "regularTimes": [
                {
                    "id": "7",
                    "startDate": "2026-06-01",
                    "duration": 1.0,
                    "row": 3,
                    "workUnitType": {
                        "reference": 1,
                        "activityType": "production",
                        "name": "Normale",
                    },
                    "project": {"id": "P1", "reference": "PRJ1"},
                }
            ],
            "exceptionalTimes": [],
            "absencesTimes": [],
        },
    },
    "included": [{"id": "P1", "type": "project", "attributes": {"reference": "PRJ1"}}],
}


def test_get_times_report_full_detail():
    client = make_client(_FULL_REPORT)
    report = asyncio.run(client.get_times_report("100"))
    assert report.term == "2026-06"
    entries = report.attributes.regular_times
    assert len(entries) == 1
    assert entries[0].project.reference == "PRJ1"
    assert entries[0].activity_name == "PRJ1"
    assert [(row.name, row.total_days) for row in report.rows()] == [("PRJ1", 1.0)]


def test_get_times_report_with_included_returns_included_list():
    client = make_client(_FULL_REPORT)
    report, included = asyncio.run(client.get_times_report_with_included("100"))
    assert report.id == "100"
    assert included == _FULL_REPORT["included"]


def test_update_times_report_raises_on_silent_drop():
    # Server returns 200 but persisted zero of the one entry sent.
    report = TimesReport.model_validate(_FULL_REPORT["data"])
    client = make_client(
        {
            "data": {
                "id": "100",
                "type": "timesreport",
                "attributes": {
                    "term": "2026-06",
                    "state": "savedAndNoValidation",
                    "regularTimes": [],
                    "exceptionalTimes": [],
                },
            }
        }
    )
    with pytest.raises(BoondManagerSilentDropError, match="regularTimes"):
        asyncio.run(client.update_times_report(report))


def test_get_resource_absences_reports_returns_periods():
    client = make_client(
        {
            "data": [
                {
                    "id": "200",
                    "type": "absencesreport",
                    "attributes": {
                        "state": "waitingForValidation",
                        "absencesPeriods": [
                            {
                                "id": "1",
                                "startDate": "2026-08-01",
                                "endDate": "2026-08-05",
                                "duration": 5.0,
                                "title": "Congés payés",
                            }
                        ],
                    },
                }
            ]
        }
    )
    reports = asyncio.run(client.get_resource_absences_reports("42"))
    assert reports[0].state == "waitingForValidation"
    assert [(p.start_date, p.duration) for p in reports[0].periods] == [("2026-08-01", 5.0)]
    assert client.last_call == ("GET", "/resources/42/absences-reports", None)


def test_create_absences_report_posts_correct_body():
    client = make_client(
        {
            "data": {
                "id": "201",
                "type": "absencesreport",
                "attributes": {"state": "waitingForValidation"},
            }
        }
    )
    period = CreateAbsencePeriod(
        start_date="2026-08-01",
        end_date="2026-08-05",
        duration=5.0,
        title="Congés payés",
        work_unit_type_reference=2,
    )
    report = asyncio.run(
        client.create_absences_report("42", [period], comments="Vacances")
    )
    assert report.id == "201"
    body = client.last_body["data"]
    assert body["type"] == "absencesreport"
    assert body["relationships"]["resource"]["data"] == {"id": "42", "type": "resource"}
    assert body["attributes"]["informationComments"] == "Vacances"
    assert body["attributes"]["absencesPeriods"] == [
        {
            "startDate": "2026-08-01",
            "endDate": "2026-08-05",
            "duration": 5.0,
            "title": "Congés payés",
            "workUnitType": {"reference": 2},
        }
    ]


def test_create_absences_report_omits_comments_when_empty():
    client = make_client(
        {"data": {"id": "202", "type": "absencesreport", "attributes": {}}}
    )
    period = CreateAbsencePeriod(
        start_date="2026-08-01",
        end_date="2026-08-01",
        duration=1.0,
        title="RTT",
        work_unit_type_reference=3,
    )
    asyncio.run(client.create_absences_report("42", [period]))
    assert "informationComments" not in client.last_body["data"]["attributes"]


def test_get_current_user():
    client = make_client(
        {
            "data": {
                "id": "9",
                "type": "resource",
                "attributes": {
                    "firstName": "Paul",
                    "lastName": "Mrabet",
                    "login": "pm",
                    "email1": "pm@lenstra.fr",
                },
            }
        }
    )
    user = asyncio.run(client.get_current_user())
    assert user.resource_id == "9"
    assert user.full_name == "Paul Mrabet"
    assert client.last_call == ("GET", "/application/current-user", None)


def test_get_dictionary_returns_raw_response_untouched():
    raw = {"data": {"id": "1", "attributes": {"setting": {"anything": True}}}}
    client = make_client(raw)
    assert asyncio.run(client.get_dictionary()) is raw


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
