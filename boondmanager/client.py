"""BoondManager API client.

API base: https://ui.boondmanager.com/api
Auth: HMAC-SHA256 JWT in the X-Jwt-Client-BoondManager header.

BoondManager uses a non-standard "type" key instead of RFC "typ" in the JWT
header, so we build the token manually rather than using a JWT library.
"""

from __future__ import annotations

import asyncio
import base64
import hashlib
import hmac
import json
import logging
import time
from typing import Any, AsyncIterator

import httpx
import jsonschema
from jsonschema.exceptions import best_match

logger = logging.getLogger(__name__)

from . import spec
from .api import BoondManagerAPI
from .jsonapi import Document, Entity
from .models import (
    AbsencesReport,
    Company,
    CreateAbsencePeriod,
    CurrentUser,
    Positioning,
    Project,
    ProjectSummary,
    Resource,
    TimesReport,
    WorkUnitType,
)
from .timesheets import Timesheet


from .exceptions import (
    BoondManagerAPIError,
    BoondManagerError,
    BoondManagerSilentDropError,
    BoondManagerValidationError,
)

# ---------------------------------------------------------------------------
# Request-body validation (module-private)
# ---------------------------------------------------------------------------


def _format_schema_error(error: jsonschema.ValidationError) -> str:
    # For oneOf/anyOf failures the top-level message dumps entire schemas;
    # descend to the most relevant leaf error instead.
    leaf = error
    while leaf.context:
        leaf = best_match(leaf.context)
    json_path = "$" + "".join(f"[{p!r}]" for p in leaf.absolute_path)
    message = leaf.message
    if len(message) > 400:
        message = message[:400] + "…"
    return f"{json_path}: {message}"


def _validate_request_body(method: str, endpoint: str, body: Any) -> None:
    info = spec.match(method, endpoint)
    if info is None:
        logger.warning(
            "%s %s is not in the vendored API spec; body not validated",
            method, endpoint,
        )
        return
    schema_name = info.get("body_schema")
    if not schema_name:
        return
    schema = spec.schema(schema_name)
    if schema is None:
        # Referenced by the RAML but not published (see scripts/fetch_spec.py)
        logger.debug("schema %s is not vendored; body not validated", schema_name)
        return
    validator = jsonschema.Draft4Validator(schema)
    errors = sorted(validator.iter_errors(body), key=lambda e: list(e.absolute_path))
    if errors:
        raise BoondManagerValidationError(
            endpoint, schema_name, [_format_schema_error(e) for e in errors]
        )


# ---------------------------------------------------------------------------
# JWT helpers (module-private)
# ---------------------------------------------------------------------------


def _b64url(data: bytes) -> bytes:
    return base64.urlsafe_b64encode(data).rstrip(b"=")


def _build_jwt(client_token: str, client_key: str | bytes, user_token: str | None) -> str:
    header = json.dumps({"alg": "HS256", "type": "JWT"}, separators=(",", ":")).encode()
    payload = json.dumps(
        {
            "userToken": user_token,
            "clientToken": client_token,
            "time": int(time.time()),
            "mode": "normal",
        },
        separators=(",", ":"),
    ).encode()
    signing_input = _b64url(header) + b"." + _b64url(payload)
    key = client_key.encode() if isinstance(client_key, str) else client_key
    sig = hmac.new(key, signing_input, hashlib.sha256).digest()
    return (signing_input + b"." + _b64url(sig)).decode()


# ---------------------------------------------------------------------------
# Client
# ---------------------------------------------------------------------------


