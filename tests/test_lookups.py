"""Tests for positioning/project/company lookups, manager resolution, and the
resource-type dictionary. No network."""

import asyncio
from datetime import date

import pytest

from boondmanager import BoondManagerClient
from boondmanager.exceptions import BoondManagerAPIError, BoondManagerError


def make_client(responses: dict) -> BoondManagerClient:
    """Fake client whose request() serves canned responses keyed by endpoint.

    A value that is an Exception instance is raised instead of returned.
    Every call is recorded in ``client.calls`` for call-count assertions.
    """
    client = BoondManagerClient(client_token="t", client_key="k")
    client.calls = []

    async def fake_request(method, endpoint, **kwargs):
        client.calls.append((method, endpoint, kwargs.get("params")))
        resp = responses[endpoint]
        if isinstance(resp, Exception):
            raise resp
        return resp

    client.request = fake_request
    return client


def _resource_item(rid: str, relationships: dict | None = None) -> dict:
    # Confirmed against a live instance: GET /resources/{id} never returns
    # email fields; they live on GET /resources/{id}/information instead
    # (see _info_response below).
    item = {
        "id": rid,
        "type": "resource",
        "attributes": {"firstName": f"First{rid}", "lastName": f"Last{rid}"},
    }
    if relationships is not None:
        item["relationships"] = relationships
    return item


def _info_response(rid: str, email1: str | None = None) -> dict:
    attrs = {"email1": email1} if email1 else {}
    return {"data": {"id": rid, "type": "resource", "attributes": attrs}}


def _rel(rid: str, rtype: str = "resource") -> dict:
    return {"data": {"id": rid, "type": rtype}}


# ---------------------------------------------------------------------------
# get_resource_positionings
# ---------------------------------------------------------------------------


def test_get_resource_positionings_returns_dates():
    # Confirmed against a live instance: a positioning has no "project"
    # relationship (only "dependsOn" and "opportunity"), so Positioning
    # carries no project_id. Use get_resource_projects() for that.
    client = make_client(
        {
            "/resources/123/positionings": {
                "data": [
                    {
                        "id": "10",
                        "type": "positioning",
                        "attributes": {"startDate": "2026-01-01", "endDate": "2026-06-30"},
                    },
                    {
                        "id": "11",
                        "type": "positioning",
                        "attributes": {"startDate": "2026-07-01", "endDate": ""},
                    },
                ]
            }
        }
    )
    positionings = asyncio.run(client.get_resource_positionings("123"))
    assert [p.id for p in positionings] == ["10", "11"]
    assert positionings[0].start_date == date(2026, 1, 1)
    assert positionings[0].end_date == date(2026, 6, 30)
    assert positionings[1].end_date is None  # empty string coerced to None
    assert client.calls == [("GET", "/resources/123/positionings", None)]


def test_get_resource_positionings_empty():
    client = make_client({"/resources/123/positionings": {"data": []}})
    assert asyncio.run(client.get_resource_positionings("123")) == []


# ---------------------------------------------------------------------------
# get_resource_projects
# ---------------------------------------------------------------------------


def test_get_resource_projects_returns_summaries():
    client = make_client(
        {
            "/resources/123/projects": {
                "data": [
                    {
                        "id": "P1",
                        "type": "project",
                        "attributes": {"title": "Mission A", "reference": "PRJ1", "state": 1},
                    },
                    {
                        "id": "P2",
                        "type": "project",
                        "attributes": {"title": "Mission B", "reference": "PRJ2", "state": 2},
                    },
                ]
            }
        }
    )
    projects = asyncio.run(client.get_resource_projects("123"))
    assert [(p.id, p.title, p.reference, p.state) for p in projects] == [
        ("P1", "Mission A", "PRJ1", 1),
        ("P2", "Mission B", "PRJ2", 2),
    ]


def test_get_resource_projects_empty():
    client = make_client({"/resources/123/projects": {"data": []}})
    assert asyncio.run(client.get_resource_projects("123")) == []


def test_get_resource_projects_title_absent_is_none():
    # Confirmed against a live instance: this endpoint never sends "title".
    # "reference" is the real display name.
    client = make_client(
        {
            "/resources/123/projects": {
                "data": [
                    {
                        "id": "P1",
                        "type": "project",
                        "attributes": {"reference": "Kering - Professional Services"},
                    }
                ]
            }
        }
    )
    projects = asyncio.run(client.get_resource_projects("123"))
    assert projects[0].title is None
    assert projects[0].reference == "Kering - Professional Services"


