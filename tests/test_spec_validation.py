"""Tests for the vendored spec, request validation, and generated API surface."""

import asyncio

import pytest

from boondmanager import (
    BoondManagerClient,
    BoondManagerSilentDropError,
    BoondManagerValidationError,
    DeliveryRef,
    ProjectRef,
    TimeEntry,
    TimesReport,
    WorkUnitType,
)
from boondmanager import spec
from boondmanager.client import _validate_request_body


def make_client() -> BoondManagerClient:
    return BoondManagerClient(client_token="t", client_key="k", user_token="u")


def entry(**overrides) -> TimeEntry:
    defaults = dict(
        id="-1",
        start_date="2026-06-30",
        duration=0.5,
        row=-1,
        work_unit_type=WorkUnitType(reference=1),
        project=ProjectRef(id="23"),
        delivery=DeliveryRef(id="270"),
    )
    defaults.update(overrides)
    return TimeEntry(**defaults)


def times_report_body(entries: list[TimeEntry]) -> dict:
    return {
        "data": {
            "type": "timesreport",
            "id": "1652",
            "attributes": {
                "regularTimes": [e.to_api_regular() for e in entries],
                "exceptionalTimes": [],
            },
        }
    }


# ---------------------------------------------------------------------------
# Spec registry
# ---------------------------------------------------------------------------


def test_registry_is_complete():
    eps = spec.endpoints()
    assert len(eps) >= 590
    assert sum(len(e["methods"]) for e in eps) >= 840


def test_match_resolves_path_params():
    info = spec.match("PUT", "/times-reports/1652")
    assert info["path"] == "/times-reports/{id}"
    assert info["body_schema"] == "timesReportsBody-put"


def test_match_prefers_literal_over_param():
    info = spec.match("GET", "/times-reports/default")
    assert info["path"] == "/times-reports/default"


def test_match_unknown_path():
    assert spec.match("GET", "/no-such-endpoint") is None


def test_referenced_schemas_are_vendored():
    # every write method's schema must be vendored, except the ones the
    # public RAML references but does not publish (fetch_spec.py warning)
    missing = {
        name
        for e in spec.endpoints()
        for m in e["methods"].values()
        if (name := m["body_schema"]) and spec.schema(name) is None
    }
    assert len(missing) <= 20, f"unexpectedly missing schemas: {sorted(missing)}"


# ---------------------------------------------------------------------------
# Request-body validation
# ---------------------------------------------------------------------------


def test_valid_timesheet_body_passes():
    _validate_request_body("PUT", "/times-reports/1652", times_report_body([entry()]))


def test_pre_fix_buggy_payload_is_rejected():
    """The exact payload shape that caused the June 2026 silent data loss."""
    body = times_report_body([entry()])
    buggy = body["data"]["attributes"]["regularTimes"][0]
    buggy["calendar"] = "calendar"  # extra key, additionalProperties: false
    buggy["batch"] = None  # must be {"data": null}
    with pytest.raises(BoondManagerValidationError) as exc:
        _validate_request_body("PUT", "/times-reports/1652", body)
    assert "timesReportsBody-put" in str(exc.value)


def test_unknown_positive_entry_id_type_rejected():
    body = times_report_body([entry()])
    body["data"]["attributes"]["regularTimes"][0]["duration"] = "half a day"
    with pytest.raises(BoondManagerValidationError):
        _validate_request_body("PUT", "/times-reports/1652", body)


def test_exceptional_serialization_passes():
    e = entry(
        id="-2",
        start_date="2026-06-15T08:00:00+0200",
        end_date="2026-06-15T10:00:00+0200",
        duration=7200,
        work_unit_type=WorkUnitType(reference=12),
        description="astreinte",
    )
    body = {
        "data": {
            "type": "timesreport",
            "id": "1652",
            "attributes": {"regularTimes": [], "exceptionalTimes": [e.to_api_exceptional()]},
        }
    }
    _validate_request_body("PUT", "/times-reports/1652", body)


def test_absences_report_body_passes():
    from boondmanager import CreateAbsencePeriod

    period = CreateAbsencePeriod(
        start_date="2026-08-01",
        end_date="2026-08-05",
        duration=5.0,
        title="Congés payés",
        work_unit_type_reference=2,
    )
    body = {
        "data": {
            "type": "absencesreport",
            "attributes": {"absencesPeriods": [period.to_api()]},
            "relationships": {
                "resource": {"data": {"id": "42", "type": "resource"}}
            },
        }
    }
    _validate_request_body("POST", "/absences-reports", body)


# ---------------------------------------------------------------------------
# Client integration (no network)
# ---------------------------------------------------------------------------


def test_client_request_validates_before_send():
    """A schema-invalid body raises before any HTTP request is attempted."""
    client = make_client()
    bad = times_report_body([entry()])
    bad["data"]["attributes"]["regularTimes"][0]["calendar"] = "calendar"
    with pytest.raises(BoondManagerValidationError):
        asyncio.run(client.request("PUT", "/times-reports/1652", json=bad))


def test_update_times_report_raises_on_silent_drop(monkeypatch):
    client = make_client()

    async def fake_request(method, endpoint, **kwargs):
        return {
            "data": {
                "id": "1652",
                "attributes": {"term": "2026-06", "regularTimes": []},
            }
        }

    monkeypatch.setattr(client, "request", fake_request)
    report = TimesReport.model_validate(
        {"id": "1652", "attributes": {"term": "2026-06"}}
    )
    report.attributes.regular_times.append(entry())
    with pytest.raises(BoondManagerSilentDropError):
        asyncio.run(client.update_times_report(report))


# ---------------------------------------------------------------------------
# Generated API surface
# ---------------------------------------------------------------------------


def test_generated_api_covers_every_endpoint():
    from boondmanager.api import BoondManagerAPI, ENDPOINT_INDEX

    api = BoondManagerAPI(make_client())
    spec_methods = {
        (verb.upper(), e["path"])
        for e in spec.endpoints()
        for verb in e["methods"]
    }
    assert set(ENDPOINT_INDEX) == spec_methods
    for group_attr, method in ENDPOINT_INDEX.values():
        group = getattr(api, group_attr)
        assert callable(getattr(group, method))


def test_generated_docstrings_document_query_params():
    client = make_client()
    doc = client.api.times_reports.search.__doc__
    assert "startMonth (string, REQUIRED)" in doc
    assert "endMonth (string, REQUIRED)" in doc
    assert "page (number" in doc  # inherited from the pagination trait


def test_api_index_doc_is_in_sync():
    import pathlib

    from boondmanager.api import ENDPOINT_INDEX

    import re

    docs = pathlib.Path(__file__).parent.parent / "docs" / "API.md"
    method_line = re.compile(r"^- `.+\(.*\)` — (GET|POST|PUT|DELETE) /")
    lines = [l for l in docs.read_text().splitlines() if method_line.match(l)]
    assert len(lines) == len(ENDPOINT_INDEX)


def test_generated_method_hits_validation():
    client = make_client()
    bad_body = {"data": {"type": "timesreport", "id": "1", "attributes": {"regularTimes": [{"nope": 1}]}}}
    with pytest.raises(BoondManagerValidationError):
        asyncio.run(client.api.times_reports.update("1", bad_body))