class BoondManagerClient:
    """Async HTTP client for the BoondManager API.

    Usage as a context manager::

        async with BoondManagerClient(...) as client:
            user = await client.get_current_user()

    Or manage the lifecycle manually and call ``await client.aclose()``
    when done.

    Two layers are exposed:

    - curated helpers on the client itself (``get_times_report``,
      ``update_times_report``, ...) returning pydantic models;
    - the full generated API surface on ``client.api`` (one method per
      endpoint of the public spec) returning raw JSON:API dicts.

    All request bodies are validated against BoondManager's own JSON schemas
    before sending (see BoondManagerValidationError).
    """

    def __init__(
        self,
        client_token: str,
        client_key: str,
        user_token: str | None = None,
        base_url: str = "https://ui.boondmanager.com/api",
        semaphore: asyncio.Semaphore | None = None,
    ) -> None:
        self._client_token = client_token
        self._client_key = client_key
        self._user_token = user_token
        self._base_url = base_url.rstrip("/")
        self._http = httpx.AsyncClient(timeout=30.0)
        self._semaphore = semaphore
        self._resource_type_dict: dict[str, int] | None = None
        self.api = BoondManagerAPI(self)

    async def aclose(self) -> None:
        await self._http.aclose()

    async def __aenter__(self) -> BoondManagerClient:
        return self

    async def __aexit__(self, *_: Any) -> None:
        await self.aclose()

    # ------------------------------------------------------------------
    # Internal HTTP
    # ------------------------------------------------------------------

    def _auth_headers(self) -> dict[str, str]:
        return {
            "X-Jwt-Client-BoondManager": _build_jwt(
                self._client_token, self._client_key, self._user_token
            ),
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    async def request(
        self,
        method: str,
        endpoint: str,
        *,
        validate: bool = True,
        **kwargs: Any,
    ) -> dict:
        """Send a request; validate any JSON body against the vendored spec first.

        ``validate=False`` skips the schema check (escape hatch for payloads
        the published spec does not describe correctly).
        """
        if validate and kwargs.get("json") is not None:
            _validate_request_body(method, endpoint, kwargs["json"])
        url = f"{self._base_url}{endpoint}"

        async def _do() -> dict:
            try:
                resp = await self._http.request(
                    method, url, headers=self._auth_headers(), **kwargs
                )
                resp.raise_for_status()
                return resp.json() if resp.content else {}
            except httpx.HTTPStatusError as exc:
                try:
                    detail = json.dumps(exc.response.json())
                except Exception:
                    detail = exc.response.text
                raise BoondManagerAPIError(
                    exc.response.status_code, endpoint, detail
                ) from exc
            except httpx.HTTPError as exc:
                raise BoondManagerError(
                    f"Request failed for {endpoint}: {exc}"
                ) from exc

        if self._semaphore:
            async with self._semaphore:
                return await _do()
        return await _do()

    # Backwards-compatible alias for pre-refactor callers.
    _request = request

    @staticmethod
    def _item(response: dict) -> dict:
        data = response.get("data")
        if not isinstance(data, dict):
            raise BoondManagerError(
                f"expected a single resource object in response, got {type(data).__name__!r}"
            )
        return data

    @staticmethod
    def _list(response: dict) -> list[dict]:
        data = response.get("data")
        if data is None:
            return []
        if isinstance(data, dict):
            return [data]
        return data

    async def paginate(
        self,
        method: str,
        endpoint: str,
        *,
        params: dict | None = None,
        page_size: int = 30,
        validate: bool = True,
    ) -> AsyncIterator[Document]:
        """Async generator that yields one Document per page.

        Increments ``page`` automatically; stops when a page is empty or
        returns fewer items than ``page_size``.

        Usage::

            async for page in client.paginate("GET", "/resources"):
                for entity in page:
                    process(entity["lastName"])
        """
        page = 1
        while True:
            p = {**(params or {}), "page": page, "maxResults": page_size}
            doc = Document(await self.request(method, endpoint, params=p, validate=validate))
            items = doc.many
            if not items:
                break
            yield doc
            if len(items) < page_size:
                break
            page += 1

    # ------------------------------------------------------------------
    # Application
    # ------------------------------------------------------------------

    async def get_current_user(self) -> CurrentUser:
        """GET /application/current-user

        Returns the authenticated user. ``user.id`` is their BoondManager
        resource ID and works for all account types, including admins who
        are not listed in the ``/resources`` endpoint.
        """
        resp = await self.request("GET", "/application/current-user")
        return CurrentUser.model_validate(self._item(resp))

    async def get_dictionary(self) -> dict:
        """GET /application/dictionary — work unit types, states, etc."""
        return await self.request("GET", "/application/dictionary")

    async def get_resource_type_dictionary(self) -> dict[str, int]:
        """Resource-type labels -> ids (``setting.typeOf.resource``).

        Fetched once per client instance via ``get_dictionary()`` and cached
        for the instance's lifetime (no TTL). Missing labels are a plain
        dict ``.get()`` miss — validating the customer's dictionary
        configuration is the caller's business.
        """
        if self._resource_type_dict is None:
            self._resource_type_dict = self._parse_resource_types(
                await self.get_dictionary()
            )
        return self._resource_type_dict

    @staticmethod
    def _parse_resource_types(raw: dict) -> dict[str, int]:
        # Confirmed against a live instance (2026-07-10): "data" is the
        # settings object directly, no JSON:API "attributes" wrapper.
        data = raw.get("data")
        entries = None
        if isinstance(data, dict):
            entries = ((data.get("setting") or {}).get("typeOf") or {}).get("resource")
        if not isinstance(entries, list):
            raise BoondManagerError(
                "unexpected /application/dictionary response shape: "
                "data.setting.typeOf.resource not found"
            )
        return {
            str(e["value"]): int(e["id"])
            for e in entries
            if isinstance(e, dict) and "id" in e and "value" in e
        }

    # ------------------------------------------------------------------
    # Resources
    # ------------------------------------------------------------------

    _MANAGER_FIELDS = (("mainManager", "main_manager"), ("hrManager", "hr_manager"))
    _EMAIL_FIELDS = ("email1", "email2", "email3")

    async def _resource_with_managers(
        self, item: dict, doc: Document, cache: dict[str, Resource | None]
    ) -> Resource:
        """Validate a resource item and resolve its manager relationships.

        Resolution is exactly one level deep: managers fetched here are
        validated directly, never passed back through this helper, so a
        manager's own ``main_manager``/``hr_manager`` are always None.
        ``cache`` deduplicates manager resolution (profile + email) within
        one caller (id -> Resource, or None for a dangling 404 reference).
        """
        resource = Resource.model_validate(item)
        for rel_name, field in self._MANAGER_FIELDS:
            refs = Entity(item).rel(rel_name)
            manager_id = str(refs[0].get("id", "")) if refs else ""
            if not manager_id:
                continue
            if manager_id not in cache:
                cache[manager_id] = await self._resolve_manager(manager_id, doc, resource.id, rel_name)
            setattr(resource.attributes, field, cache[manager_id])
        return resource

    async def _resolve_manager(
        self, manager_id: str, doc: Document, resource_id: str, rel_name: str
    ) -> Resource | None:
        included = doc.find("resource", manager_id)
        if included is not None:
            manager = Resource.model_validate(included.raw)
        else:
            try:
                resp = await self.request("GET", f"/resources/{manager_id}")
                manager = Resource.model_validate(self._item(resp))
            except BoondManagerAPIError as exc:
                if exc.status_code != 404:
                    raise
                logger.warning(
                    "resource %s has dangling %s reference to resource %s (404)",
                    resource_id, rel_name, manager_id,
                )
                return None
        await self._fill_email(manager)
        return manager

    async def _fill_email(self, resource: Resource) -> None:
        """GET /resources/{id}/information — the basic resource payload never
        carries email1/2/3, they live on this sub-resource instead."""
        try:
            resp = await self.request("GET", f"/resources/{resource.id}/information")
        except BoondManagerAPIError as exc:
            if exc.status_code != 404:
                raise
            logger.warning(
                "could not fetch /resources/%s/information for email (404)", resource.id
            )
            return
        attrs = self._item(resp).get("attributes") or {}
        for field in self._EMAIL_FIELDS:
            value = attrs.get(field)
            if value:
                setattr(resource.attributes, field, value)

    async def get_resource(self, resource_id: str) -> Resource:
        """GET /resources/{id}

        ``mainManager``/``hrManager`` relationships are always resolved to
        full ``Resource`` objects, including their email (via one extra GET
        to ``/resources/{id}/information``, since the basic payload never
        carries emails), on top of the profile itself (from the response's
        ``included`` data when present, otherwise one extra GET). A dangling
        manager reference (404) is logged and resolves to None.
        """
        resp = await self.request("GET", f"/resources/{resource_id}")
        return await self._resource_with_managers(self._item(resp), Document(resp), {})

    async def search_resources_by_email(self, email: str) -> list[Resource]:
        """GET /resources?keywords=<email>&keywordsType=emails

        Each returned resource gets the same manager resolution as
        ``get_resource``, so N results can cost up to 4N extra calls
        (managers shared between results are resolved once).
        """
        resp = await self.request(
            "GET",
            "/resources",
            params={"keywords": email, "keywordsType": "emails"},
        )
        doc = Document(resp)
        cache: dict[str, Resource | None] = {}
        return [
            await self._resource_with_managers(r, doc, cache)
            for r in self._list(resp)
        ]

    # ------------------------------------------------------------------
    # Positionings, projects, companies
    # ------------------------------------------------------------------

    async def get_resource_positionings(self, resource_id: str) -> list[Positioning]:
        """GET /resources/{id}/positionings — the resource's staffing assignments.

        A positioning has no direct relationship to a project (it relates to
        an opportunity instead); use get_resource_projects() to get a
        resource's projects.
        """
        doc = await self.api.resources.positionings(resource_id)
        return [
            Positioning(
                id=e.id,
                start_date=e.get("startDate"),
                end_date=e.get("endDate"),
            )
            for e in doc.many
        ]

    async def get_resource_projects(self, resource_id: str) -> list[ProjectSummary]:
        """GET /resources/{id}/projects — the resource's project assignments.

        Use ``reference`` as the display name: BoondManager does not
        populate ``title`` on this endpoint.
        """
        doc = await self.api.resources.projects(resource_id)
        return [
            ProjectSummary(
                id=e.id,
                title=e.get("title"),
                reference=e.get("reference"),
                state=e.get("state"),
            )
            for e in doc.many
        ]

    async def get_project(self, project_id: str) -> Project:
        """GET /projects/{id}

        The ``company`` relationship is resolved to a ``Company`` (from
        ``included`` data when present, otherwise one extra GET). Projects
        without a linked company return ``company=None``; so does a dangling
        company reference (404, logged).
        """
        doc = await self.api.projects.get(project_id)
        entity = doc.one
        company: Company | None = None
        refs = entity.rel("company")
        company_id = str(refs[0].get("id", "")) if refs else ""
        if company_id:
            included = doc.find("company", company_id)
            if included is not None:
                company = Company(id=included.id, name=included.get("name") or "")
            else:
                try:
                    company = await self.get_company(company_id)
                except BoondManagerAPIError as exc:
                    if exc.status_code != 404:
                        raise
                    logger.warning(
                        "project %s has dangling company reference to %s (404)",
                        entity.id, company_id,
                    )
        return Project(
            id=entity.id,
            title=entity.get("title"),
            reference=entity.get("reference"),
            state=entity.get("state"),
            start_date=entity.get("startDate"),
            end_date=entity.get("endDate"),
            company=company,
        )

    async def get_company(self, company_id: str) -> Company:
        """GET /companies/{id}"""
        doc = await self.api.companies.get(company_id)
        return Company(id=doc.one.id, name=doc.one.get("name") or "")

    # ------------------------------------------------------------------
    # Times reports
    # ------------------------------------------------------------------

    async def get_resource_times_reports(self, resource_id: str) -> list[TimesReport]:
        """GET /resources/{id}/times-reports

        Returns lightweight summary objects (no time entries). Call
        ``get_times_report(report.id)`` to fetch the full detail.
        """
        resp = await self.request("GET", f"/resources/{resource_id}/times-reports")
        return [TimesReport.model_validate(r) for r in self._list(resp)]

    async def get_times_report(self, report_id: str) -> TimesReport:
        """GET /times-reports/{id} — full report including all time entries."""
        resp = await self.request("GET", f"/times-reports/{report_id}")
        return TimesReport.model_validate(self._item(resp))

    async def create_times_report(self, resource_id: str, term: str) -> TimesReport:
        """POST /times-reports — create an empty timesheet for the given month.

        ``term`` must be in ``YYYY-MM`` format.  Returns the newly created report
        (typically with state ``savedAndNoValidation`` and empty time lists).
        """
        body = {
            "data": {
                "type": "timesreport",
                "attributes": {"term": term},
                "relationships": {
                    "resource": {"data": {"id": str(resource_id), "type": "resource"}}
                },
            }
        }
        resp = await self.request("POST", "/times-reports", json=body)
        return TimesReport.model_validate(self._item(resp))

    async def get_times_report_with_included(
        self, report_id: str
    ) -> tuple[TimesReport, list[dict]]:
        """GET /times-reports/{id} — returns (report, included) where included
        contains the full JSON:API included array (projects, deliveries, resources…)."""
        resp = await self.request("GET", f"/times-reports/{report_id}")
        report = TimesReport.model_validate(self._item(resp))
        return report, resp.get("included", [])

    async def fetch_timesheet(self, report_id: str) -> Timesheet:
        """High-level editable timesheet grid (see boondmanager.timesheets).

        ::

            ts = await client.fetch_timesheet("1652")
            ts.row(project="23").set("2026-06-30", 0.5)
            await ts.save()
        """
        return await Timesheet.fetch(self, report_id)

    async def update_times_report(self, report: TimesReport) -> TimesReport:
        """PUT /times-reports/{id} — update regular and exceptional time entries.

        RAML: only regularTimes and exceptionalTimes are accepted; absencesTimes is
        managed separately via POST /absences-reports.
        """
        attrs = report.attributes
        body = {
            "data": {
                "type": "timesreport",
                "id": str(report.id),
                "attributes": {
                    "regularTimes": [
                        e.to_api_regular() for e in attrs.regular_times if e.duration > 0
                    ],
                    "exceptionalTimes": [
                        e.to_api_exceptional()
                        for e in attrs.exceptional_times
                        if e.duration > 0
                    ],
                },
            }
        }
        logger.info(
            "PUT /times-reports/%s body: %s",
            report.id,
            json.dumps(body, ensure_ascii=False),
        )
        resp = await self.request("PUT", f"/times-reports/{report.id}", json=body)
        logger.info("PUT /times-reports/%s response: %s", report.id, json.dumps(resp, ensure_ascii=False))
        updated = TimesReport.model_validate(self._item(resp))

        # The API can accept a schema-valid entry and still discard it
        # (nonexistent row/delivery id, closed period, ...) while returning
        # 200 — surface that as an error instead of pretending it saved.
        sent = body["data"]["attributes"]
        for kind, persisted in (
            ("regularTimes", updated.attributes.regular_times),
            ("exceptionalTimes", updated.attributes.exceptional_times),
        ):
            if len(persisted) < len(sent[kind]):
                raise BoondManagerSilentDropError(
                    f"/times-reports/{report.id}",
                    f"sent {len(sent[kind])} {kind} but server persisted "
                    f"{len(persisted)}",
                )
        return updated

    # ------------------------------------------------------------------
    # Absences reports
    # ------------------------------------------------------------------

    async def get_resource_absences_reports(self, resource_id: str) -> list[AbsencesReport]:
        """GET /resources/{id}/absences-reports"""
        resp = await self.request("GET", f"/resources/{resource_id}/absences-reports")
        return [AbsencesReport.model_validate(r) for r in self._list(resp)]

    async def get_absence_types(self, resource_id: str) -> list[WorkUnitType]:
        """Absence work-unit types the resource may request, sorted by name.

        Authoritative source: the resource's ``workUnitTypesAllowed`` in the
        included section of GET /absences-reports/default. Do not hardcode
        these references — their meaning is per-customer configuration.
        """
        doc = await self.api.absences_reports.default(
            params={"resource": resource_id}
        )
        for entity in doc.included("resource"):
            types = [
                WorkUnitType.model_validate(w)
                for w in entity.get("workUnitTypesAllowed") or []
                if w.get("activityType") == "absence"
            ]
            if types:
                return sorted(types, key=lambda w: w.name)
        return []

    async def count_working_days(self, start_date: str, end_date: str) -> float:
        """Open days in [start_date, end_date], excluding weekends and bank
        holidays (GET /application/weekendAndBankHolidays)."""
        doc = await self.api.application.weekend_and_bank_holidays(
            params={"startDate": start_date, "endDate": end_date}
        )
        return float(
            sum(
                1
                for d in doc.raw.get("data", [])
                if not d.get("weekend") and not d.get("bankHoliday")
            )
        )

    async def create_absences_report(
        self,
        resource_id: str,
        periods: list[CreateAbsencePeriod],
        comments: str = "",
    ) -> AbsencesReport:
        """POST /absences-reports

        Example::

            from boondmanager import BoondManagerClient, CreateAbsencePeriod

            await client.create_absences_report(
                resource_id="42",
                periods=[
                    CreateAbsencePeriod(
                        start_date="2026-08-01",
                        end_date="2026-08-05",
                        duration=5.0,
                        title="Congés payés",
                        work_unit_type_reference=2,
                    )
                ],
                comments="Vacances d'été",
            )
        """
        body: dict = {
            "data": {
                "type": "absencesreport",
                "attributes": {
                    "absencesPeriods": [p.to_api() for p in periods],
                },
                "relationships": {
                    "resource": {"data": {"id": str(resource_id), "type": "resource"}}
                },
            }
        }
        if comments:
            body["data"]["attributes"]["informationComments"] = comments
        resp = await self.request("POST", "/absences-reports", json=body)
        return AbsencesReport.model_validate(self._item(resp))