# ---------------------------------------------------------------------------
# get_project
# ---------------------------------------------------------------------------


def _project_item(company_rel: dict | None) -> dict:
    # Confirmed against a live instance: real projects don't send "title" or
    # "endDate"; "reference" is the display name. "endDate" stays supported
    # by the model in case some project type does send it.
    item = {
        "id": "P1",
        "type": "project",
        "attributes": {
            "reference": "PRJ1",
            "state": 1,
            "startDate": "2026-01-01",
        },
    }
    if company_rel is not None:
        item["relationships"] = {"company": company_rel}
    return item


def test_get_project_with_included_company():
    client = make_client(
        {
            "/projects/P1": {
                "data": _project_item(_rel("C1", "company")),
                "included": [
                    {"id": "C1", "type": "company", "attributes": {"name": "Acme Corp"}}
                ],
            }
        }
    )
    project = asyncio.run(client.get_project("P1"))
    assert project.title is None
    assert project.reference == "PRJ1"
    assert project.start_date == date(2026, 1, 1)
    assert project.end_date is None
    assert project.company.id == "C1"
    assert project.company.name == "Acme Corp"
    # Company resolved from included data: no extra call
    assert len(client.calls) == 1


def test_get_project_without_company():
    client = make_client({"/projects/P1": {"data": _project_item(None)}})
    project = asyncio.run(client.get_project("P1"))
    assert project.company is None


def test_get_project_company_not_included_is_fetched():
    client = make_client(
        {
            "/projects/P1": {"data": _project_item(_rel("C1", "company"))},
            "/companies/C1": {
                "data": {"id": "C1", "type": "company", "attributes": {"name": "Acme Corp"}}
            },
        }
    )
    project = asyncio.run(client.get_project("P1"))
    assert project.company.name == "Acme Corp"
    assert ("GET", "/companies/C1", None) in client.calls


def test_get_project_dangling_company_resolves_to_none():
    client = make_client(
        {
            "/projects/P1": {"data": _project_item(_rel("C404", "company"))},
            "/companies/C404": BoondManagerAPIError(404, "/companies/C404", "not found"),
        }
    )
    project = asyncio.run(client.get_project("P1"))
    assert project.company is None


def test_get_project_404_propagates():
    client = make_client(
        {"/projects/P404": BoondManagerAPIError(404, "/projects/P404", "not found")}
    )
    with pytest.raises(BoondManagerAPIError) as exc_info:
        asyncio.run(client.get_project("P404"))
    assert exc_info.value.status_code == 404


# ---------------------------------------------------------------------------
# get_company
# ---------------------------------------------------------------------------


def test_get_company():
    client = make_client(
        {
            "/companies/C1": {
                "data": {"id": "C1", "type": "company", "attributes": {"name": "Acme Corp"}}
            }
        }
    )
    company = asyncio.run(client.get_company("C1"))
    assert (company.id, company.name) == ("C1", "Acme Corp")


def test_get_company_404_propagates():
    client = make_client(
        {"/companies/C404": BoondManagerAPIError(404, "/companies/C404", "not found")}
    )
    with pytest.raises(BoondManagerAPIError) as exc_info:
        asyncio.run(client.get_company("C404"))
    assert exc_info.value.status_code == 404


# ---------------------------------------------------------------------------
# get_resource — basic fields
# ---------------------------------------------------------------------------


def test_get_resource_basic_fields_still_parsed():
    client = make_client(
        {
            "/resources/42": {
                "data": {
                    "id": "42",
                    "type": "resource",
                    "attributes": {
                        "firstName": "Jane",
                        "lastName": "Doe",
                        "email1": "jane@lenstra.fr",
                        "email2": "jane@perso.fr",
                        "state": 1,
                        "typeOf": 4,
                        "title": "Consultante",
                    },
                }
            }
        }
    )
    resource = asyncio.run(client.get_resource("42"))
    assert resource.id == "42"
    assert resource.full_name == "Jane Doe"
    assert resource.attributes.emails() == ["jane@lenstra.fr", "jane@perso.fr"]
    assert resource.attributes.has_email("JANE@LENSTRA.FR")
    assert resource.attributes.type_of == 4
    assert resource.attributes.state == 1


# ---------------------------------------------------------------------------
# get_resource — manager resolution
# ---------------------------------------------------------------------------


def test_get_resource_resolves_both_managers_via_fallback_fetch():
    # Manager 456's own response has a mainManager relationship pointing to
    # "999", which is NOT in the canned responses: any recursive resolution
    # would KeyError. Resolution must be exactly one level deep.
    client = make_client(
        {
            "/resources/123": {
                "data": _resource_item(
                    "123", {"mainManager": _rel("456"), "hrManager": _rel("789")}
                )
            },
            "/resources/456": {
                "data": _resource_item("456", {"mainManager": _rel("999")})
            },
            "/resources/456/information": _info_response("456", "manager456@lenstra.fr"),
            "/resources/789": {"data": _resource_item("789")},
            "/resources/789/information": _info_response("789", "manager789@lenstra.fr"),
        }
    )
    resource = asyncio.run(client.get_resource("123"))
    assert resource.main_manager.id == "456"
    assert resource.main_manager.attributes.email1 == "manager456@lenstra.fr"
    assert resource.hr_manager.id == "789"
    assert resource.hr_manager.attributes.email1 == "manager789@lenstra.fr"
    endpoints = [c[1] for c in client.calls]
    assert endpoints == [
        "/resources/123",
        "/resources/456",
        "/resources/456/information",
        "/resources/789",
        "/resources/789/information",
    ]
    # One level deep: the manager's own managers are never resolved
    assert resource.main_manager.main_manager is None
    assert resource.main_manager.hr_manager is None


def test_get_resource_manager_resolved_from_included():
    # Profile comes from included data (no extra GET for that), but email
    # still requires a separate call: /resources/{id} (basic or included)
    # never carries emails, only /resources/{id}/information does.
    client = make_client(
        {
            "/resources/123": {
                "data": _resource_item("123", {"mainManager": _rel("456")}),
                "included": [_resource_item("456")],
            },
            "/resources/456/information": _info_response("456", "manager456@lenstra.fr"),
        }
    )
    resource = asyncio.run(client.get_resource("123"))
    assert resource.main_manager.id == "456"
    assert resource.main_manager.full_name == "First456 Last456"
    assert resource.main_manager.attributes.email1 == "manager456@lenstra.fr"
    endpoints = [c[1] for c in client.calls]
    assert endpoints == ["/resources/123", "/resources/456/information"]


def test_get_resource_without_managers_makes_no_extra_call():
    for relationships in (None, {"mainManager": {"data": None}, "hrManager": {"data": None}}):
        client = make_client({"/resources/123": {"data": _resource_item("123", relationships)}})
        resource = asyncio.run(client.get_resource("123"))
        assert resource.main_manager is None
        assert resource.hr_manager is None
        assert len(client.calls) == 1


def test_get_resource_dangling_manager_404_is_swallowed():
    client = make_client(
        {
            "/resources/123": {
                "data": _resource_item("123", {"mainManager": _rel("999")})
            },
            "/resources/999": BoondManagerAPIError(404, "/resources/999", "not found"),
        }
    )
    resource = asyncio.run(client.get_resource("123"))
    assert resource.id == "123"
    assert resource.main_manager is None


def test_get_resource_manager_fetch_non_404_propagates():
    client = make_client(
        {
            "/resources/123": {
                "data": _resource_item("123", {"mainManager": _rel("456")})
            },
            "/resources/456": BoondManagerAPIError(500, "/resources/456", "boom"),
        }
    )
    with pytest.raises(BoondManagerAPIError) as exc_info:
        asyncio.run(client.get_resource("123"))
    assert exc_info.value.status_code == 500


def test_get_resource_manager_email_fetch_404_is_swallowed():
    # Manager profile resolves fine, but /information 404s (e.g. the
    # sub-resource was never populated): resolution still succeeds, just
    # without an email, rather than failing get_resource() entirely.
    client = make_client(
        {
            "/resources/123": {
                "data": _resource_item("123", {"mainManager": _rel("456")})
            },
            "/resources/456": {"data": _resource_item("456")},
            "/resources/456/information": BoondManagerAPIError(
                404, "/resources/456/information", "not found"
            ),
        }
    )
    resource = asyncio.run(client.get_resource("123"))
    assert resource.main_manager.id == "456"
    assert resource.main_manager.attributes.email1 is None


def test_get_resource_manager_email_fetch_non_404_propagates():
    client = make_client(
        {
            "/resources/123": {
                "data": _resource_item("123", {"mainManager": _rel("456")})
            },
            "/resources/456": {"data": _resource_item("456")},
            "/resources/456/information": BoondManagerAPIError(
                500, "/resources/456/information", "boom"
            ),
        }
    )
    with pytest.raises(BoondManagerAPIError) as exc_info:
        asyncio.run(client.get_resource("123"))
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# search_resources_by_email
# ---------------------------------------------------------------------------


def test_search_resources_by_email_params_and_models():
    client = make_client(
        {
            "/resources": {
                "data": [
                    {
                        "id": "1",
                        "type": "resource",
                        "attributes": {"firstName": "A", "lastName": "One", "email1": "a@x.fr"},
                    },
                    {
                        "id": "2",
                        "type": "resource",
                        "attributes": {"firstName": "B", "lastName": "Two", "email1": "b@x.fr"},
                    },
                ]
            }
        }
    )
    resources = asyncio.run(client.search_resources_by_email("a@x.fr"))
    assert [r.id for r in resources] == ["1", "2"]
    assert client.calls == [
        ("GET", "/resources", {"keywords": "a@x.fr", "keywordsType": "emails"})
    ]


def test_search_resources_by_email_no_match_returns_empty_list():
    client = make_client({"/resources": {"data": []}})
    assert asyncio.run(client.search_resources_by_email("nobody@x.fr")) == []


def test_search_resources_shared_manager_fetched_once():
    client = make_client(
        {
            "/resources": {
                "data": [
                    _resource_item("1", {"mainManager": _rel("77")}),
                    _resource_item("2", {"mainManager": _rel("77")}),
                    _resource_item("3", {"mainManager": _rel("77")}),
                ]
            },
            "/resources/77": {"data": _resource_item("77")},
            "/resources/77/information": _info_response("77", "manager77@lenstra.fr"),
        }
    )
    resources = asyncio.run(client.search_resources_by_email("shared@lenstra.fr"))
    assert [r.main_manager.id for r in resources] == ["77", "77", "77"]
    assert all(r.main_manager.attributes.email1 == "manager77@lenstra.fr" for r in resources)
    # per-call cache dedupes the shared manager: profile and email each fetched once
    assert len([c for c in client.calls if c[1] == "/resources/77"]) == 1
    assert len([c for c in client.calls if c[1] == "/resources/77/information"]) == 1


# ---------------------------------------------------------------------------
# get_resource_type_dictionary
# ---------------------------------------------------------------------------

# Confirmed against a live instance (2026-07-10): "data" is the settings
# object directly, no JSON:API "attributes"/"id"/"type" envelope. Each entry
# carries extra fields (scenario, isEnabled, isExternal, isStructure) that
# the parser ignores.
_TYPES = [
    {"id": 4, "value": "Consultant interne", "isEnabled": True, "isExternal": True},
    {"id": 1, "value": "Consultant externe", "isEnabled": True, "isExternal": True},
]


def test_resource_type_dictionary_parses_real_shape():
    client = make_client(
        {
            "/application/dictionary": {
                "data": {"setting": {"typeOf": {"resource": _TYPES}}}
            }
        }
    )
    mapping = asyncio.run(client.get_resource_type_dictionary())
    assert mapping == {"Consultant interne": 4, "Consultant externe": 1}
    assert mapping.get("Inconnu") is None


def test_resource_type_dictionary_is_cached_per_instance():
    client = make_client(
        {
            "/application/dictionary": {
                "data": {"setting": {"typeOf": {"resource": _TYPES}}}
            }
        }
    )

    async def call_twice():
        first = await client.get_resource_type_dictionary()
        second = await client.get_resource_type_dictionary()
        return first, second

    first, second = asyncio.run(call_twice())
    assert first == second
    assert len(client.calls) == 1  # second call served from the instance cache


def test_resource_type_dictionary_unexpected_shape_raises():
    client = make_client({"/application/dictionary": {"data": {"other": 1}}})
    with pytest.raises(BoondManagerError, match="setting.typeOf.resource"):
        asyncio.run(client.get_resource_type_dictionary())
