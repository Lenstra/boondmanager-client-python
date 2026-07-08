"""Generated BoondManager API surface — DO NOT EDIT.

Regenerate with scripts/fetch_spec.py + scripts/generate_api.py.

One namespace per API resource, one method per endpoint+verb, covering the
whole BoondManager API v1.0 (844 endpoints). Every call goes through
BoondManagerClient.request(), which validates request bodies against
BoondManager's own JSON schemas before sending (the API silently drops
non-conforming payload items while returning 200).

Methods return a jsonapi.Document (dict-compatible; .one / .many / .included()
/ .related() for navigation). ``params`` are query-string parameters (search
keywords, period, pagination, ...) — see https://doc.boondmanager.com/api-externe/.

ENDPOINT_INDEX maps ("VERB", "/path/{id}") to ("group", "method") for
programmatic discovery.
"""

# fmt: off

from __future__ import annotations

from typing import Any

from .jsonapi import Document


class AbsencesAPI:
    """Endpoints under /absences."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /absences
        
        Search absences
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/absences.csv?keywords=TPS1*
        
        Query params:
          keywords (string): If `keywords = COMP**ID1**` then absences
          resourceTypes (integer, repeatable): List of resource types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.resource)
          excludeResourceTypes (integer, repeatable): List of resource types `id` not filtered (described by /api/rest/application/dictionary/setting.typeOf.resource)
          period (string): * `inProgress` : Absences between `startDate` and `endDate` are filtered
          startDate (string): Start date
          endDate (string): End date
          encoding (string): If the output format is **csv** then **encoding** filter should be one of
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: resource.lastName
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/absences", params=params, validate=validate))



class AbsencesReportsAPI:
    """Endpoints under /absences-reports."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /absences-reports
        
        Search request absences
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/absences-reports.csv?keywords=ABS1*
        
        Query params:
          startMonth (string, REQUIRED): Start month
          endMonth (string, REQUIRED): End month
          keywords (string): If `keywords = ABS**ID1** COMP**ID2**` then absences
          resourceTypes (integer, repeatable): List of resource types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.resource)
          validationStates (string, repeatable, one of: waitingForValidation | validated | rejected)
          encoding (string): If the output format is **csv** then **encoding** filter should be one of
          extractType (string, default notDetailed): If the output format is **csv** then **extractType** filter should be one of
          exportToDownloadCenter (string): Export requests of absences formatted file and/or documents to the download center
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: creationDate | state | resource.lastName
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/absences-reports", params=params, validate=validate))

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /absences-reports
        
        Create a request of absences
        
        Request body schema: absencesReportsBody-post
        """
        return Document(await self._client.request("POST", "/absences-reports", json=body, params=params, validate=validate))

    async def default(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /absences-reports/default
        
        Get empty request of absences default basic data
        
        Query params:
          resource (integer, REQUIRED): Resource's `id` on which request of absences depends
          agency (integer): Agency's `id` on which request of absences depends
        """
        return Document(await self._client.request("GET", "/absences-reports/default", params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /absences-reports/{id}
        
        Delete the request of absences
        """
        return Document(await self._client.request("DELETE", f"/absences-reports/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /absences-reports/{id}
        
        Get request of absences basic data
        """
        return Document(await self._client.request("GET", f"/absences-reports/{id}", params=params, validate=validate))

    async def update(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /absences-reports/{id}
        
        Update basic data related to a request of absences
        
        Request body schema: absencesReportsBody-put
        """
        return Document(await self._client.request("PUT", f"/absences-reports/{id}", json=body, params=params, validate=validate))

    async def download(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /absences-reports/{id}/download
        
        Get request of absences formatted file content
        
        Query params:
          language (string, one of: fr | en | es): Language used for the file content
        """
        return Document(await self._client.request("GET", f"/absences-reports/{id}/download", params=params, validate=validate))

    async def reject(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /absences-reports/{id}/reject
        
        Reject a request of absence
        
        Request body schema: absencesReportsRejectBody-post
        """
        return Document(await self._client.request("POST", f"/absences-reports/{id}/reject", json=body, params=params, validate=validate))

    async def rights(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /absences-reports/{id}/rights
        
        Get requets of absences rights
        
        Query params:
          resource (integer): Resource's `id` on which request of absences depends
          agency (integer): Agency's `id` on which request of absences depends
        """
        return Document(await self._client.request("GET", f"/absences-reports/{id}/rights", params=params, validate=validate))

    async def unvalidate(self, id, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /absences-reports/{id}/unvalidate
        
        Unvalidate a request of absence
        
        Query params:
          expectedValidator (integer, REQUIRED): Resource's `id` on which request of absence depends
        """
        return Document(await self._client.request("POST", f"/absences-reports/{id}/unvalidate", json=body, params=params, validate=validate))

    async def validate(self, id, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /absences-reports/{id}/validate
        
        Validate a request of absence
        
        Query params:
          expectedValidator (integer, REQUIRED): Resource's `id` on which request of absence depends
        """
        return Document(await self._client.request("POST", f"/absences-reports/{id}/validate", json=body, params=params, validate=validate))



class AccountsAPI:
    """Endpoints under /accounts."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /accounts
        
        Search accounts
        
        Query params:
          keywords (string): If `keywords = USER**ID1** COMP**ID2** ROLE**ID3**` then accounts
          userSubscriptions (string, repeatable): * `active` : Active accounts are filtered
          resourceTypes (integer, repeatable): List of resource types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.resource)
          roles (integer, repeatable): Results whom belong to role's unique identifier are filtered
          period (string): * `created` : Resources created between `startDate` and `endDate` are filtered
          periodDynamic (string): * `today` : Resources filtered according to the grid for today's period
          periodDynamicParameters (string): Filter parameters of dynamic period. Used when periodDynamic is "lastCustomPeriod" or "nextCustomPeriod"
          startDate (string): Start date
          endDate (string): End date
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: lastName | login | role.name | typeOf | subscription | mainManager.lastName | pole.name | agency.name
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/accounts", params=params, validate=validate))

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /accounts
        
        Create an account
        
        Request body schema: accountsBody-post
        """
        return Document(await self._client.request("POST", "/accounts", json=body, params=params, validate=validate))

    async def default(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /accounts/default
        
        Get empty account's default basic data
        
        Query params:
          resource (integer): Resource's `id` on which account depends.
        """
        return Document(await self._client.request("GET", "/accounts/default", params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /accounts/{id}
        
        Delete the account
        """
        return Document(await self._client.request("DELETE", f"/accounts/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /accounts/{id}
        
        Get account's basic data
        """
        return Document(await self._client.request("GET", f"/accounts/{id}", params=params, validate=validate))

    async def update(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /accounts/{id}
        
        Update basic data related to an account
        
        Request body schema: accountsBody-put
        """
        return Document(await self._client.request("PUT", f"/accounts/{id}", json=body, params=params, validate=validate))

    async def connect(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /accounts/{id}/connect
        
        Connect to this account
        """
        return Document(await self._client.request("GET", f"/accounts/{id}/connect", params=params, validate=validate))



class ActionsAPI:
    """Endpoints under /actions."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /actions
        
        Search actions entity (Resource, Candidate, Project, Opportunity, Order, Invoice, Contact)
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/actions.csv?keywords=COMP100*
        
        Query params:
          keywords (string): If `keywords = COMP**ID1** CAND**ID2** PRJ**ID3** CCON**ID4** CSOC**ID5** AO**ID6** BDC**ID7** FACT**ID8**` then
          actionTypes (integer, repeatable): List of action types `id`, related to the action's entity (Resource, Candidate, Project, Opportunity, Order, Bill, Contact), to filter (described by /api/rest/application/dictionary/setting.action)
          states (string, repeatable): List of entity states `id`, related to the action's entity (Resource, Candidate, Project, Opportunity, Order, Bill, Contact), to filter (described by /api/rest/dictionary/setting.state)
          origins (string, repeatable): List of contacts/companies/opportunities origins `id` to filter (described by /api/rest/application/dictionary/setting.origin)
          period (string): * `started` : Actions started between `startDate` and `endDate` are filtered
          periodDynamic (string): * `today` : Actions filtered according to the grid for today's period
          periodDynamicParameters (string): Filter parameters of dynamic period. Used when periodDynamic is "lastCustomPeriod" or "nextCustomPeriod"
          startDate (string): Start date
          endDate (string): End date
          flags (integer, repeatable): Entities (Resource, Candidate, Project, Opportunity, Order, Invoice, Contact, Positioning, Action) attached to this flag whom flag's unique identifier = integer are filtered
          onlyVisible (boolean, default True): The user has to have the global right `showGroupe` set to `true` or call this api into mode `god`.
          returnRelatedActions (boolean, default False): Return related parent and child/sibbling actions
          keywordsType (string, default ): * `` : Actions are filtered following `keywords` found into their resource's name, candidate's name, contact's name, company's name, project's reference, order's number
          encoding (string): If the output format is **csv** then **encoding** filter should be one of
          columns (string, repeatable): List of columns
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: startDate | typeOf | mainManager.lastName | dependsOn.email1 | dependsOn.lastName | dependsOn.reference | dependsOn.name | dependsOn.title | dependsOn.id | dependsOn.number
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/actions", params=params, validate=validate))

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /actions
        
        Create an action
        
        Query params:
          positioning (integer): Positioning's `id` to create `Client Presentation` slaves on opportunity, contact and resource/candidate
          delivery (integer): Delivery's `id` to create `Monitoring Delivery` slaves on project, contact and resource
        
        Request body schema: actionsBody-post
        """
        return Document(await self._client.request("POST", "/actions", json=body, params=params, validate=validate))

    async def default(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /actions/default
        
        Get empty action's default basic data
        
        Query params:
          resource (integer): Resource's `id` on which action depends
          candidate (integer): Candidate's `id` on which action depends
          opportunity (integer): Opportunity's `id` on which action depends
          project (integer): Project's `id` on which action depends
          order (integer): Order's `id` on which action depends
          invoice (integer): Invoice's `id` on which action depends
          contact (integer): Contact's `id` on which action depends
          company (integer): Company's `id` on which action depends
          positioning (integer): Positioning's `id` to create `Client Presentation` slaves on opportunity, contact and resource/candidate
          delivery (integer): Delivery's `id` to create `Monitoring Delivery` slaves on project, contact and resource
        """
        return Document(await self._client.request("GET", "/actions/default", params=params, validate=validate))

    async def templates(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /actions/templates
        
        Search templates
        
        Query params:
          actionTypes (string, repeatable): List of action types `id`, related to the action's entity (Resource, Candidate, Project, Opportunity, Order, Bill, Contact), to filter (described by /api/rest/application/dictionary/setting.action) or "notUsed" for global templates
          keywords (string): Search action templates on title
          dependsOn (integer): The id of the entity that the action is created for.
          dependsOnType (string, one of: candidate | resource | contact | company | project | opportunity | invoice | order): The type of the entity that the action is created for.
          sort (string, repeatable): Order by a given column: title
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/actions/templates", params=params, validate=validate))

    async def post_templates(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /actions/templates
        
        Create a template
        
        Request body schema: actionsTemplatesBody-post
        """
        return Document(await self._client.request("POST", "/actions/templates", json=body, params=params, validate=validate))

    async def delete_templates_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /actions/templates/{id}
        
        Delete the template
        """
        return Document(await self._client.request("DELETE", f"/actions/templates/{id}", params=params, validate=validate))

    async def templates_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /actions/templates/{id}
        
        Get template's data
        """
        return Document(await self._client.request("GET", f"/actions/templates/{id}", params=params, validate=validate))

    async def update_templates_by_id(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /actions/templates/{id}
        
        Update data related to a template
        
        Request body schema: actionsTemplatesBody-put
        """
        return Document(await self._client.request("PUT", f"/actions/templates/{id}", json=body, params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /actions/{id}
        
        Delete the action
        """
        return Document(await self._client.request("DELETE", f"/actions/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /actions/{id}
        
        Get action's basic data
        """
        return Document(await self._client.request("GET", f"/actions/{id}", params=params, validate=validate))

    async def update(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /actions/{id}
        
        Update basic data related to an action
        
        Query params:
          positioning (integer): Positioning's `id` to create `Client Presentation` slaves on opportunity, contact and resource/candidate
          delivery (integer): Delivery's `id` to create `Monitoring Delivery` slaves on project, contact and resource
        
        Request body schema: actionsBody-put
        """
        return Document(await self._client.request("PUT", f"/actions/{id}", json=body, params=params, validate=validate))

    async def attached_flags(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /actions/{id}/attached-flags
        
        Get action's attached flags
        """
        return Document(await self._client.request("GET", f"/actions/{id}/attached-flags", params=params, validate=validate))

    async def rights(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /actions/{id}/rights
        
        Get action's rights
        
        Query params:
          resource (integer): Resource's `id` on which action depends
          candidate (integer): Candidate's `id` on which action depends
          opportunity (integer): Opportunity's `id` on which action depends
          project (integer): Project's `id` on which action depends
          order (integer): Order's `id` on which action depends
          invoice (integer): Invoice's `id` on which action depends
          contact (integer): Contact's `id` on which action depends
          company (integer): Company's `id` on which action depends
          positioning (integer): Positioning's `id` to create `Client Presentation` slaves on opportunity, contact and resource/candidate
          delivery (integer): Delivery's `id` to create `Monitoring Delivery` slaves on project, contact and resource
        """
        return Document(await self._client.request("GET", f"/actions/{id}/rights", params=params, validate=validate))



class AdministratorAPI:
    """Endpoints under /administrator."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /administrator
        
        Get customer's administrator basic data
        """
        return Document(await self._client.request("GET", "/administrator", params=params, validate=validate))

    async def delete_logo(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /administrator/logo
        
        Delete the logo
        """
        return Document(await self._client.request("DELETE", "/administrator/logo", params=params, validate=validate))

    async def update_logo(self, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /administrator/logo
        
        Update logo
        """
        return Document(await self._client.request("PUT", "/administrator/logo", json=body, params=params, validate=validate))



class AdvantagesAPI:
    """Endpoints under /advantages."""

    def __init__(self, client) -> None:
        self._client = client

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /advantages
        
        Create an advantage
        
        Request body schema: advantagesBody-post
        """
        return Document(await self._client.request("POST", "/advantages", json=body, params=params, validate=validate))

    async def default(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /advantages/default
        
        Get empty advantage's default basic data
        
        Query params:
          resource (integer, REQUIRED): Resource's `id` on which advantage depends.
          contract (integer): Contract's `id` on which advantage depends. `project` & `delivery` parameter can not be set too.
          project (integer): Project's `id` on which advantage depends. `contract` & `delivery` parameter can not be set too.
          delivery (integer): Delivery's `id` on which advantage depends. `contract` & `project` parameter can not be set too.
        """
        return Document(await self._client.request("GET", "/advantages/default", params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /advantages/{id}
        
        Delete the advantage
        """
        return Document(await self._client.request("DELETE", f"/advantages/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /advantages/{id}
        
        Get advantage's basic data
        """
        return Document(await self._client.request("GET", f"/advantages/{id}", params=params, validate=validate))

    async def update(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /advantages/{id}
        
        Update basic data related to an advantage
        
        Request body schema: advantagesBody-put
        """
        return Document(await self._client.request("PUT", f"/advantages/{id}", json=body, params=params, validate=validate))

    async def rights(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /advantages/{id}/rights
        
        Get advantage's rights
        
        Query params:
          resource (integer): Resource's `id` on which advantage depends. `candidate` parameter can not be set too.
          contract (integer): Contract's `id` on which advantage depends. `project` & `delivery` parameter can not be set too.
          project (integer): Project's `id` on which advantage depends. `contract` & `delivery` parameter can not be set too.
          delivery (integer): Delivery's `id` on which advantage depends. `contract` & `project` parameter can not be set too.
        """
        return Document(await self._client.request("GET", f"/advantages/{id}/rights", params=params, validate=validate))



class AgenciesAPI:
    """Endpoints under /agencies."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /agencies
        
        Search agencies
        """
        return Document(await self._client.request("GET", "/agencies", params=params, validate=validate))

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /agencies
        
        Create an agency
        
        Request body schema: agenciesBody-post
        """
        return Document(await self._client.request("POST", "/agencies", json=body, params=params, validate=validate))

    async def default(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /agencies/default
        
        Get empty agency's default information data
        """
        return Document(await self._client.request("GET", "/agencies/default", params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /agencies/{id}
        
        Delete the agency
        """
        return Document(await self._client.request("DELETE", f"/agencies/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /agencies/{id}
        
        Get agency's basic data
        """
        return Document(await self._client.request("GET", f"/agencies/{id}", params=params, validate=validate))

    async def activity_expenses(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /agencies/{id}/activity-expenses
        
        Get agency's activity & expenses data
        """
        return Document(await self._client.request("GET", f"/agencies/{id}/activity-expenses", params=params, validate=validate))

    async def update_activity_expenses(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /agencies/{id}/activity-expenses
        
        Update activity & expenses data related to an agency
        
        Request body schema: agenciesActivityExpensesBody-put
        """
        return Document(await self._client.request("PUT", f"/agencies/{id}/activity-expenses", json=body, params=params, validate=validate))

    async def delete_activity_expenses_logo(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /agencies/{id}/activity-expenses/logo
        
        Delete the logo
        """
        return Document(await self._client.request("DELETE", f"/agencies/{id}/activity-expenses/logo", params=params, validate=validate))

    async def update_activity_expenses_logo(self, id, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /agencies/{id}/activity-expenses/logo
        
        Update logo
        """
        return Document(await self._client.request("PUT", f"/agencies/{id}/activity-expenses/logo", json=body, params=params, validate=validate))

    async def billing(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /agencies/{id}/billing
        
        Get agency's billing data
        """
        return Document(await self._client.request("GET", f"/agencies/{id}/billing", params=params, validate=validate))

    async def update_billing(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /agencies/{id}/billing
        
        Update billing data related to an agency
        
        Request body schema: agenciesBillingBody-put
        """
        return Document(await self._client.request("PUT", f"/agencies/{id}/billing", json=body, params=params, validate=validate))

    async def delete_billing_logo(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /agencies/{id}/billing/logo
        
        Delete the logo
        """
        return Document(await self._client.request("DELETE", f"/agencies/{id}/billing/logo", params=params, validate=validate))

    async def update_billing_logo(self, id, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /agencies/{id}/billing/logo
        
        Update logo
        """
        return Document(await self._client.request("PUT", f"/agencies/{id}/billing/logo", json=body, params=params, validate=validate))

    async def information(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /agencies/{id}/information
        
        Get agency's information data
        """
        return Document(await self._client.request("GET", f"/agencies/{id}/information", params=params, validate=validate))

    async def update_information(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /agencies/{id}/information
        
        Update information data related to an agency
        
        Request body schema: agenciesInformationBody-put
        """
        return Document(await self._client.request("PUT", f"/agencies/{id}/information", json=body, params=params, validate=validate))

    async def opportunities(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /agencies/{id}/opportunities
        
        Get agency's opportunities data
        """
        return Document(await self._client.request("GET", f"/agencies/{id}/opportunities", params=params, validate=validate))

    async def update_opportunities(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /agencies/{id}/opportunities
        
        Update opportunities data related to an agency
        
        Request body schema: agenciesOpportunitiesBody-put
        """
        return Document(await self._client.request("PUT", f"/agencies/{id}/opportunities", json=body, params=params, validate=validate))

    async def products(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /agencies/{id}/products
        
        Get agency's products data
        """
        return Document(await self._client.request("GET", f"/agencies/{id}/products", params=params, validate=validate))

    async def update_products(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /agencies/{id}/products
        
        Update products data related to an agency
        
        Request body schema: agenciesProductsBody-put
        """
        return Document(await self._client.request("PUT", f"/agencies/{id}/products", json=body, params=params, validate=validate))

    async def projects(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /agencies/{id}/projects
        
        Get agency's projects data
        """
        return Document(await self._client.request("GET", f"/agencies/{id}/projects", params=params, validate=validate))

    async def update_projects(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /agencies/{id}/projects
        
        Update projects data related to an agency
        
        Request body schema: agenciesProjectsBody-put
        """
        return Document(await self._client.request("PUT", f"/agencies/{id}/projects", json=body, params=params, validate=validate))

    async def purchases(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /agencies/{id}/purchases
        
        Get agency's purchases data
        """
        return Document(await self._client.request("GET", f"/agencies/{id}/purchases", params=params, validate=validate))

    async def update_purchases(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /agencies/{id}/purchases
        
        Update purchases data related to an agency
        
        Request body schema: agenciesPurchasesBody-put
        """
        return Document(await self._client.request("PUT", f"/agencies/{id}/purchases", json=body, params=params, validate=validate))

    async def resources(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /agencies/{id}/resources
        
        Get agency's resources data
        """
        return Document(await self._client.request("GET", f"/agencies/{id}/resources", params=params, validate=validate))

    async def update_resources(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /agencies/{id}/resources
        
        Update resources data related to an agency
        
        Request body schema: agenciesResourcesBody-put
        """
        return Document(await self._client.request("PUT", f"/agencies/{id}/resources", json=body, params=params, validate=validate))

    async def rights(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /agencies/{id}/rights
        
        Get agency's rights
        """
        return Document(await self._client.request("GET", f"/agencies/{id}/rights", params=params, validate=validate))

    async def technical_data(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /agencies/{id}/technical-data
        
        Get agency's technical data customization colors (_only available when feature flag `technical-data-customization` is enabled_)
        """
        return Document(await self._client.request("GET", f"/agencies/{id}/technical-data", params=params, validate=validate))

    async def update_technical_data(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /agencies/{id}/technical-data
        
        Update technical data customization colors for an agency (_only available when feature flag `technical-data-customization` is enabled_)
        
        Request body schema: agenciesTechnicalDataBody-put
        """
        return Document(await self._client.request("PUT", f"/agencies/{id}/technical-data", json=body, params=params, validate=validate))



class AlertsAPI:
    """Endpoints under /alerts."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /alerts
        
        Search alerts entity
        """
        return Document(await self._client.request("GET", "/alerts", params=params, validate=validate))

    async def configuration(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /alerts/configuration
        
        Get alerts settings for administrator
        """
        return Document(await self._client.request("GET", "/alerts/configuration", params=params, validate=validate))

    async def update_configuration(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /alerts/configuration
        
        Update administrator alerts settings
        
        Request body schema: alertsConfigurationBody-put
        """
        return Document(await self._client.request("PUT", "/alerts/configuration", json=body, params=params, validate=validate))

    async def values(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /alerts/{id}/values
        
        Get values for alert
        """
        return Document(await self._client.request("GET", f"/alerts/{id}/values", params=params, validate=validate))



class AnalyticsAPI:
    """Endpoints under /analytics."""

    def __init__(self, client) -> None:
        self._client = client

    async def reportings_production_by_manager(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /analytics/reportings/production-by-manager
        
        Search production by manager reporting
        
        Query params:
          startDate (string, REQUIRED): Start date of the reporting period
          endDate (string, REQUIRED): End date of the reporting period
          keywords (string): Filter managers by keywords (name search)
          projectTypes (integer, repeatable): List of non-internal project types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.project)
          period (string, default custom): Period granularity for the reporting
          periodDynamic (string): * `today` : Reporting filtered according to the grid for today's period
          periodDynamicParameters (string): Filter parameters of dynamic period. Used when periodDynamic is "lastCustomPeriod" or "nextCustomPeriod".
          maxResources (integer, default 10): Maximum number of managers to return (max 10)
          onlyTotals (boolean, default False): If true, return only global totals in meta without per-manager indicator rows in data
          threshold (integer): Minimum profitability threshold. Managers below this margin rate are counted in `meta.totals.underThreshold`
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: lastName | marginRateProduction | marginProductionExcludingTax | costProductionExcludingTax | turnoverProductionExcludingTax | updateDate | nbProjects
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/analytics/reportings/production-by-manager", params=params, validate=validate))



class ApplicationAPI:
    """Endpoints under /application."""

    def __init__(self, client) -> None:
        self._client = client

    async def assignments(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /application/assignments
        
        Get the list of assignments availables for updating
        
        Query params:
          module (string): The module concerned by the assignment, it have to be one of attributes inside advancedRights attribute of the current user
        """
        return Document(await self._client.request("GET", "/application/assignments", params=params, validate=validate))

    async def backup_dictionary(self, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /application/backup-dictionary
        
        Backup the specific translations
        """
        return Document(await self._client.request("POST", "/application/backup-dictionary", json=body, params=params, validate=validate))

    async def current_user(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /application/current-user
        
        Get current user's data
        """
        return Document(await self._client.request("GET", "/application/current-user", params=params, validate=validate))

    async def dictionary(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /application/dictionary
        
        Get the specific translations
        
        Query params:
          mergeAllLanguages (boolean, default False): true if you need to get all languages merged
          language (string, one of: fr | en | es): Language
        """
        return Document(await self._client.request("GET", "/application/dictionary", params=params, validate=validate))

    async def update_dictionary(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /application/dictionary
        
        Update the specific translations
        
        Query params:
          language (string, one of: fr | en | es): Language
        
        Request body schema: application-dictionaryBody-put
        """
        return Document(await self._client.request("PUT", "/application/dictionary", json=body, params=params, validate=validate))

    async def download_dictionary(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /application/download-dictionary
        
        Get dictionar's file
        
        Query params:
          language (string, one of: fr | en | es): Language
        """
        return Document(await self._client.request("GET", "/application/download-dictionary", params=params, validate=validate))

    async def dump_database(self, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /application/dump-database
        
        Create a dabatase dump
        """
        return Document(await self._client.request("POST", "/application/dump-database", json=body, params=params, validate=validate))

    async def dynamic_filters(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /application/dynamic-filters
        
        Get cleaned dynamic filters availables for searching
        
        Query params:
          module (string): The module concerned by the search, it have to be one of attributes inside advancedRights attribute of the current user
          period (string): * `dynamicPeriod` : Reporting are returned following the period dynamic filter
          periodDynamic (string): * `today` : Resources filtered according to the grid for today's period
          periodDynamicParameters (string): Filter parameters of dynamic period. Used when periodDynamic is "lastCustomPeriod" or "nextCustomPeriod"
          startDate (string): Start date
          endDate (string): End date
          creationPeriod (string): Used only for advanced reporting won opportunities.
          creationPeriodDynamic (string): Used only for advanced reporting won opportunities.
          creationPeriodDynamicParameters (string): Filter parameters of dynamic period for advanced reporting won opportunities. Used when creationPeriodDynamicParameters is "lastCustomPeriod" or "nextCustomPeriod"
          creationStartDate (string): Creation start date for advanced reporting won opportunities
          creationEndDate (string): Creation end date for advanced reporting won opportunities
          winPeriod (string): Used only for advanced reporting won opportunities.
          winPeriodDynamic (string): Used only for advanced reporting won opportunities.
          winPeriodDynamicParameters (string): Filter parameters of dynamic period for advanced reporting won opportunities. Used when winPeriodDynamicParameters is "lastCustomPeriod" or "nextCustomPeriod"
          winStartDate (string): Win start date for advanced reporting won opportunities
          winEndDate (string): Win end date for advanced reporting won opportunities
        """
        return Document(await self._client.request("GET", "/application/dynamic-filters", params=params, validate=validate))

    async def flags(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /application/flags
        
        Get the list of flags availables for searching or updating
        """
        return Document(await self._client.request("GET", "/application/flags", params=params, validate=validate))

    async def geocities(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /application/geocities
        
        Search for cities by name (autosuggest)
        
        Query params:
          keywords (string, REQUIRED): City name to search for (minimum 3 characters)
        """
        return Document(await self._client.request("GET", "/application/geocities", params=params, validate=validate))

    async def perimeters(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /application/perimeters
        
        Get the list of perimeters availables for searching
        
        Query params:
          module (string): The module concerned by the search, it have to be one of attributes inside advancedRights attribute of the current user
        """
        return Document(await self._client.request("GET", "/application/perimeters", params=params, validate=validate))

    async def read_database(self, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /application/read-database
        
        Read database thanks to a MySQL query
        """
        return Document(await self._client.request("POST", "/application/read-database", json=body, params=params, validate=validate))

    async def update_restore_dictionary(self, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /application/restore-dictionary
        
        Restore the last specific translations backup
        """
        return Document(await self._client.request("PUT", "/application/restore-dictionary", json=body, params=params, validate=validate))

    async def settings(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /application/settings
        
        Get the specific settings
        """
        return Document(await self._client.request("GET", "/application/settings", params=params, validate=validate))

    async def update_settings(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /application/settings
        
        Update the specific settings
        
        Request body schema: application-dictionaryBody-put
        """
        return Document(await self._client.request("PUT", "/application/settings", json=body, params=params, validate=validate))

    async def status(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /application/status
        
        Get status
        """
        return Document(await self._client.request("GET", "/application/status", params=params, validate=validate))

    async def weekend_and_bank_holidays(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /application/weekendAndBankHolidays
        
        Get the types of days between 2 dates
        
        Query params:
          startDate (string, REQUIRED): Start date
          endDate (string, REQUIRED): End date
          calendar (string): Calendar to filter (described by /api/rest/application/dictionary/setting.calendar)
        """
        return Document(await self._client.request("GET", "/application/weekendAndBankHolidays", params=params, validate=validate))



class AppsAPI:
    """Endpoints under /apps."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps
        
        Search installed apps
        """
        return Document(await self._client.request("GET", "/apps", params=params, validate=validate))

    async def absences_accounts_absences_accounts(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/absences-accounts/absences-accounts
        
        Search absences accounts
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/absences.csv?keywords=TPS1*
        
        Query params:
          keywords (string): If `keywords = COMP**ID1**` then absences
          resourceTypes (integer, repeatable): List of resource types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.resource)
          resourceStates (integer, repeatable): List of resource states `id` to filter (described by /api/rest/application/dictionary/setting.state.resource)
          workUnitTypes (string, repeatable): List of entity workunit types `id`, related to the agency's entity, to filter
          startYear (string): Start year
          endYear (string): End year
          encoding (string): If the output format is **csv** then **encoding** filter should be one of
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: resource.lastName | workUnitType.reference | period | agency.name
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/apps/absences-accounts/absences-accounts", params=params, validate=validate))

    async def update_absences_accounts_absences_accounts_by_id(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/absences-accounts/absences-accounts/{id}
        
        Update basic data related to an absences account
        
        Request body schema: appsAbsencesAccountsAbsencesAccountsBody-put
        """
        return Document(await self._client.request("PUT", f"/apps/absences-accounts/absences-accounts/{id}", json=body, params=params, validate=validate))

    async def absences_accounts_import__absences_accounts(self, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /apps/absences-accounts/import/absences-accounts
        
        Import absences accounts
        """
        return Document(await self._client.request("POST", "/apps/absences-accounts/import/absences-accounts", json=body, params=params, validate=validate))

    async def accounting_payroll_companies(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/accounting-payroll/companies
        
        Search companies
        
        Query params:
          keywords (string): Available only if `type` is `boondmanagerCompanies`.
          states (integer, repeatable): List of company states `id` to filter (described by /api/rest/application/dictionary/setting.state.company).
          typeOfCompanies (string, one of: sageCompaniesWithThirdAccount | sageCompaniesWithoutThirdAccount | boondmanagerCompanies, default sageCompaniesWithoutThirdAccount)
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: name | state
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/apps/accounting-payroll/companies", params=params, validate=validate))

    async def update_accounting_payroll_companies_by_id(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/accounting-payroll/companies/{id}
        
        Update company data related to Sage Interface's customer
        
        Request body schema: appsAccountingPayrollCompaniesBody-put
        """
        return Document(await self._client.request("PUT", f"/apps/accounting-payroll/companies/{id}", json=body, params=params, validate=validate))

    async def accounting_payroll_configuration(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/accounting-payroll/configuration
        
        Get app's Sage Interface configuration data
        """
        return Document(await self._client.request("GET", "/apps/accounting-payroll/configuration", params=params, validate=validate))

    async def update_accounting_payroll_configuration(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/accounting-payroll/configuration
        
        Update accounting configuration data related to Sage Interface's customer
        
        Request body schema: appsAccountingPayrollConfigurationBody-put
        """
        return Document(await self._client.request("PUT", "/apps/accounting-payroll/configuration", json=body, params=params, validate=validate))

    async def accounting_payroll_contracts(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/accounting-payroll/contracts
        
        Search contracts
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/apps/accounting-payroll/contracts.csv?keywords=CTR1*
        
        Query params:
          month (string, REQUIRED): month
          keywords (string): If `keywords = CTR**ID1** COMP**ID2**` then contracts
          resourceTypes (integer, repeatable): List of resource types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.resource)
          extractType (string, one of: activitySalaryExpensesAndAdvantages | activity | salaryExpensesAndAdvantages | activityAbsencesAndVariable | variable, default activitySalaryExpensesAndAdvantages)
          encoding (string): If accountingVersion is `sageCoala` then **encoding** filter should be one of
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: typeOf | resource.lastName | timesReports.state | expensesReports.state
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/apps/accounting-payroll/contracts", params=params, validate=validate))

    async def accounting_payroll_expenses_reports(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/accounting-payroll/expenses-reports
        
        Search expenses
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/apps/accounting-payroll/expenses-reports.csv?keywords=EXP1*
        
        Query params:
          startMonth (string, REQUIRED): Start month
          endMonth (string, REQUIRED): End month
          keywords (string): If `keywords = EXP**ID1** COMP**ID2**` then expenses
          validationStates (string, repeatable, one of: waitingForValidation | validated | rejected)
          extractType (string, one of: vatIncludingTax | vatExcludingTax, default vatIncludingTax)
          encoding (string): If accountingVersion is `sageCoala` then **encoding** filter should be one of
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: term | state | resource.lastName
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/apps/accounting-payroll/expenses-reports", params=params, validate=validate))

    async def accounting_payroll_invoices(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/accounting-payroll/invoices
        
        Search companies
        
        Query params:
          keywords (string): Available only if `type` is `boondmanagerCompanies`.
          states (integer, repeatable): List of company states `id` to filter (described by /api/rest/application/dictionary/setting.state.company).
          typeOfCompanies (string, one of: sageCompaniesWithThirdAccount | sageCompaniesWithoutThirdAccount | boondmanagerCompanies, default sageCompaniesWithoutThirdAccount)
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: name | state
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/apps/accounting-payroll/invoices", params=params, validate=validate))

    async def accounting_payroll_payments(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/accounting-payroll/payments
        
        Search payments
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/apps/accounting-payroll/payments.csv?keywords=CTR1*
        
        Query params:
          startMonth (string, REQUIRED): Start month
          endMonth (string, REQUIRED): End month
          keywords (string): If `keywords = ACH**ID1** CCON**ID2** CSOC**ID3** PRJ**ID4** COMP**ID5**` then payments
          paymentStates (integer, repeatable): List of payment states `id` to filter (described by /api/rest/application/dictionary/setting.state.payment)
          extractType (string, one of: vatIncludingTax | vatExcludingTax, default vatIncludingTax)
          extractedElements (boolean): * true : display only already extracted payments
          encoding (string): If accountingVersion is `sageCoala` then **encoding** filter should be one of
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: state | date | purchase.title | project.reference | company.name
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/apps/accounting-payroll/payments", params=params, validate=validate))

    async def accounting_payroll_resources(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/accounting-payroll/resources
        
        Search resources
        
        Query params:
          keywords (string): Available only if `type` is `boondmanagerEmployees`.
          states (integer, repeatable): List of resources states `id` to filter (described by /api/rest/application/dictionary/setting.state.resource).
          typeOfCompanies (string, one of: sageEmployeesWithAccount | sageEmployeesWithoutAccount | boondmanagerEmployees, default sageEmployeesWithoutAccount)
          extractedElements (boolean): * true : display only already extracted resources
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: lastName | state
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/apps/accounting-payroll/resources", params=params, validate=validate))

    async def update_accounting_payroll_resources_by_id(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/accounting-payroll/resources/{id}
        
        Update resource data related to Sage Interface's customer
        
        Request body schema: appsAccountingPayrollResourcesBody-put
        """
        return Document(await self._client.request("PUT", f"/apps/accounting-payroll/resources/{id}", json=body, params=params, validate=validate))

    async def advanced_candidates_candidates(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/advanced-candidates/candidates
        
        Search candidates
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/candidates.csv?keywords=CAND100*
        
        Query params:
          keywords (string): If `keywords = CAND**ID1** CAND**ID2**` then candidates
          keywordsType (string, default resumeTd): * `resumeTd` : Candidates are filtered following `keywords` found into their resumes and technical document
          returnMoreData (string, repeatable): Returns the following attributes or relationships, if specified and user is allowed to
          contractTypes (integer, repeatable): List of contract types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.contract)
          activityAreas (string, repeatable): List of activity areas `id` to filter (described by /api/rest/application/dictionary/setting.activityArea)
          expertiseAreas (string, repeatable): List of expertise areas `id` to filter (described by /api/rest/application/dictionary/setting.expertiseArea)
          tools (string, repeatable): List of tools `id` to filter (described by /api/rest/application/dictionary/setting.tool)
          mobilityAreas (string): List of mobility areas `id` to filter (described by /api/rest/application/dictionary/setting.mobilityArea)
          experiences (integer, repeatable): List of experiences `id` to filter (described by /api/rest/application/dictionary/setting.experience)
          trainings (string, repeatable): List of trainings `id` to filter (described by /api/rest/application/dictionary/setting.training)
          period (string): * `created` : Candidates created between `startDate` and `endDate` are filtered
          periodDynamic (string): * `today` : Candidates filtered according to the grid for today's period
          periodDynamicParameters (string): Filter parameters of dynamic period. Used when periodDynamic is "lastCustomPeriod" or "nextCustomPeriod"
          startDate (string): Start date
          endDate (string): End date
          flags (integer, repeatable): Candidates attached to this flag whom flag's unique identifier = integer are filtered
          candidateStates (integer, repeatable): List of candidate states `id` to filter (described by /api/rest/application/dictionary/setting.state.candidate)
          perimeterManagersType (string): - `main`: The filter **perimeterManagers** is used only on the **Main Manager** of candidates
          availabilityTypes (integer, repeatable): List of availability `id` to filter (described by /api/rest/application/dictionary/setting.availability)
          languages (string, repeatable): List of languages spoken `id` to filter (described by /api/rest/application/dictionary/setting.languageSpoken)
          evaluations (string, repeatable): List of evaluations `id` to filter (described by /api/rest/application/dictionary/setting.evaluation)
          sources (string, repeatable): List of sources `id` to filter (described by /api/rest/application/dictionary/setting.source)
          candidateTypes (integer, repeatable): List of candidate types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.resource)
          onlyVisible (boolean, default True): The user has to have the global right `showGroupe` set to `true` or call this api into mode `god`.
          encoding (string): If the output format is **csv** then **encoding** filter should be one of
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: lastName | title | availability | numberOfActivePositionings | mainManager.lastName | updateDate | state | experience | creationDate | evaluation | hrManager.lastName | source
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/apps/advanced-candidates/candidates", params=params, validate=validate))

    async def post_advanced_candidates_candidates(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /apps/advanced-candidates/candidates
        
        Create a candidate
        
        Request body schema: appsAdvancedCandidatesCandidatesBody-post
        """
        return Document(await self._client.request("POST", "/apps/advanced-candidates/candidates", json=body, params=params, validate=validate))

    async def advanced_candidates_candidates_default(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/advanced-candidates/candidates/default
        
        Get empty candidate's default specific data
        """
        return Document(await self._client.request("GET", "/apps/advanced-candidates/candidates/default", params=params, validate=validate))

    async def advanced_candidates_candidates_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/advanced-candidates/candidates/{id}
        
        Get candidate's specific data
        """
        return Document(await self._client.request("GET", f"/apps/advanced-candidates/candidates/{id}", params=params, validate=validate))

    async def update_advanced_candidates_candidates_by_id(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/advanced-candidates/candidates/{id}
        
        Update specific data related to a candidate
        
        Query params:
          importResumes (boolean): If `true` if you want to import candidate's resumes into the new resource when candidate is hired
          importFiles (boolean): If `true` if you want to import candidate's files into the new resource when candidate is hired
          importContractFiles (boolean): If `true` if you want to import candidate's cp,tract file into the new resource when candidate is hired
          importContract (boolean, default True): If `true` if you want to import candidate's contract into the updated resource when candidate is hired again
          importFields (string): List of resource's fields to update from candidate when candidate is hired again. Fields available
        
        Request body schema: appsAdvancedCandidatesCandidatesBody-put
        """
        return Document(await self._client.request("PUT", f"/apps/advanced-candidates/candidates/{id}", json=body, params=params, validate=validate))

    async def advanced_candidates_candidates_by_id_download(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/advanced-candidates/candidates/{id}/download
        
        Get candidate's specific data formatted file content
        """
        return Document(await self._client.request("GET", f"/apps/advanced-candidates/candidates/{id}/download", params=params, validate=validate))

    async def advanced_candidates_candidates_by_id_rights(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/advanced-candidates/candidates/{id}/rights
        
        Get candidate's rights
        """
        return Document(await self._client.request("GET", f"/apps/advanced-candidates/candidates/{id}/rights", params=params, validate=validate))

    async def advanced_candidates_candidates_by_id_tasks(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/advanced-candidates/candidates/{id}/tasks
        
        Get candidate's tasks
        """
        return Document(await self._client.request("GET", f"/apps/advanced-candidates/candidates/{id}/tasks", params=params, validate=validate))

    async def advanced_candidates_resources_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/advanced-candidates/resources/{id}
        
        Get app's Candidates+ resource configuration data
        """
        return Document(await self._client.request("GET", f"/apps/advanced-candidates/resources/{id}", params=params, validate=validate))

    async def update_advanced_candidates_resources_by_id(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/advanced-candidates/resources/{id}
        
        Update resource configuration data related to app's Candidates+
        
        Request body schema: appsAdvancedCandidatesResourcesBody-put
        """
        return Document(await self._client.request("PUT", f"/apps/advanced-candidates/resources/{id}", json=body, params=params, validate=validate))

    async def advanced_projects_configuration(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/advanced-projects/configuration
        
        Get app's Projects+ configuration data
        """
        return Document(await self._client.request("GET", "/apps/advanced-projects/configuration", params=params, validate=validate))

    async def update_advanced_projects_configuration(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/advanced-projects/configuration
        
        Update configuration data related to Projects+'s customer
        
        Request body schema: appsAdvancedProjectsConfigurationBody-put
        """
        return Document(await self._client.request("PUT", "/apps/advanced-projects/configuration", json=body, params=params, validate=validate))

    async def advanced_projects_projects(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/advanced-projects/projects
        
        Search projects
        
        Query params:
          keywords (string): If `keywords = PRJ**ID1** MIS**ID2** COMP**ID3** CCON**ID4** CSOC**ID5** AO**ID6** PROD**ID7** CTR**ID8**` then projects
          month (string): month
          projectStates (integer, repeatable): List of project states `id` to filter (described by /api/rest/application/dictionary/setting.state.project)
          projectTypes (integer, repeatable): List of project types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.project)
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: currentTerm | reference | mainManager.lastName | startDate | endDate | company.name
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/apps/advanced-projects/projects", params=params, validate=validate))

    async def advanced_projects_projects_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/advanced-projects/projects/{id}
        
        Get project's specific data
        """
        return Document(await self._client.request("GET", f"/apps/advanced-projects/projects/{id}", params=params, validate=validate))

    async def update_advanced_projects_projects_by_id(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/advanced-projects/projects/{id}
        
        Update specific data related to a project
        
        Request body schema: appsAdvancedProjectsProjectsBody-put
        """
        return Document(await self._client.request("PUT", f"/apps/advanced-projects/projects/{id}", json=body, params=params, validate=validate))

    async def advantages_advantages(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/advantages/advantages
        
        Search advantages
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/advantages.csv?keywords=COMP100*
        
        Query params:
          keywords (string): If `keywords = ADV**ID1** COMP**ID2** CTR**ID3**` then
          resourceTypes (integer, repeatable): List of resource types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.resource)
          resourceStates (integer, repeatable): List of resource states `id` to filter (described by /api/rest/application/dictionary/setting.state.resource)
          period (string): * `paid` : Paid advantages between `startDate` and `endDate` are filtered
          periodDynamic (string): * `today` : Advantages filtered according to the grid for today's period
          periodDynamicParameters (string): Filter parameters of dynamic period. Used when periodDynamic is "lastCustomPeriod" or "nextCustomPeriod"
          startDate (string): Start date
          endDate (string): End date
          encoding (string): If the output format is **csv** then **encoding** filter should be one of
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: date | advantageType.reference | resource.lastName
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/apps/advantages/advantages", params=params, validate=validate))

    async def answering_validators_answering_machines(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/answering-validators/answering-machines
        
        Search answering machines
        
        Query params:
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          keywords (string): If `keywords = ANS**ID1**` then answering machines
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
        """
        return Document(await self._client.request("GET", "/apps/answering-validators/answering-machines", params=params, validate=validate))

    async def post_answering_validators_answering_machines(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /apps/answering-validators/answering-machines
        
        Create an answering machine.
        
        Query params:
          sendMail (boolean): If `true` to send an email
        
        Request body schema: appsAnsweringValidatorsAnsweringMachinesBody-post
        """
        return Document(await self._client.request("POST", "/apps/answering-validators/answering-machines", json=body, params=params, validate=validate))

    async def delete_answering_validators_answering_machines_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /apps/answering-validators/answering-machines/{id}
        
        Delete the answering machine
        """
        return Document(await self._client.request("DELETE", f"/apps/answering-validators/answering-machines/{id}", params=params, validate=validate))

    async def backup_database_configuration(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/backup-database/configuration
        
        Get app's BackupDatabase configuration data
        """
        return Document(await self._client.request("GET", "/apps/backup-database/configuration", params=params, validate=validate))

    async def update_backup_database_configuration(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/backup-database/configuration
        
        Update configuration data related to BackupDatabase's customer
        
        Request body schema: appsBackupDatabaseConfigurationBody-put
        """
        return Document(await self._client.request("PUT", "/apps/backup-database/configuration", json=body, params=params, validate=validate))

    async def backup_database_dump_database(self, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /apps/backup-database/dump-database
        
        Dump database
        """
        return Document(await self._client.request("POST", "/apps/backup-database/dump-database", json=body, params=params, validate=validate))

    async def celebrations_configuration(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/celebrations/configuration
        
        Get app's Celebrations customer configuration data
        """
        return Document(await self._client.request("GET", "/apps/celebrations/configuration", params=params, validate=validate))

    async def update_celebrations_configuration(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/celebrations/configuration
        
        Update configuration data related to Celebrations customer, main's tab
        
        Request body schema: appsCelebrationsConfigurationBody-put
        """
        return Document(await self._client.request("PUT", "/apps/celebrations/configuration", json=body, params=params, validate=validate))

    async def celebrations_employees_arrival(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/celebrations/employees/arrival
        
        Search resources celebrating their arrival
        
        Query params:
          keywords (string): Filter only on firstname , lastname, fullName and title
          resourceTypes (integer, repeatable): List of resource types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.resource)
          periodDynamic (string): ** WARNING : This parameter might be required if you did not provided `startDate` and `endDate` parameters**
          startDate (string): Start date
          endDate (string): End date
          resourceStates (integer, repeatable): List of resource states `id` to filter (described by /api/rest/application/dictionary/setting.state.resource)
        """
        return Document(await self._client.request("GET", "/apps/celebrations/employees/arrival", params=params, validate=validate))

    async def celebrations_employees_birthday(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/celebrations/employees/birthday
        
        Search resources celebrating their birthday
        
        Query params:
          keywords (string): Filter only on firstname , lastname, fullName and title
          resourceTypes (integer, repeatable): List of resource types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.resource)
          periodDynamic (string): ** WARNING : This parameter might be required if you did not provided `startDate` and `endDate` parameters**
          startDate (string): Start date
          endDate (string): End date
          resourceStates (integer, repeatable): List of resource states `id` to filter (described by /api/rest/application/dictionary/setting.state.resource)
        """
        return Document(await self._client.request("GET", "/apps/celebrations/employees/birthday", params=params, validate=validate))

    async def celebrations_employees_seniority(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/celebrations/employees/seniority
        
        Search resources celebrating their seniority
        
        Query params:
          keywords (string): Filter only on firstname , lastname, fullName and title
          resourceTypes (integer, repeatable): List of resource types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.resource)
          periodDynamic (string): ** WARNING : This parameter might be required if you did not provided `startDate` and `endDate` parameters**
          startDate (string): Start date
          endDate (string): End date
          resourceStates (integer, repeatable): List of resource states `id` to filter (described by /api/rest/application/dictionary/setting.state.resource)
        """
        return Document(await self._client.request("GET", "/apps/celebrations/employees/seniority", params=params, validate=validate))

    async def celebrations_employees_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/celebrations/employees/{id}
        
        Get app's Celebrations resource configuration data
        """
        return Document(await self._client.request("GET", f"/apps/celebrations/employees/{id}", params=params, validate=validate))

    async def update_celebrations_employees_by_id(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/celebrations/employees/{id}
        
        Update resource configuration data related to app's Celebrations
        
        Request body schema: appsCelebrationsEmployeesConfigurationBody-put
        """
        return Document(await self._client.request("PUT", f"/apps/celebrations/employees/{id}", json=body, params=params, validate=validate))

    async def contracts_contracts(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/contracts/contracts
        
        Search contracts
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/contracts.csv?keywords=CTR100*
        
        Query params:
          keywords (string): If `keywords = CTR**ID1** COMP**ID2**` then
          resourceTypes (integer, repeatable): List of resource types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.resource)
          contractTypes (integer, repeatable): List of contract types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.contract)
          excludeResourceTypes (integer, repeatable): List of resource types `id` not filtered (described by /api/rest/application/dictionary/setting.typeOf.resource)
          resourceStates (integer, repeatable): List of resource states `id` to filter (described by /api/rest/application/dictionary/setting.state.resource)
          period (string): * `current` : Current contracts between `startDate` and `endDate` are filtered
          periodDynamic (string): * `today` : Contracts filtered according to the grid for today's period
          periodDynamicParameters (string): Filter parameters of dynamic period. Used when periodDynamic is "lastCustomPeriod" or "nextCustomPeriod"
          startDate (string): Start date
          endDate (string): End date
          encoding (string): If the output format is **csv** then **encoding** filter should be one of
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: startDate | typeOf | endDate | dependsOn.lastName | dependsOn.function
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/apps/contracts/contracts", params=params, validate=validate))

    async def corporama_configuration(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/corporama/configuration
        
        Get app's Corporama configuration data
        """
        return Document(await self._client.request("GET", "/apps/corporama/configuration", params=params, validate=validate))

    async def create_activity_documents_resources_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/create-activity-documents/resources/{id}
        
        Get resource's basic data
        """
        return Document(await self._client.request("GET", f"/apps/create-activity-documents/resources/{id}", params=params, validate=validate))

    async def data_closing_closed_periods(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/data-closing/closed-periods
        
        Search closed periods
        
        Query params:
          parentTypes (string, repeatable): List of closed period parent types `id` to filter
          perimeterAgencies (integer, repeatable): Results whom closed period belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: agency.name | parentType | period
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/apps/data-closing/closed-periods", params=params, validate=validate))

    async def update_data_closing_closed_periods_by_id(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/data-closing/closed-periods/{id}
        
        Update specific data related to a closed period
        
        Request body schema: closedPeriodsBody-put
        """
        return Document(await self._client.request("PUT", f"/apps/data-closing/closed-periods/{id}", json=body, params=params, validate=validate))

    async def data_closing_configuration(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/data-closing/configuration
        
        Get app's DataClosing configuration data
        """
        return Document(await self._client.request("GET", "/apps/data-closing/configuration", params=params, validate=validate))

    async def update_data_closing_configuration(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/data-closing/configuration
        
        Update configuration data related to DataClosing's customer
        
        Request body schema: appsDataClosingConfigurationBody-put
        """
        return Document(await self._client.request("PUT", "/apps/data-closing/configuration", json=body, params=params, validate=validate))

    async def data_closing_expenses_reports(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/data-closing/expenses-reports
        
        Search expenses
        
        Query params:
          startMonth (string, REQUIRED): Start month
          endMonth (string, REQUIRED): End month
          keywords (string): If `keywords = TPS**ID1** COMP**ID2**` then timesheets
          validationStates (string, repeatable, one of: waitingForValidation | validated | rejected)
          closed (integer): If `true` returns only expenses closed, if `false` returns only expenses which are not closed
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: term | closed | state | resource.lastName
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/apps/data-closing/expenses-reports", params=params, validate=validate))

    async def update_data_closing_expenses_reports_by_id(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/data-closing/expenses-reports/{id}
        
        Update specific data related to an expenses
        
        Request body schema: appsDataClosingExpensesReportsBody-put
        """
        return Document(await self._client.request("PUT", f"/apps/data-closing/expenses-reports/{id}", json=body, params=params, validate=validate))

    async def data_closing_invoices(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/data-closing/invoices
        
        Search invoices
        
        Query params:
          startDate (string, REQUIRED): Start date
          endDate (string, REQUIRED): End date
          keywords (string): If `keywords = FACT**ID1** BDC**ID2** PRJ**ID3** CCON**ID4** CSOC**ID5**` then invoices
          states (integer, repeatable): List of invoice states `id` to filter (described by /api/rest/application/dictionary/setting.state.invoice)
          closed (integer): If `true` returns only invoices closed, if `false` returns only invoices which are not closed
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: date | reference | state | reference | order.number | order.project.reference | order.project.company.name
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/apps/data-closing/invoices", params=params, validate=validate))

    async def update_data_closing_invoices_by_id(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/data-closing/invoices/{id}
        
        Update specific data related to an invoice
        
        Request body schema: appsDataClosingInvoicesBody-put
        """
        return Document(await self._client.request("PUT", f"/apps/data-closing/invoices/{id}", json=body, params=params, validate=validate))

    async def data_closing_times_reports(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/data-closing/times-reports
        
        Search timesheets
        
        Query params:
          startMonth (string, REQUIRED): Start month
          endMonth (string, REQUIRED): End month
          keywords (string): If `keywords = TPS**ID1** COMP**ID2**` then timesheets
          validationStates (string, repeatable, one of: waitingForValidation | validated | rejected)
          closed (integer): If `true` returns only timesheets closed, if `false` returns only timesheets which are not closed
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: term | closed | state | resource.lastName
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/apps/data-closing/times-reports", params=params, validate=validate))

    async def update_data_closing_times_reports_by_id(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/data-closing/times-reports/{id}
        
        Update specific data related to a timesheet
        
        Request body schema: appsDataClosingTimesReportsBody-put
        """
        return Document(await self._client.request("PUT", f"/apps/data-closing/times-reports/{id}", json=body, params=params, validate=validate))

    async def digital_workplace_categories(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/digital-workplace/categories
        
        Get app's digital workplace categories
        """
        return Document(await self._client.request("GET", "/apps/digital-workplace/categories", params=params, validate=validate))

    async def post_digital_workplace_categories(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /apps/digital-workplace/categories
        
        Add app's digital workplace new category
        
        Request body schema: appsDigitalWorkplaceCategoryBody-post
        """
        return Document(await self._client.request("POST", "/apps/digital-workplace/categories", json=body, params=params, validate=validate))

    async def delete_digital_workplace_categories_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /apps/digital-workplace/categories/{id}
        
        Delete app's Digital workplace category
        """
        return Document(await self._client.request("DELETE", f"/apps/digital-workplace/categories/{id}", params=params, validate=validate))

    async def digital_workplace_categories_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/digital-workplace/categories/{id}
        
        Get app's Digital workplace category data
        """
        return Document(await self._client.request("GET", f"/apps/digital-workplace/categories/{id}", params=params, validate=validate))

    async def update_digital_workplace_categories_by_id(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/digital-workplace/categories/{id}
        
        Update app's Digital workplace category
        
        Request body schema: appsDigitalWorkplaceCategoryBody-put
        """
        return Document(await self._client.request("PUT", f"/apps/digital-workplace/categories/{id}", json=body, params=params, validate=validate))

    async def digital_workplace_documents(self, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /apps/digital-workplace/documents
        
        Create a document
        """
        return Document(await self._client.request("POST", "/apps/digital-workplace/documents", json=body, params=params, validate=validate))

    async def digital_workplace_documents_viewer(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/digital-workplace/documents/viewer
        
        Search documents for app's viewer.
        
        You must have an app's viewer installed.
        
        Query params:
          documents (string, repeatable): Documents whom document's unique identifier are filtered
        """
        return Document(await self._client.request("GET", "/apps/digital-workplace/documents/viewer", params=params, validate=validate))

    async def delete_digital_workplace_documents_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /apps/digital-workplace/documents/{id}
        
        Delete the document
        """
        return Document(await self._client.request("DELETE", f"/apps/digital-workplace/documents/{id}", params=params, validate=validate))

    async def digital_workplace_documents_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/digital-workplace/documents/{id}
        
        Get document content
        """
        return Document(await self._client.request("GET", f"/apps/digital-workplace/documents/{id}", params=params, validate=validate))

    async def digital_workplace_news(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/digital-workplace/news
        
        Search digital workplace news
        
        Query params:
          keywords (string): If `keywords = POST**ID1** POST**ID2**` then news
          resourceTypes (integer, repeatable): List of resource types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.resource)
          perimeterAgencies (integer, repeatable): List of agencies `id` to filter
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: creationDate
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/apps/digital-workplace/news", params=params, validate=validate))

    async def post_digital_workplace_news(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /apps/digital-workplace/news
        
        Add app's digital workplace new news
        
        Request body schema: appsDigitalWorkplaceNewsBody-post
        """
        return Document(await self._client.request("POST", "/apps/digital-workplace/news", json=body, params=params, validate=validate))

    async def delete_digital_workplace_news_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /apps/digital-workplace/news/{id}
        
        Delete app's Digital news category
        """
        return Document(await self._client.request("DELETE", f"/apps/digital-workplace/news/{id}", params=params, validate=validate))

    async def digital_workplace_news_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/digital-workplace/news/{id}
        
        Get app's Digital workplace news data
        """
        return Document(await self._client.request("GET", f"/apps/digital-workplace/news/{id}", params=params, validate=validate))

    async def update_digital_workplace_news_by_id(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/digital-workplace/news/{id}
        
        Update app's Digital news category
        
        Request body schema: appsDigitalWorkplaceNewsBody-put
        """
        return Document(await self._client.request("PUT", f"/apps/digital-workplace/news/{id}", json=body, params=params, validate=validate))

    async def doc_templates_configuration(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/doc-templates/configuration
        
        Get app's DocumentsTemplates configuration data
        """
        return Document(await self._client.request("GET", "/apps/doc-templates/configuration", params=params, validate=validate))

    async def doc_templates_templates(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/doc-templates/templates
        
        Search templates available for an entity (candidate, resource, opportunity, order, purchase, contract, delivery, quotation)
        
        Query params:
          keywords (string, REQUIRED): Must contains only one internal reference of following entities
          types (string, repeatable): * `candidate`
        """
        return Document(await self._client.request("GET", "/apps/doc-templates/templates", params=params, validate=validate))

    async def post_doc_templates_templates(self, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /apps/doc-templates/templates
        
        Create a template
        """
        return Document(await self._client.request("POST", "/apps/doc-templates/templates", json=body, params=params, validate=validate))

    async def doc_templates_templates_viewer(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/doc-templates/templates/viewer
        
        Search templates for app's viewer.
        
        You must have an app's viewer installed.
        
        Query params:
          documents (string, repeatable): Templates whom document's unique identifier are filtered
        """
        return Document(await self._client.request("GET", "/apps/doc-templates/templates/viewer", params=params, validate=validate))

    async def delete_doc_templates_templates_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /apps/doc-templates/templates/{id}
        
        Delete the template
        """
        return Document(await self._client.request("DELETE", f"/apps/doc-templates/templates/{id}", params=params, validate=validate))

    async def doc_templates_templates_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/doc-templates/templates/{id}
        
        Get template content
        """
        return Document(await self._client.request("GET", f"/apps/doc-templates/templates/{id}", params=params, validate=validate))

    async def update_doc_templates_templates_by_id(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/doc-templates/templates/{id}
        
        update template content
        
        Request body schema: appsDocTemplatesTemplatesProfileBody-put
        """
        return Document(await self._client.request("PUT", f"/apps/doc-templates/templates/{id}", json=body, params=params, validate=validate))

    async def emailing_absencesreports_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/emailing/absencesreports/{id}
        
        Get app's EMailing absencesreports data, main's tab
        """
        return Document(await self._client.request("GET", f"/apps/emailing/absencesreports/{id}", params=params, validate=validate))

    async def emailing_candidates_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/emailing/candidates/{id}
        
        Get app's EMailing candidate data
        """
        return Document(await self._client.request("GET", f"/apps/emailing/candidates/{id}", params=params, validate=validate))

    async def emailing_configuration(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/emailing/configuration
        
        Get app's EMailing customer configuration data, main's tab
        """
        return Document(await self._client.request("GET", "/apps/emailing/configuration", params=params, validate=validate))

    async def update_emailing_configuration(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/emailing/configuration
        
        Update configuration data related to EMailing customer, main's tab
        
        Request body schema: appsEMailingConfigurationBody-put
        """
        return Document(await self._client.request("PUT", "/apps/emailing/configuration", json=body, params=params, validate=validate))

    async def emailing_configuration_connection(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/emailing/configuration/connection
        
        Get app's EMailing test connection results
        """
        return Document(await self._client.request("GET", "/apps/emailing/configuration/connection", params=params, validate=validate))

    async def emailing_contacts_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/emailing/contacts/{id}
        
        Get app's EMailing contact data, main's tab
        """
        return Document(await self._client.request("GET", f"/apps/emailing/contacts/{id}", params=params, validate=validate))

    async def emailing_expensesreports_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/emailing/expensesreports/{id}
        
        Get app's EMailing expensesreports data, main's tab
        """
        return Document(await self._client.request("GET", f"/apps/emailing/expensesreports/{id}", params=params, validate=validate))

    async def emailing_invoices_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/emailing/invoices/{id}
        
        Get app's EMailing invoice data, main's tab
        """
        return Document(await self._client.request("GET", f"/apps/emailing/invoices/{id}", params=params, validate=validate))

    async def emailing_positionings_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/emailing/positionings/{id}
        
        Get app's EMailing positioning data, main's tab
        """
        return Document(await self._client.request("GET", f"/apps/emailing/positionings/{id}", params=params, validate=validate))

    async def emailing_quotations_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/emailing/quotations/{id}
        
        Get app's EMailing quotation data, main's tab
        """
        return Document(await self._client.request("GET", f"/apps/emailing/quotations/{id}", params=params, validate=validate))

    async def emailing_resources_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/emailing/resources/{id}
        
        Get app's EMailing resource data, main's tab
        """
        return Document(await self._client.request("GET", f"/apps/emailing/resources/{id}", params=params, validate=validate))

    async def emailing_resources_by_id_connection(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/emailing/resources/{id}/connection
        
        Get app's EMailing test connection results
        """
        return Document(await self._client.request("GET", f"/apps/emailing/resources/{id}/connection", params=params, validate=validate))

    async def emailing_resources_by_id_settings(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/emailing/resources/{id}/settings
        
        Get app's EMailing resource configuration data, main's tab
        """
        return Document(await self._client.request("GET", f"/apps/emailing/resources/{id}/settings", params=params, validate=validate))

    async def update_emailing_resources_by_id_settings(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/emailing/resources/{id}/settings
        
        Update configuration data related to EMailing resource, main's tab
        
        Request body schema: appsEMailingResourcesSettingsBody-put
        """
        return Document(await self._client.request("PUT", f"/apps/emailing/resources/{id}/settings", json=body, params=params, validate=validate))

    async def emailing_share(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /apps/emailing/share
        
        Share a push/message
        
        Request body schema: appsEMailingShareBody-post
        """
        return Document(await self._client.request("POST", "/apps/emailing/share", json=body, params=params, validate=validate))

    async def emailing_templates(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/emailing/templates
        
        Search templates
        
        Query params:
          isAdministrator (boolean)
          templateType (string, one of: pushMessage | invoice | activity | quotation): Type of template to search
          keywords (string): Search emailing templates on title
        """
        return Document(await self._client.request("GET", "/apps/emailing/templates", params=params, validate=validate))

    async def post_emailing_templates(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /apps/emailing/templates
        
        Create a template
        
        Request body schema: appsEMailingTemplatesBody-post
        """
        return Document(await self._client.request("POST", "/apps/emailing/templates", json=body, params=params, validate=validate))

    async def emailing_templates_last_used(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/emailing/templates/last-used
        
        Get last used template's data
        
        Query params:
          templateType (string, REQUIRED, one of: pushMessage | invoice | activity | quotation): Type of template to search
        """
        return Document(await self._client.request("GET", "/apps/emailing/templates/last-used", params=params, validate=validate))

    async def delete_emailing_templates_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /apps/emailing/templates/{id}
        
        Delete the template
        """
        return Document(await self._client.request("DELETE", f"/apps/emailing/templates/{id}", params=params, validate=validate))

    async def emailing_templates_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/emailing/templates/{id}
        
        Get template's data
        """
        return Document(await self._client.request("GET", f"/apps/emailing/templates/{id}", params=params, validate=validate))

    async def update_emailing_templates_by_id(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/emailing/templates/{id}
        
        Update data related to a template.
        
        Request body schema: appsEMailingTemplatesBody-put
        """
        return Document(await self._client.request("PUT", f"/apps/emailing/templates/{id}", json=body, params=params, validate=validate))

    async def emailing_timesreports_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/emailing/timesreports/{id}
        
        Get app's EMailing timesreports data, main's tab
        """
        return Document(await self._client.request("GET", f"/apps/emailing/timesreports/{id}", params=params, validate=validate))

    async def esignature_candidates_default(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/esignature/candidates/default
        
        Get empty esignature's default specific data
        """
        return Document(await self._client.request("GET", "/apps/esignature/candidates/default", params=params, validate=validate))

    async def esignature_esignatures(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /apps/esignature/esignatures
        
        Create an esignature
        
        Request body schema: appsEsignatureEsignaturesBody-post
        """
        return Document(await self._client.request("POST", "/apps/esignature/esignatures", json=body, params=params, validate=validate))

    async def delete_esignature_esignatures_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /apps/esignature/esignatures/{id}
        
        Delete/cancel esignature's specific data
        """
        return Document(await self._client.request("DELETE", f"/apps/esignature/esignatures/{id}", params=params, validate=validate))

    async def esignature_esignatures_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/esignature/esignatures/{id}
        
        Get esignature's specific data
        """
        return Document(await self._client.request("GET", f"/apps/esignature/esignatures/{id}", params=params, validate=validate))

    async def esignature_esignatures_by_id_cancel(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /apps/esignature/esignatures/{id}/cancel
        
        Cancel an esignature
        
        Request body schema: appsEsignatureEsignaturesCancelBody-post
        """
        return Document(await self._client.request("POST", f"/apps/esignature/esignatures/{id}/cancel", json=body, params=params, validate=validate))

    async def exceptional_activity_companies(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/exceptional-activity/companies
        
        Search companies
        
        Query params:
          keywords (string): Available only if `type` is `boondmanagerCompanies`.
          states (integer, repeatable): List of company states `id` to filter (described by /api/rest/application/dictionary/setting.state.company).
          typeOfScales (string, one of: withScales | withoutScales)
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: name | state
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/apps/exceptional-activity/companies", params=params, validate=validate))

    async def exceptional_activity_times(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/exceptional-activity/times
        
        Search times
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/times.csv?keywords=TPSEXP1*
        
        Query params:
          month (string, REQUIRED): month
          keywords (string): If `keywords = COMP**ID1** PRJ**ID2** CCON**ID3** CSOC**ID4**` then times
          workUnitTypes (string, repeatable): List of entity workunit types `id`, related to the agency's entity, to filter
          category (string, one of: regular | exceptional)
          resourceTypes (integer, repeatable): List of resource types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.resource)
          encoding (string): If the output format is **csv** then **encoding** filter should be one of
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: startDate | workUnitType.reference | timesReport.resource.lastName | timesReport.state | delivery.project.company.name | delivery.project.reference | recovering | processed
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/apps/exceptional-activity/times", params=params, validate=validate))

    async def exceptional_activity_times_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/exceptional-activity/times/{id}
        
        Get time data
        """
        return Document(await self._client.request("GET", f"/apps/exceptional-activity/times/{id}", params=params, validate=validate))

    async def update_exceptional_activity_times_by_id(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/exceptional-activity/times/{id}
        
        Update time data
        
        Request body schema: appsExtractPayrollTimesBody-put
        """
        return Document(await self._client.request("PUT", f"/apps/exceptional-activity/times/{id}", json=body, params=params, validate=validate))

    async def extract_payroll_contracts(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/extract-payroll/contracts
        
        Search contracts
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/apps/extract-payroll/contracts.csv?keywords=COMP100*
        
        Query params:
          month (string, REQUIRED): month
          keywords (string): If `keywords = CTR**ID1** COMP**ID2**` then contracts
          resourceTypes (integer, repeatable): List of resource types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.resource)
          encoding (string): If the output format is **csv** then **encoding** filter should be one of
          generateAdvantages (boolean): Generate advantages for all contracts found
          extractOnlyValidatedExpenses (boolean)
          extractType (string, default extractInDays): If the output format is **csv** then **extractType** filter should be one of
        """
        return Document(await self._client.request("GET", "/apps/extract-payroll/contracts", params=params, validate=validate))

    async def update_extract_payroll_contracts_by_id(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/extract-payroll/contracts/{id}
        
        Update contract data related to app's ExtractPayroll
        
        Request body schema: appsExtractPayrollContractsBody-put
        """
        return Document(await self._client.request("PUT", f"/apps/extract-payroll/contracts/{id}", json=body, params=params, validate=validate))

    async def extract_payroll_resources_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/extract-payroll/resources/{id}
        
        Get app's ExtractPayroll resource configuration data
        """
        return Document(await self._client.request("GET", f"/apps/extract-payroll/resources/{id}", params=params, validate=validate))

    async def update_extract_payroll_resources_by_id(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/extract-payroll/resources/{id}
        
        Update resource configuration data related to app's ExtractPayroll
        
        Request body schema: appsExtractPayrollResourcesBody-put
        """
        return Document(await self._client.request("PUT", f"/apps/extract-payroll/resources/{id}", json=body, params=params, validate=validate))

    async def extractbi_configuration(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/extractbi/configuration
        
        Get app's ExtractBI configuration data
        """
        return Document(await self._client.request("GET", "/apps/extractbi/configuration", params=params, validate=validate))

    async def update_extractbi_configuration(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/extractbi/configuration
        
        Update configuration data related to ExtractBI's customer
        
        Request body schema: appsExtractBIConfigurationBody-put
        """
        return Document(await self._client.request("PUT", "/apps/extractbi/configuration", json=body, params=params, validate=validate))

    async def extractbi_requests(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/extractbi/requests
        
        Search requests
        
        Query params:
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
        """
        return Document(await self._client.request("GET", "/apps/extractbi/requests", params=params, validate=validate))

    async def post_extractbi_requests(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /apps/extractbi/requests
        
        Create a request
        
        Request body schema: appsExtractBIRequestsBody-post
        """
        return Document(await self._client.request("POST", "/apps/extractbi/requests", json=body, params=params, validate=validate))

    async def delete_extractbi_requests_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /apps/extractbi/requests/{id}
        
        Delete the request
        """
        return Document(await self._client.request("DELETE", f"/apps/extractbi/requests/{id}", params=params, validate=validate))

    async def extractbi_requests_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/extractbi/requests/{id}
        
        Get request's basic data
        """
        return Document(await self._client.request("GET", f"/apps/extractbi/requests/{id}", params=params, validate=validate))

    async def update_extractbi_requests_by_id(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/extractbi/requests/{id}
        
        Update basic data related to a request
        
        Request body schema: appsExtractBIRequestsBody-put
        """
        return Document(await self._client.request("PUT", f"/apps/extractbi/requests/{id}", json=body, params=params, validate=validate))

    async def extractbi_requests_by_id_download(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/extractbi/requests/{id}/download
        
        Generate extract file
        """
        return Document(await self._client.request("GET", f"/apps/extractbi/requests/{id}/download", params=params, validate=validate))

    async def extractbi_templates(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/extractbi/templates
        
        Search templates
        
        Query params:
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
        """
        return Document(await self._client.request("GET", "/apps/extractbi/templates", params=params, validate=validate))

    async def post_extractbi_templates(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /apps/extractbi/templates
        
        Create a template
        
        Request body schema: appsExtractBIViewsBody-post
        """
        return Document(await self._client.request("POST", "/apps/extractbi/templates", json=body, params=params, validate=validate))

    async def delete_extractbi_templates_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /apps/extractbi/templates/{id}
        
        Delete the template
        """
        return Document(await self._client.request("DELETE", f"/apps/extractbi/templates/{id}", params=params, validate=validate))

    async def extractbi_templates_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/extractbi/templates/{id}
        
        Get view's basic data
        """
        return Document(await self._client.request("GET", f"/apps/extractbi/templates/{id}", params=params, validate=validate))

    async def update_extractbi_templates_by_id(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/extractbi/templates/{id}
        
        Update basic data related to a template
        
        Request body schema: appsExtractBIViewsBody-put
        """
        return Document(await self._client.request("PUT", f"/apps/extractbi/templates/{id}", json=body, params=params, validate=validate))

    async def extractbi_templates_by_id_rights(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/extractbi/templates/{id}/rights
        
        Get template's rights
        """
        return Document(await self._client.request("GET", f"/apps/extractbi/templates/{id}/rights", params=params, validate=validate))

    async def extractbi_test(self, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /apps/extractbi/test
        
        Test an a query with extractBI
        
        Query params:
          sql (string): an sql query to test
          language (string, one of: fr | es | en | auto): If the output format is **csv** then **encoding** filter should be one of
          encoding (string): If the output format is **csv** then **encoding** filter should be one of
        """
        return Document(await self._client.request("POST", "/apps/extractbi/test", json=body, params=params, validate=validate))

    async def gcalendar_get_event(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/gcalendar/get-event
        
        Get an event inside GCalendar
        
        Query params:
          signedRequest (string, REQUIRED): Signed request used to identify the user
        """
        return Document(await self._client.request("GET", "/apps/gcalendar/get-event", params=params, validate=validate))

    async def gcalendar_notifications_events(self, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /apps/gcalendar/notifications-events
        
        Receive event's notification from GCalendar
        """
        return Document(await self._client.request("POST", "/apps/gcalendar/notifications-events", json=body, params=params, validate=validate))

    async def delete_gcalendar_remove_event(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /apps/gcalendar/remove-event
        
        Remove an event inside GCalendar
        """
        return Document(await self._client.request("DELETE", "/apps/gcalendar/remove-event", params=params, validate=validate))

    async def gcalendar_resources_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/gcalendar/resources/{id}
        
        Get app's GCalendar resource configuration data
        """
        return Document(await self._client.request("GET", f"/apps/gcalendar/resources/{id}", params=params, validate=validate))

    async def update_gcalendar_update_event(self, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/gcalendar/update-event
        
        Update an event inside GCalendar
        """
        return Document(await self._client.request("PUT", "/apps/gcalendar/update-event", json=body, params=params, validate=validate))

    async def gmail_mails(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /apps/gmail/mails
        
        Add the mail like an action to boondmanager's resources/candidates/contacts
        
        Request body schema: appsGMailMailsBody-post
        """
        return Document(await self._client.request("POST", "/apps/gmail/mails", json=body, params=params, validate=validate))

    async def gmail_mails_by_id_mail(self, id_mail, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/gmail/mails/{idMail}
        
        Get mail's basic data
        
        Query params:
          emails (string, REQUIRED): list of emails to search into Boond
        """
        return Document(await self._client.request("GET", f"/apps/gmail/mails/{id_mail}", params=params, validate=validate))

    async def gmail_resources_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/gmail/resources/{id}
        
        Get app's GMail resource configuration data
        """
        return Document(await self._client.request("GET", f"/apps/gmail/resources/{id}", params=params, validate=validate))

    async def gviewer_download_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/gviewer/download/{id}
        
        Get document content
        
        Query params:
          signedRequest (string, REQUIRED): Signed request used to identify the user
          embedded (boolean): Flag to get the displayable or downloadable version of the document
        """
        return Document(await self._client.request("GET", f"/apps/gviewer/download/{id}", params=params, validate=validate))

    async def gviewer_resources_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/gviewer/resources/{id}
        
        Get app's GViewer resource configuration data
        """
        return Document(await self._client.request("GET", f"/apps/gviewer/resources/{id}", params=params, validate=validate))

    async def update_gviewer_resources_by_id(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/gviewer/resources/{id}
        
        Update resource configuration data related to app's GViewer
        
        Request body schema: appsGViewerResourcesBody-put
        """
        return Document(await self._client.request("PUT", f"/apps/gviewer/resources/{id}", json=body, params=params, validate=validate))

    async def gviewer_url_documents(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/gviewer/url-documents
        
        Get URLs to view documents
        
        Query params:
          signedRequest (string, REQUIRED): Signed request used to identify the user
        """
        return Document(await self._client.request("GET", "/apps/gviewer/url-documents", params=params, validate=validate))

    async def hour_accounts_configuration(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/hour-accounts/configuration
        
        Get app's HourAccount configuration data
        """
        return Document(await self._client.request("GET", "/apps/hour-accounts/configuration", params=params, validate=validate))

    async def update_hour_accounts_configuration(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/hour-accounts/configuration
        
        Update configuration data related to HourAccount's customer
        
        Request body schema: appsHourAccountsConfigurationBody-put
        """
        return Document(await self._client.request("PUT", "/apps/hour-accounts/configuration", json=body, params=params, validate=validate))

    async def hour_accounts_houraccounts(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/hour-accounts/houraccounts
        
        Search houraccounts
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/apps/hour-accounts/hour-accounts.csv*
        
        Query params:
          startMonth (string): startMonth
          endMonth (string): endMonth
          resources (integer, repeatable): List of resources `id`
          encoding (string): Must be one of
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: validated | term
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/apps/hour-accounts/houraccounts", params=params, validate=validate))

    async def hour_accounts_houraccounts_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/hour-accounts/houraccounts/{id}
        
        Get app's HourAccount data
        """
        return Document(await self._client.request("GET", f"/apps/hour-accounts/houraccounts/{id}", params=params, validate=validate))

    async def update_hour_accounts_houraccounts_by_id(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/hour-accounts/houraccounts/{id}
        
        Update data related to HourAccount
        
        Request body schema: appsHourAccountsHourAccountBody-put
        """
        return Document(await self._client.request("PUT", f"/apps/hour-accounts/houraccounts/{id}", json=body, params=params, validate=validate))

    async def hour_accounts_houraccounts_by_id_rights(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/hour-accounts/houraccounts/{id}/rights
        
        Get HourAccount's rights
        """
        return Document(await self._client.request("GET", f"/apps/hour-accounts/houraccounts/{id}/rights", params=params, validate=validate))

    async def hour_accounts_resources_by_id_rights(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/hour-accounts/resources/{id}/rights
        
        Get resource's rights
        """
        return Document(await self._client.request("GET", f"/apps/hour-accounts/resources/{id}/rights", params=params, validate=validate))

    async def hour_accounts_resources_by_id_settings(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/hour-accounts/resources/{id}/settings
        
        Get resource's settings basic data
        """
        return Document(await self._client.request("GET", f"/apps/hour-accounts/resources/{id}/settings", params=params, validate=validate))

    async def update_hour_accounts_resources_by_id_settings(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/hour-accounts/resources/{id}/settings
        
        Update basic data related to resource's settings
        
        Request body schema: appsHourAccountsResourceSettingsBody-put
        """
        return Document(await self._client.request("PUT", f"/apps/hour-accounts/resources/{id}/settings", json=body, params=params, validate=validate))

    async def hrflow_configuration(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/hrflow/configuration
        
        Get app's HrFlow configuration data
        """
        return Document(await self._client.request("GET", "/apps/hrflow/configuration", params=params, validate=validate))

    async def update_hrflow_configuration(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/hrflow/configuration
        
        Update configuration data related to HrFlow's customer
        
        Request body schema: appsHrFlowConfigurationBody-put
        """
        return Document(await self._client.request("PUT", "/apps/hrflow/configuration", json=body, params=params, validate=validate))

    async def hrflow_resumes(self, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /apps/hrflow/resumes
        
        Parse a resume
        """
        return Document(await self._client.request("POST", "/apps/hrflow/resumes", json=body, params=params, validate=validate))

    async def intranet_accounts_resources(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/intranet-accounts/resources
        
        Search resources
        
        Query params:
          keywords (string): If `keywords = COMP**ID2**` then resources
          resourceSubscriptions (string, repeatable): * `active` : Active resources are filtered
          resourceTypes (integer, repeatable): List of resource types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.resource)
          resourceStates (integer, repeatable): List of resource states `id` to filter (described by /api/rest/application/dictionary/setting.state.resource)
          roles (integer, repeatable): List of resource roles `id` to filter
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
        """
        return Document(await self._client.request("GET", "/apps/intranet-accounts/resources", params=params, validate=validate))

    async def update_intranet_accounts_resources_by_id(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/intranet-accounts/resources/{id}
        
        Update basic data related to a resource
        
        Request body schema: appsIntranetAccountsResourcesBody-put
        """
        return Document(await self._client.request("PUT", f"/apps/intranet-accounts/resources/{id}", json=body, params=params, validate=validate))

    async def markers_markers(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/markers/markers
        
        Search markers
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/markers.csv?keywords=PRJ100*
        
        Query params:
          keywords (string): If `keywords = PRJ**ID1** COMP**ID2**` then markers
          projectTypes (integer, repeatable): List of project types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.project)
          projectStates (integer, repeatable): List of project states `id` to filter (described by /api/rest/application/dictionary/setting.state.project)
          encoding (string): If the output format is **csv** then **encoding** filter should be one of
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: resource.lastName | date | batch.id | project.reference | company.name
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/apps/markers/markers", params=params, validate=validate))

    async def delete_microsoft_events_by_id_event(self, id_event, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /apps/microsoft/events/{idEvent}
        
        Delete the event's action on Boond
        """
        return Document(await self._client.request("DELETE", f"/apps/microsoft/events/{id_event}", params=params, validate=validate))

    async def microsoft_events_by_id_event(self, id_event, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/microsoft/events/{idEvent}
        
        Get event's basic data
        """
        return Document(await self._client.request("GET", f"/apps/microsoft/events/{id_event}", params=params, validate=validate))

    async def update_microsoft_events_by_id_event(self, id_event, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/microsoft/events/{idEvent}
        
        Synchronize an action on a boondmanager's resource/candidate/contact/opportunity/project/order/invoice
        
        Request body schema: appsMicrosoftEventsBody-put
        """
        return Document(await self._client.request("PUT", f"/apps/microsoft/events/{id_event}", json=body, params=params, validate=validate))

    async def microsoft_events_by_id_event_find(self, id_event, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/microsoft/events/{idEvent}/find
        
        Search resources, candidates, contacts, opportunities, projects, orders or invoices
        
        Query params:
          keywordsType (string, REQUIRED, default resource): * `resource` : Resources are filtered following `keywords`
          keywords (string, REQUIRED): If `keywords = CAND**ID1** COMP**ID2** CCON**ID3** BDC**ID4** FACT**ID5** AO**ID6** PRJ**ID7**` then profiles
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: lastName
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/apps/microsoft/events/{id_event}/find", params=params, validate=validate))

    async def microsoft_extra_id(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/microsoft/extra-id
        
        Get extraId basic's data inside Microsoft Gadget
        """
        return Document(await self._client.request("GET", "/apps/microsoft/extra-id", params=params, validate=validate))

    async def microsoft_gadget(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/microsoft/gadget
        
        Get Microsoft Office Gadget
        """
        return Document(await self._client.request("GET", "/apps/microsoft/gadget", params=params, validate=validate))

    async def microsoft_get_event(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/microsoft/get-event
        
        Get an event inside Microsoft Calendar
        
        Query params:
          signedRequest (string, REQUIRED): Signed request used to identify the user
        """
        return Document(await self._client.request("GET", "/apps/microsoft/get-event", params=params, validate=validate))

    async def microsoft_mails(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /apps/microsoft/mails
        
        Add the mail like an action to boondmanager's resources/candidates/contacts
        
        Request body schema: appsMicrosoftMailsBody-post
        """
        return Document(await self._client.request("POST", "/apps/microsoft/mails", json=body, params=params, validate=validate))

    async def microsoft_mails_by_id_mail(self, id_mail, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/microsoft/mails/{idMail}
        
        Get mail's basic data
        
        Query params:
          emails (string, REQUIRED): list of emails to search into Boond
        """
        return Document(await self._client.request("GET", f"/apps/microsoft/mails/{id_mail}", params=params, validate=validate))

    async def microsoft_manifest(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/microsoft/manifest
        
        Get Microsoft Office Manifest
        """
        return Document(await self._client.request("GET", "/apps/microsoft/manifest", params=params, validate=validate))

    async def delete_microsoft_remove_event(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /apps/microsoft/remove-event
        
        Remove an event inside Microsoft Calendar
        """
        return Document(await self._client.request("DELETE", "/apps/microsoft/remove-event", params=params, validate=validate))

    async def microsoft_resources_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/microsoft/resources/{id}
        
        Get app's Microsoft resource configuration data
        """
        return Document(await self._client.request("GET", f"/apps/microsoft/resources/{id}", params=params, validate=validate))

    async def update_microsoft_update_event(self, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/microsoft/update-event
        
        Update an event inside Microsoft Calendar
        """
        return Document(await self._client.request("PUT", "/apps/microsoft/update-event", json=body, params=params, validate=validate))

    async def organization_charts_nodes(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /apps/organization-charts/nodes
        
        Create organization chart's node
        
        Request body schema: appsOrganizationCharts-nodesBody-post
        """
        return Document(await self._client.request("POST", "/apps/organization-charts/nodes", json=body, params=params, validate=validate))

    async def delete_organization_charts_nodes_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /apps/organization-charts/nodes/{id}
        
        Delete the node
        """
        return Document(await self._client.request("DELETE", f"/apps/organization-charts/nodes/{id}", params=params, validate=validate))

    async def update_organization_charts_nodes_by_id(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/organization-charts/nodes/{id}
        
        Update data related to a node
        
        Request body schema: appsOrganizationCharts-nodesBody-put
        """
        return Document(await self._client.request("PUT", f"/apps/organization-charts/nodes/{id}", json=body, params=params, validate=validate))

    async def organization_charts_orgcharts(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/organization-charts/orgcharts
        
        Search organization charts
        
        Query params:
          type (string, REQUIRED, one of: company): Organization chart's type.
          id (string, REQUIRED): Company's unique identifier where to search orgcharts.
        """
        return Document(await self._client.request("GET", "/apps/organization-charts/orgcharts", params=params, validate=validate))

    async def post_organization_charts_orgcharts(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /apps/organization-charts/orgcharts
        
        Create an orgchart
        
        Request body schema: appsOrganizationCharts-orgChartsBody-post
        """
        return Document(await self._client.request("POST", "/apps/organization-charts/orgcharts", json=body, params=params, validate=validate))

    async def delete_organization_charts_orgcharts_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /apps/organization-charts/orgcharts/{id}
        
        Delete the organization chart
        """
        return Document(await self._client.request("DELETE", f"/apps/organization-charts/orgcharts/{id}", params=params, validate=validate))

    async def organization_charts_orgcharts_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/organization-charts/orgcharts/{id}
        
        Get organization chart's basic data
        """
        return Document(await self._client.request("GET", f"/apps/organization-charts/orgcharts/{id}", params=params, validate=validate))

    async def organization_charts_settings(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /apps/organization-charts/settings
        
        Create organization chart's settings
        
        Request body schema: appsOrganizationCharts-settingsBody-post
        """
        return Document(await self._client.request("POST", "/apps/organization-charts/settings", json=body, params=params, validate=validate))

    async def delete_organization_charts_settings_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /apps/organization-charts/settings/{id}
        
        delete this settings
        """
        return Document(await self._client.request("DELETE", f"/apps/organization-charts/settings/{id}", params=params, validate=validate))

    async def organization_charts_settings_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/organization-charts/settings/{id}
        
        Get settings data
        """
        return Document(await self._client.request("GET", f"/apps/organization-charts/settings/{id}", params=params, validate=validate))

    async def update_organization_charts_settings_by_id(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/organization-charts/settings/{id}
        
        Update settings data
        
        Request body schema: appsOrganizationCharts-settingsBody-put
        """
        return Document(await self._client.request("PUT", f"/apps/organization-charts/settings/{id}", json=body, params=params, validate=validate))

    async def plan_production_resources(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/plan-production/resources
        
        Search production plans, absences or times
        
        Query params:
          month (string, REQUIRED): month
          keywords (string): If `keywordsType` is not defined & `keywords = COMP**ID1** COMP**ID2**` then resources
          resourceTypes (integer, repeatable): List of resource types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.resource)
          resourceStates (integer, repeatable): List of resource states `id` to filter (described by /api/rest/application/dictionary/setting.state.resource)
          projectsIds (integer, repeatable): List of projects `id`
          contactsIds (integer, repeatable): List of contacts `id`
          companiesIds (integer, repeatable): List of companies `id`
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: lastName | availability
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/apps/plan-production/resources", params=params, validate=validate))

    async def post_production_projects(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/post-production/projects
        
        Search projects
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/apps/post-production/projects.csv?keywords=COMP100*
        
        Query params:
          month (string, REQUIRED): month
          keywords (string): If `keywords = PRJ**ID1** MIS**ID2** COMP**ID3** CCON**ID4** CSOC**ID5** AO**ID6** PROD**ID7** CTR**ID8**` then projects
          projectTypes (integer, repeatable): List of project types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.project)
          encoding (string): If the output format is **csv** then **encoding** filter should be one of
          generateInvoices (boolean): Generate invoices for all projects found
          allDatas (boolean): Retrieve project with PostProduction datas (true by default)
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: reference | company.name
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/apps/post-production/projects", params=params, validate=validate))

    async def update_post_production_projects_by_id(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/post-production/projects/{id}
        
        Update project data related to app's PostProduction
        
        Request body schema: appsPostProductionProjectsBody-put
        """
        return Document(await self._client.request("PUT", f"/apps/post-production/projects/{id}", json=body, params=params, validate=validate))

    async def post_production_resources_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/post-production/resources/{id}
        
        Get app's PostProduction resource configuration data
        """
        return Document(await self._client.request("GET", f"/apps/post-production/resources/{id}", params=params, validate=validate))

    async def update_post_production_resources_by_id(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/post-production/resources/{id}
        
        Update resource configuration data related to app's PostProduction
        
        Request body schema: appsPostproductionResourcesBody-put
        """
        return Document(await self._client.request("PUT", f"/apps/post-production/resources/{id}", json=body, params=params, validate=validate))

    async def quotations_quotations(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/quotations/quotations
        
        Search quotations
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/apps/quotations/quotations.csv?keywords=COMP100*
        
        Query params:
          keywords (string): If `keywords = QUOT**ID1** AO**ID2** CCON**ID3** CSOC**ID4**` then opportunities
          period (string): * `created` : Quotations created between `startDate` and `endDate` are filtered
          periodDynamic (string): * `today` : Quotations filtered according to the grid for today's period
          periodDynamicParameters (string): Filter parameters of dynamic period. Used when periodDynamic is "lastCustomPeriod" or "nextCustomPeriod"
          startDate (string): Start date
          endDate (string): End date
          quotationStates (integer, repeatable): List of quotation states `id` to filter (described by /api/rest/application/dictionary/setting.state.quotation)
          opportunityTypes (string, repeatable): List of opportunity types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.project)
          onlyVisible (boolean, default True): The user has to have the global right `showGroupe` set to `true` or call this api into mode `god`.
          encoding (string): If the output format is **csv** then **encoding** filter should be one of
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: date | reference | opportunity.title | company.name | state | validationDate | turnoverInvoicedExcludingTax | turnoverInvoicedIncludingTax | mainManager.lastName
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/apps/quotations/quotations", params=params, validate=validate))

    async def post_quotations_quotations(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /apps/quotations/quotations
        
        Create a quotation
        
        Request body schema: appsQuotationsQuotationsBody-post
        """
        return Document(await self._client.request("POST", "/apps/quotations/quotations", json=body, params=params, validate=validate))

    async def quotations_quotations_default(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/quotations/quotations/default
        
        Get empty quotation's default information data
        
        Query params:
          opportunity (integer): Opportunity's `id` on which quotation depends
          positioning (integer): Positioning's `id` on which quotation depends
        """
        return Document(await self._client.request("GET", "/apps/quotations/quotations/default", params=params, validate=validate))

    async def delete_quotations_quotations_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /apps/quotations/quotations/{id}
        
        Delete the quotation
        """
        return Document(await self._client.request("DELETE", f"/apps/quotations/quotations/{id}", params=params, validate=validate))

    async def quotations_quotations_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/quotations/quotations/{id}
        
        Get quotation's basic data
        """
        return Document(await self._client.request("GET", f"/apps/quotations/quotations/{id}", params=params, validate=validate))

    async def update_quotations_quotations_by_id(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/quotations/quotations/{id}
        
        Update basic data related to a quotation
        
        Request body schema: appsQuotationsQuotationsBody-put
        """
        return Document(await self._client.request("PUT", f"/apps/quotations/quotations/{id}", json=body, params=params, validate=validate))

    async def quotations_quotations_by_id_download(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/quotations/quotations/{id}/download
        
        Get quotation formatted file content
        
        Query params:
          language (string, one of: fr | en | es): Language used for the file content
        """
        return Document(await self._client.request("GET", f"/apps/quotations/quotations/{id}/download", params=params, validate=validate))

    async def quotations_quotations_by_id_rights(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/quotations/quotations/{id}/rights
        
        Get quotation's rights
        
        Query params:
          opportunity (integer): Opportunity's `id` on which quotation depends
          positioning (integer): Positioning's `id` on which quotation depends
        """
        return Document(await self._client.request("GET", f"/apps/quotations/quotations/{id}/rights", params=params, validate=validate))

    async def quotations_quotations_by_id_send(self, id, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /apps/quotations/quotations/{id}/send
        
        Send invoice by mail
        """
        return Document(await self._client.request("POST", f"/apps/quotations/quotations/{id}/send", json=body, params=params, validate=validate))

    async def quotations_quotations_by_id_tasks(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/quotations/quotations/{id}/tasks
        
        Get quotation's tasks
        """
        return Document(await self._client.request("GET", f"/apps/quotations/quotations/{id}/tasks", params=params, validate=validate))

    async def resource_planner_projects_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/resource-planner/projects/{id}
        
        Get project's planned times data
        """
        return Document(await self._client.request("GET", f"/apps/resource-planner/projects/{id}", params=params, validate=validate))

    async def update_resource_planner_projects_by_id(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/resource-planner/projects/{id}
        
        Update project data related to app's ResourcePlanner
        
        Request body schema: appsResourcePlannerProjectsBody-put
        """
        return Document(await self._client.request("PUT", f"/apps/resource-planner/projects/{id}", json=body, params=params, validate=validate))

    async def resource_planner_projects_by_id_rights(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/resource-planner/projects/{id}/rights
        
        Get resourceplanner project's rights
        """
        return Document(await self._client.request("GET", f"/apps/resource-planner/projects/{id}/rights", params=params, validate=validate))

    async def resource_planner_resources_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/resource-planner/resources/{id}
        
        Get resource's planned times data
        """
        return Document(await self._client.request("GET", f"/apps/resource-planner/resources/{id}", params=params, validate=validate))

    async def update_resource_planner_resources_by_id(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/resource-planner/resources/{id}
        
        Update resource data related to app's ResourcePlanner
        
        Request body schema: appsResourcePlannerResourcesBody-put
        """
        return Document(await self._client.request("PUT", f"/apps/resource-planner/resources/{id}", json=body, params=params, validate=validate))

    async def resource_planner_resources_by_id_rights(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/resource-planner/resources/{id}/rights
        
        Get resourceplanner resource's rights
        """
        return Document(await self._client.request("GET", f"/apps/resource-planner/resources/{id}/rights", params=params, validate=validate))

    async def saas_editor_configuration(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/saas-editor/configuration
        
        Get app's SaasEditor configuration data
        """
        return Document(await self._client.request("GET", "/apps/saas-editor/configuration", params=params, validate=validate))

    async def update_saas_editor_configuration(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/saas-editor/configuration
        
        Update configuration data related to SaasEditor's customer
        
        Request body schema: appsSaasEditorConfigurationBody-put
        """
        return Document(await self._client.request("PUT", "/apps/saas-editor/configuration", json=body, params=params, validate=validate))

    async def saas_editor_reporting(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/saas-editor/reporting
        
        Search reporting
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/apps/saas-editor/reporting.csv?product=1&startDate=2022-01-01
        
        Query params:
          startDate (string, REQUIRED): Start date
          products (integer, repeatable): List of products `id`
          numberOfPeriod (integer)
          period (string, default annual): * `monthly` : Reporting are returned following 12 or numberOfPeriod months between `startDate`
          scorecards (string, repeatable): List of scorecard to filter.
          encoding (string): If the output format is **csv** then **encoding** filter should be one of
        """
        return Document(await self._client.request("GET", "/apps/saas-editor/reporting", params=params, validate=validate))

    async def sepa_companies_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/sepa/companies/{id}
        
        Get company's specific data
        """
        return Document(await self._client.request("GET", f"/apps/sepa/companies/{id}", params=params, validate=validate))

    async def update_sepa_companies_by_id(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/sepa/companies/{id}
        
        Update specific data related to a company
        
        Request body schema: appsSepaCompaniesBody-put
        """
        return Document(await self._client.request("PUT", f"/apps/sepa/companies/{id}", json=body, params=params, validate=validate))

    async def sepa_configuration(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/sepa/configuration
        
        Get app's Sepa configuration data
        """
        return Document(await self._client.request("GET", "/apps/sepa/configuration", params=params, validate=validate))

    async def update_sepa_configuration(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/sepa/configuration
        
        Update configuration data related to Sepa's customer
        
        Request body schema: appsSepaConfigurationBody-put
        """
        return Document(await self._client.request("PUT", "/apps/sepa/configuration", json=body, params=params, validate=validate))

    async def sepa_contracts(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/sepa/contracts
        
        Search contracts
        
        _You can specify the output format by appending to the url **.xml** or **.csv**_
        *Example : {BASE_URL}/api/apps/sepa/contracts.xml*
        
        Query params:
          keywords (string): If `keywords = CTR**ID1** COMP**ID2**` then contracts
          month (string): month
          resourceTypes (integer, repeatable): List of resource types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.resource)
          resourceStates (integer, repeatable): List of resource states `id` to filter (described by /api/rest/application/dictionary/setting.state.resource)
          typeOfBanksDetails (string, one of: sepaContractsWithBankDetails | sepaContractsWithoutBankDetails | boondmanagerContracts, default sepaContractsWithoutBankDetails)
          extractType (string, repeatable, one of: salary | expenses | advantages): Used only if extraction is following format xml
          extractDate (string)
          extractPaid (boolean, default False)
          encoding (string): If the output format is **csv** then **encoding** filter should be one of
          groupPayments (boolean): For extraction, whether the payments should be grouped or not
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: typeOf | dependsOn.lastName | expensesReports.state | expensesReports.paid
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/apps/sepa/contracts", params=params, validate=validate))

    async def sepa_contracts_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/sepa/contracts/{id}
        
        Get contract's specific data
        """
        return Document(await self._client.request("GET", f"/apps/sepa/contracts/{id}", params=params, validate=validate))

    async def update_sepa_contracts_by_id(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/sepa/contracts/{id}
        
        Update specific data related to a contract
        
        Request body schema: appsSepaContractsBody-put
        """
        return Document(await self._client.request("PUT", f"/apps/sepa/contracts/{id}", json=body, params=params, validate=validate))

    async def sepa_import__contracts(self, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /apps/sepa/import/contracts
        
        Import contracts bank detail
        """
        return Document(await self._client.request("POST", "/apps/sepa/import/contracts", json=body, params=params, validate=validate))

    async def sepa_import__orders(self, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /apps/sepa/import/orders
        
        Import contracts bank detail
        """
        return Document(await self._client.request("POST", "/apps/sepa/import/orders", json=body, params=params, validate=validate))

    async def sepa_import__purchases(self, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /apps/sepa/import/purchases
        
        Import contracts bank detail
        """
        return Document(await self._client.request("POST", "/apps/sepa/import/purchases", json=body, params=params, validate=validate))

    async def sepa_import__transfers(self, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /apps/sepa/import/transfers
        
        Import contracts transfers
        """
        return Document(await self._client.request("POST", "/apps/sepa/import/transfers", json=body, params=params, validate=validate))

    async def sepa_invoices(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/sepa/invoices
        
        Search invoices or credit notes
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/apps/sepa/invoices.csv*
        
        Query params:
          month (string, REQUIRED): month
          creditNote (boolean, REQUIRED): If `true` returns only credit notes, if `false` returns only bills
          keywords (string): If `keywords = FACT**ID1** BDC**ID2** PRJ**ID3** CCON**ID4** CSOC**ID5**` then invoices
          projectTypes (integer, repeatable): List of project types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.project)
          states (integer, repeatable): List of invoice states `id` to filter (described by /api/rest/application/dictionary/setting.state.invoice)
          extractDate (string)
          extractState (string): Payment state `id` to set after extraction or empty string if no set to do
          extractSequenceTypeOfFirstToRecurrent (boolean)
          groupPayments (boolean): For extraction, whether the payments should be grouped or not
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: turnoverInvoicedIncludingTax | date | reference | turnoverExvoicedIncludingTax | expectedPaymentDate | state | order.number | order.project.reference | order.project.company.name
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/apps/sepa/invoices", params=params, validate=validate))

    async def sepa_orders(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/sepa/orders
        
        Search orders
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/orders.csv?keywords=BDC1*
        
        Query params:
          keywords (string): If `keywords = BDC**ID1** PRJ**ID2** CCON**ID3** CSOC**ID4**` then orders
          paymentMethods (integer, repeatable): List of payment methods `id` to filter (described by /api/rest/application/dictionary/setting.paymentMethod)
          states (integer, repeatable): List of order states `id` to filter (described by /api/rest/application/dictionary/setting.state.order)
          typeOfBanksDetails (string, one of: sepaOrdersWithBankDetailsAndUniqueReferenceMandate | sepaOrdersWithoutBankDetailsOrUniqueReferenceMandate | boondmanagerOrders, default sepaOrdersWithoutBankDetailsOrUniqueReferenceMandate)
          encoding (string): If the output format is **csv** then **encoding** filter should be one of
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: date | number | state | project.reference | project.company.name
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/apps/sepa/orders", params=params, validate=validate))

    async def sepa_orders_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/sepa/orders/{id}
        
        Get order's specific data
        """
        return Document(await self._client.request("GET", f"/apps/sepa/orders/{id}", params=params, validate=validate))

    async def update_sepa_orders_by_id(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/sepa/orders/{id}
        
        Update specific data related to an order
        
        Request body schema: appsSepaOrdersBody-put
        """
        return Document(await self._client.request("PUT", f"/apps/sepa/orders/{id}", json=body, params=params, validate=validate))

    async def sepa_payments(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/sepa/payments
        
        Search payments
        
        _You can specify the output format by appending to the url **.xml**_
        *Example : {BASE_URL}/api/apps/sepa/payments.xml*
        
        Query params:
          month (string, REQUIRED): month
          keywords (string): If `keywords = ACH**ID1** CCON**ID2** CSOC**ID3** PRJ**ID4** COMP**ID5**` then payments
          subscriptionTypes (integer, repeatable): List of subscription types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.subscription)
          paymentStates (integer, repeatable): List of payment states `id` to filter (described by /api/rest/application/dictionary/setting.state.payment)
          extractDate (string)
          extractState (string): Payment state `id` to set after extraction or empty string if no set to do
          groupPayments (boolean): For extraction, whether the payments should be grouped or not
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: expectedDate | performedDate | state | date | purchase.title | project.reference | purchase.company.name
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/apps/sepa/payments", params=params, validate=validate))

    async def sepa_purchases(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/sepa/purchases
        
        Search purchases
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/purchases.csv?keywords=ACH1*
        
        Query params:
          keywords (string): If `keywords = ACH**ID1** CCON**ID2** CSOC**ID3** PRJ**ID4** COMP**ID5**` then purchases
          purchaseStates (integer, repeatable): List of purchase states `id` to filter (described by /api/rest/application/dictionary/setting.state.purchase)
          paymentMethods (integer, repeatable): List of payment methods `id` to filter (described by /api/rest/application/dictionary/setting.paymentMethod)
          typeOfBanksDetails (string, one of: sepaPurchasesWithBankDetails | sepaPurchasesWithoutBankDetails | boondmanagerPurchases, default sepaPurchasesWithoutBankDetails)
          encoding (string): If the output format is **csv** then **encoding** filter should be one of
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: title | state | date | project.reference | company.name
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/apps/sepa/purchases", params=params, validate=validate))

    async def sepa_purchases_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/sepa/purchases/{id}
        
        Get purchase's specific data
        """
        return Document(await self._client.request("GET", f"/apps/sepa/purchases/{id}", params=params, validate=validate))

    async def update_sepa_purchases_by_id(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/sepa/purchases/{id}
        
        Update specific data related to a purchase
        
        Request body schema: appsSepaPurchasesBody-put
        """
        return Document(await self._client.request("PUT", f"/apps/sepa/purchases/{id}", json=body, params=params, validate=validate))

    async def special_reporting_reporting(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/special-reporting/reporting
        
        Generate reporting file
        
        _You have to set the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/apps/special-reporting/reporting.csv*
        
        Query params:
          month (string, REQUIRED): month
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
        """
        return Document(await self._client.request("GET", "/apps/special-reporting/reporting", params=params, validate=validate))

    async def survey_configuration(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/survey/configuration
        
        Get app's Survey configuration data
        """
        return Document(await self._client.request("GET", "/apps/survey/configuration", params=params, validate=validate))

    async def update_survey_configuration(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/survey/configuration
        
        Update configuration data related to Survey's customer
        
        Request body schema: appsSurveyConfigurationBody-put
        """
        return Document(await self._client.request("PUT", "/apps/survey/configuration", json=body, params=params, validate=validate))

    async def survey_enquiries_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/survey/enquiries/{id}
        
        Get enquiry's basic data
        """
        return Document(await self._client.request("GET", f"/apps/survey/enquiries/{id}", params=params, validate=validate))

    async def update_survey_enquiries_by_id(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /apps/survey/enquiries/{id}
        
        Update basic data related to an enquiry
        
        Request body schema: appsSurveyEnquiriesBody-put
        """
        return Document(await self._client.request("PUT", f"/apps/survey/enquiries/{id}", json=body, params=params, validate=validate))

    async def survey_enquiries_by_id_rights(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/survey/enquiries/{id}/rights
        
        Get enquiry's rights
        """
        return Document(await self._client.request("GET", f"/apps/survey/enquiries/{id}/rights", params=params, validate=validate))

    async def survey_satisfaction_indicators(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/survey/satisfaction-indicators
        
        Search satisfaction indicators
        
        Query params:
          keywords (string): If `keywords = COMP**ID1**` then
          startDate (string): Start date
          endDate (string): End date
          onlyMySurveys (boolean)
          evaluations (string, repeatable): * `noEvaluation` : Satisfactions with no evaluation are filtered
          encoding (string): If the output format is **csv** then **encoding** filter should be one of
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
        """
        return Document(await self._client.request("GET", "/apps/survey/satisfaction-indicators", params=params, validate=validate))

    async def survey_satisfactions(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/survey/satisfactions
        
        Search satisfactions
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/apps/survey/satisfactions.csv?keywords=COMP100*
        
        Query params:
          keywords (string): If `keywords = COMP**ID1**` then
          startDate (string): Start date
          endDate (string): End date
          onlyMySurveys (boolean)
          evaluations (string, repeatable): * `noEvaluation` : Satisfactions with no evaluation are filtered
          encoding (string): If the output format is **csv** then **encoding** filter should be one of
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
        """
        return Document(await self._client.request("GET", "/apps/survey/satisfactions", params=params, validate=validate))

    async def install(self, app_code, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /apps/{appCode}/install
        
        Install App
        """
        return Document(await self._client.request("POST", f"/apps/{app_code}/install", json=body, params=params, validate=validate))

    async def delete_uninstall(self, app_code, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /apps/{appCode}/uninstall
        
        Uninstall App
        """
        return Document(await self._client.request("DELETE", f"/apps/{app_code}/uninstall", params=params, validate=validate))

    async def entities(self, app_id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/{appId}/entities
        
        Search app entities (Only for moduleNoCode's app)
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/apps/100000/entities.csv?keywords=APPENTITY100*
        
        Query params:
          keywords (string): If `keywords = APPENTITY**ID1** CAND**ID2** COMP**ID3** CCON**ID4** CSOC**ID5** PROD**ID6** AO**ID7** ACH**ID8** BDC**ID9** FACT**ID10** PRJ**ID11**` then app entities
          period (string): * `created` : App entities created between `startDate` and `endDate` are filtered
          periodDynamic (string): * `today` : Candidates filtered according to the grid for today's period
          periodDynamicParameters (string): Filter parameters of dynamic period. Used when periodDynamic is "lastCustomPeriod" or "nextCustomPeriod"
          startDate (string): Start date
          endDate (string): End date
          flags (integer, repeatable): Candidates attached to this flag whom flag's unique identifier = integer are filtered
          appEntityStates (integer, repeatable): List of app entity states `id`
          appEntityTypes (integer, repeatable): List of app entity types `id`
          appEntityFields (string, repeatable): List of app entity responses filtered by `<fieldId>:<responseValue>` and with html characters encoded
          visibility (integer, repeatable): List of visibility's `id` (0 or 1)
          onlyMyProfile (boolean, default False)
          onlyVisible (boolean, default True): The user has to have the global right `showGroupe` set to `true` or call this api into mode `god`.
          encoding (string): If the output format is **csv** then **encoding** filter should be one of
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: id | mainManager.lastName | agency.name | pole.name | updateDate | creationDate | state | typeOf | visibility | globalValidation | guestsValidation | managersValidation | managerValidator.lastName | guestValidator.lastName | dependsOn.value | field.<integer>
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/apps/{app_id}/entities", params=params, validate=validate))

    async def post_entities(self, app_id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /apps/{appId}/entities
        
        Create an app entity (Only for moduleNoCode's app)
        
        Query params:
          candidate (integer): Candidate's `id` on which app entity depends
          company (integer): Company's `id` on which app entity depends
          contact (integer): Contact's `id` on which app entity depends
          invoice (integer): Invoice's `id` on which app entity depends
          opportunity (integer): Opportunity's `id` on which app entity depends
          order (integer): Order's `id` on which app entity depends
          product (integer): Product's `id` on which app entity depends
          project (integer): Project's `id` on which app entity depends
          purchase (integer): Purchase's `id` on which app entity depends
          resource (integer): Resource's `id` on which app entity depends
        
        Request body schema: appsEntitiesBody-post
        """
        return Document(await self._client.request("POST", f"/apps/{app_id}/entities", json=body, params=params, validate=validate))

    async def entities_default(self, app_id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/{appId}/entities/default
        
        Get empty app entity's default data
        
        Query params:
          candidate (integer): Candidate's `id` on which app entity depends
          company (integer): Company's `id` on which app entity depends
          contact (integer): Contact's `id` on which app entity depends
          invoice (integer): Invoice's `id` on which app entity depends
          opportunity (integer): Opportunity's `id` on which app entity depends
          order (integer): Order's `id` on which app entity depends
          product (integer): Product's `id` on which app entity depends
          project (integer): Project's `id` on which app entity depends
          purchase (integer): Purchase's `id` on which app entity depends
          resource (integer): Resource's `id` on which app entity depends
        """
        return Document(await self._client.request("GET", f"/apps/{app_id}/entities/default", params=params, validate=validate))

    async def entities_dependson(self, app_id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/{appId}/entities/dependson
        
        Get app entity's from dependsOn, or create it if does not exist (Only for sectionNoCode's app)
        
        Query params:
          candidate (integer): Candidate's `id` on which app entity depends
          company (integer): Company's `id` on which app entity depends
          contact (integer): Contact's `id` on which app entity depends
          invoice (integer): Invoice's `id` on which app entity depends
          opportunity (integer): Opportunity's `id` on which app entity depends
          order (integer): Order's `id` on which app entity depends
          product (integer): Product's `id` on which app entity depends
          project (integer): Project's `id` on which app entity depends
          purchase (integer): Purchase's `id` on which app entity depends
          resource (integer): Resource's `id` on which app entity depends
        """
        return Document(await self._client.request("GET", f"/apps/{app_id}/entities/dependson", params=params, validate=validate))

    async def delete_entities_by_id(self, app_id, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /apps/{appId}/entities/{id}
        
        Delete the app entity
        """
        return Document(await self._client.request("DELETE", f"/apps/{app_id}/entities/{id}", params=params, validate=validate))

    async def entities_by_id(self, app_id, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/{appId}/entities/{id}
        
        Get app entity's basic data
        """
        return Document(await self._client.request("GET", f"/apps/{app_id}/entities/{id}", params=params, validate=validate))

    async def entities_by_id_attached_flags(self, app_id, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/{appId}/entities/{id}/attached-flags
        
        Get app entity's attached flags
        """
        return Document(await self._client.request("GET", f"/apps/{app_id}/entities/{id}/attached-flags", params=params, validate=validate))

    async def entities_by_id_rights(self, app_id, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/{appId}/entities/{id}/rights
        
        Get app entity's rights
        """
        return Document(await self._client.request("GET", f"/apps/{app_id}/entities/{id}/rights", params=params, validate=validate))

    async def entities_by_id_tasks(self, app_id, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/{appId}/entities/{id}/tasks
        
        Get app entity's tasks
        """
        return Document(await self._client.request("GET", f"/apps/{app_id}/entities/{id}/tasks", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /apps/{id}
        
        Get app's basic data
        """
        return Document(await self._client.request("GET", f"/apps/{id}", params=params, validate=validate))



class AttachedFlagsAPI:
    """Endpoints under /attached-flags."""

    def __init__(self, client) -> None:
        self._client = client

    async def delete_many(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /attached-flags
        
        Delete an attached flag
        
        Query params:
          flag (integer, REQUIRED): Flag's `id` on which attached flag depends
          company (integer): Company's `id` on which attached flag depends
          opportunity (integer): Opportunity's `id` on which attached flag depends
          project (integer): Project's `id` on which attached flag depends
          order (integer): Order's `id` on which attached flag depends
          product (integer): Product's `id` on which attached flag depends
          purchase (integer): Purchase's `id` on which attached flag depends
          action (integer): Action's `id` on which attached flag depends
          resource (integer): Resource's `id` on which attached flag depends
          candidate (integer): Candidate's `id` on which attached flag depends
          positioning (integer): Positioning's `id` on which attached flag depends
          contact (integer): Contact's `id` on which attached flag depends
          invoice (integer): Invoice's `id` on which attached flag depends
          appEntity (integer): App entity's `id` on which attached flag depends
        """
        return Document(await self._client.request("DELETE", "/attached-flags", params=params, validate=validate))

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /attached-flags
        
        Create an attached flag
        
        Request body schema: attachedFlagsBody-post
        """
        return Document(await self._client.request("POST", "/attached-flags", json=body, params=params, validate=validate))



class BankingAccountsAPI:
    """Endpoints under /banking-accounts."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /banking-accounts
        
        Search banking accounts
        
        Query params:
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
        """
        return Document(await self._client.request("GET", "/banking-accounts", params=params, validate=validate))



class BankingTransactionsAPI:
    """Endpoints under /banking-transactions."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /banking-transactions
        
        Search banking transactions
        
        Query params:
          keywords (string): If `keywords = BNKTRS**ID1** BNKTRS**ID2**` then transactions
          keywordsType (string, default default): * `default` : Transactions are filtered following `keywords` found transaction description and transaction amount
          states (integer, repeatable): List of banking transactions states `id` to filter
          perimeterAgencies (integer, repeatable): Results whom banking transaction account belong to agency's unique identifier are filtered
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          period (string): * `created` : Transaction created between `startDate` and `endDate` are filtered
          periodDynamic (string): * `today` : Transactions filtered according to the grid for today's period
          periodDynamicParameters (string): Filter parameters of dynamic period. Used when periodDynamic is "lastCustomPeriod" or "nextCustomPeriod"
          startDate (string): Start date
          endDate (string): End date
          bankingAccounts (integer, repeatable): Transaction attached to this banking account whom account's unique identifier = integer are filtered
          columns (string, repeatable): List of columns
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: amount | description | date |state
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/banking-transactions", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /banking-transactions/{id}
        
        get the banking transaction
        """
        return Document(await self._client.request("GET", f"/banking-transactions/{id}", params=params, validate=validate))

    async def update(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /banking-transactions/{id}
        
        Update the banking transaction
        
        Request body schema: bankingTransactionsBody-put
        """
        return Document(await self._client.request("PUT", f"/banking-transactions/{id}", json=body, params=params, validate=validate))



class BillingDeliveriesPurchasesBalanceAPI:
    """Endpoints under /billing-deliveries-purchases-balance."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /billing-deliveries-purchases-balance
        
        Search deliveries or purchases with a billing balance
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/billing-deliveries-purchases-balance.csv?keywords=PRJ1*
        
        Query params:
          keywords (string): If `keywords = PRJ**ID1** CCON**ID2** CSOC**ID3**` then deliveries or purchases
          projectTypes (integer, repeatable): List of project types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.project)
          projectStates (integer, repeatable): List of project states `id` to filter (described by /api/rest/application/dictionary/setting.state.project)
          period (string): * `inProgress` : Deliveries or purchases in progress between `startDate` and `endDate` are filtered
          periodDynamic (string): * `today` : Deliveries or purchases filtered according to the grid for today's period
          periodDynamicParameters (string): Filter parameters of dynamic period. Used when periodDynamic is "lastCustomPeriod" or "nextCustomPeriod"
          startDate (string): Start date
          endDate (string): End date
          flags (integer, repeatable): Deliveries or purchases attached to this flag whom flag's unique identifier = integer are filtered
          columns (string, repeatable): List of columns
          encoding (string): If the output format is **csv** then **encoding** filter should be one of
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: startDate | endDate | id | project.creationDate | project.reference | project.state | order.number | project.company.name | mainManager.lastName | intermediaryCompany.name
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/billing-deliveries-purchases-balance", params=params, validate=validate))



class BillingDetailsAPI:
    """Endpoints under /billing-details."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /billing-details
        
        Search billing details
        
        Query params:
          keywords (string): Full-text search on name, contact and company name.
          companies (integer, repeatable): List of companies `id` on which billing detail depends
          companyStates (integer, repeatable): List of company states to filter
          state (boolean): Filter by billing detail state
          orderSendingModes (integer, repeatable): List of sending modes to filter
          columns (string, repeatable): List of columns to return
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: name, company.name, town, sendingMode, invalid
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/billing-details", params=params, validate=validate))

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /billing-details
        
        Create a billing detail
        
        Request body schema: billingDetailsBody-post
        """
        return Document(await self._client.request("POST", "/billing-details", json=body, params=params, validate=validate))

    async def analyze(self, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /billing-details/analyze
        
        Analyze billing details to validate VAT numbers and registration numbers.
        The analysis is performed asynchronously via a hook consumer.
        The `invalid` and `invalidType` fields of each billing detail will be updated based on the validation results.
        
        Query params:
          keywords (string): Full-text search on name, contact and company name.
          companies (integer, repeatable): List of companies `id` on which billing detail depends
          companyStates (integer, repeatable): List of company states to filter
          state (boolean): Filter by billing detail state
          orderSendingModes (integer, repeatable): List of sending modes to filter
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
        """
        return Document(await self._client.request("POST", "/billing-details/analyze", json=body, params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /billing-details/{id}
        
        Delete the billing detail
        """
        return Document(await self._client.request("DELETE", f"/billing-details/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /billing-details/{id}
        
        Get billing detail's data
        """
        return Document(await self._client.request("GET", f"/billing-details/{id}", params=params, validate=validate))

    async def update(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /billing-details/{id}
        
        Update billing detail's data
        
        Request body schema: billingDetailsBody-put
        """
        return Document(await self._client.request("PUT", f"/billing-details/{id}", json=body, params=params, validate=validate))



class BillingMonthlyBalanceAPI:
    """Endpoints under /billing-monthly-balance."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /billing-monthly-balance
        
        Search orders with a monthly billing balance
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/billing-monthly-balance.csv?keywords=BDC1*
        
        Query params:
          startMonth (string, REQUIRED): Start month
          keywords (string): If `keywords = BDC**ID1** PRJ**ID2** CCON**ID3** CSOC**ID4**` then orders
          projectTypes (integer, repeatable): List of project types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.project)
          orderPaymentMethods (integer, repeatable): List of payment methods `id` to filter (described by /api/rest/application/dictionary/setting.paymentMethod)
          orderSendingModes (integer, repeatable): List of sending mode `id` to filter (described by /api/rest/application/dictionary/setting.sendingMode)
          orderStates (integer, repeatable): List of order states `id` to filter (described by /api/rest/application/dictionary/setting.state.order)
          flags (integer, repeatable): Orders attached to this flag whom flag's unique identifier = integer are filtered
          columns (string, repeatable): List of columns
          encoding (string): If the output format is **csv** then **encoding** filter should be one of
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: date | number | invoice.state | numberOfInvoices | invoice.reference | project.reference | project.company.name | mainManager.lastName | intermediaryCompany.name
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/billing-monthly-balance", params=params, validate=validate))



class BillingProjectsBalanceAPI:
    """Endpoints under /billing-projects-balance."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /billing-projects-balance
        
        Search projects with a billing balance
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/billing-projects-balance.csv?keywords=PRJ1*
        
        Query params:
          keywords (string): If `keywords = PRJ**ID2** CCON**ID3** CSOC**ID4**` then projects
          projectTypes (integer, repeatable): List of project types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.project)
          projectStates (integer, repeatable): List of project states `id` to filter (described by /api/rest/application/dictionary/setting.state.project)
          period (string): * `created` : Projects created between `startDate` and `endDate` are filtered
          periodDynamic (string): * `today` : Projects filtered according to the grid for today's period
          periodDynamicParameters (string): Filter parameters of dynamic period. Used when periodDynamic is "lastCustomPeriod" or "nextCustomPeriod"
          startDate (string): Start date
          endDate (string): End date
          flags (integer, repeatable): Projects attached to this flag whom flag's unique identifier = integer are filtered
          columns (string, repeatable): List of columns
          encoding (string): If the output format is **csv** then **encoding** filter should be one of
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: creationDate | reference | state | numberOfOrders | company.name | mainManager.lastName | intermediaryCompany.name
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/billing-projects-balance", params=params, validate=validate))



class BillingSchedulesBalanceAPI:
    """Endpoints under /billing-schedules-balance."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /billing-schedules-balance
        
        Search schedules with a billing balance
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/billing-schedules-balance.csv?keywords=BDC1*
        
        Query params:
          keywords (string): If `keywords = BDC**ID1** PRJ**ID2** CCON**ID3** CSOC**ID4**` then schedules
          projectTypes (integer, repeatable): List of project types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.project)
          orderPaymentMethods (integer, repeatable): List of payment methods `id` to filter (described by /api/rest/application/dictionary/setting.paymentMethod)
          orderStates (integer, repeatable): List of orders states `id` to filter (described by /api/rest/application/dictionary/setting.state.order)
          period (string): * `paymentDate` : Schedules whose paymentDate is between `startDate` and `endDate` are filtered
          periodDynamic (string): * `today` : Projects filtered according to the grid for today's period
          periodDynamicParameters (string): Filter parameters of dynamic period. Used when periodDynamic is "lastCustomPeriod" or "nextCustomPeriod"
          startDate (string): Start date
          endDate (string): End date
          flags (integer, repeatable): Orders attached to this flag whom flag's unique identifier = integer are filtered
          columns (string, repeatable): List of columns
          encoding (string): If the output format is **csv** then **encoding** filter should be one of
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: date | order.number | invoice.state | invoice.reference | numberOfInvoices | order.project.reference | turnoverInvoicedExcludingTax | turnoverTermOfPaymentExcludingTax | deltaInvoicedExcludingTax | order.project.company.name | order.mainManager.lastName | intermediaryCompany.name
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/billing-schedules-balance", params=params, validate=validate))



class BoondmanagerContractsAPI:
    """Endpoints under /boondmanager-contracts."""

    def __init__(self, client) -> None:
        self._client = client

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /boondmanager-contracts/{id}
        
        Get boondmanager contract's basic data
        """
        return Document(await self._client.request("GET", f"/boondmanager-contracts/{id}", params=params, validate=validate))

    async def update(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /boondmanager-contracts/{id}
        
        Update basic data related to a contract
        
        Request body schema: boondmanagerContractsBody-put
        """
        return Document(await self._client.request("PUT", f"/boondmanager-contracts/{id}", json=body, params=params, validate=validate))



class BusinessUnitsAPI:
    """Endpoints under /business-units."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /business-units
        
        Search business units
        """
        return Document(await self._client.request("GET", "/business-units", params=params, validate=validate))

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /business-units
        
        Create a business units
        
        Request body schema: businessUnitsBody-post
        """
        return Document(await self._client.request("POST", "/business-units", json=body, params=params, validate=validate))

    async def default(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /business-units/default
        
        Get empty business unit's default information data
        """
        return Document(await self._client.request("GET", "/business-units/default", params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /business-units/{id}
        
        Delete the business unit
        """
        return Document(await self._client.request("DELETE", f"/business-units/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /business-units/{id}
        
        Get business unit's basic data
        """
        return Document(await self._client.request("GET", f"/business-units/{id}", params=params, validate=validate))

    async def update(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /business-units/{id}
        
        Update basic data related to a business unit
        
        Request body schema: businessUnitsBody-put
        """
        return Document(await self._client.request("PUT", f"/business-units/{id}", json=body, params=params, validate=validate))



class CalendarsAPI:
    """Endpoints under /calendars."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /calendars
        
        Search calendars
        """
        return Document(await self._client.request("GET", "/calendars", params=params, validate=validate))

    async def default(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /calendars/default
        
        Get empty calendar's default data
        
        Query params:
          year (integer): Calendar's `year` between 2000 and 3000.
          iso (string): Calendar's `iso` following ISO 3166-1 alpha-2 or ISO 3166-1 alpha-3 or ISO 3166-2.
        """
        return Document(await self._client.request("GET", "/calendars/default", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /calendars/{id}
        
        Get calendar's basic data
        
        Query params:
          year (integer): Calendar's `year` between 2000 and 3000.
          iso (string): Calendar's `iso` following ISO 3166-1 alpha-2 or ISO 3166-1 alpha-3 or ISO 3166-2.
        """
        return Document(await self._client.request("GET", f"/calendars/{id}", params=params, validate=validate))

    async def update(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /calendars/{id}
        
        Update basic data related to a calendar
        
        Request body schema: calendarsBody-put
        """
        return Document(await self._client.request("PUT", f"/calendars/{id}", json=body, params=params, validate=validate))



class CandidatesAPI:
    """Endpoints under /candidates."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /candidates
        
        Search candidates
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/candidates.csv?keywords=CAND100*
        
        Query params:
          keywords (string): If `keywords = CAND**ID1** CAND**ID2**` then candidates
          keywordsType (string, default resumeTd): * `resumeTd` : Candidates are filtered following `keywords` found into their resumes and technical document
          returnMoreData (string, repeatable): Returns the following attributes or relationships, if specified and user is allowed to
          contractTypes (integer, repeatable): List of contract types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.contract)
          activityAreas (string, repeatable): List of activity areas `id` to filter (described by /api/rest/application/dictionary/setting.activityArea)
          expertiseAreas (string, repeatable): List of expertise areas `id` to filter (described by /api/rest/application/dictionary/setting.expertiseArea)
          tools (string, repeatable): List of tools `id` to filter (described by /api/rest/application/dictionary/setting.tool)
          mobilityAreas (string): List of mobility areas `id` to filter (described by /api/rest/application/dictionary/setting.mobilityArea)
          experiences (integer, repeatable): List of experiences `id` to filter (described by /api/rest/application/dictionary/setting.experience)
          trainings (string, repeatable): List of trainings `id` to filter (described by /api/rest/application/dictionary/setting.training)
          period (string): * `created` : Candidates created between `startDate` and `endDate` are filtered
          periodActions (integer, repeatable): List of actions `id` (../bddboondmanager/classes/TAB_ACTION.html#property_ACTION_TYPE described by /api/rest/application/dictionary/setting.action.candidate = integer
          periodDynamic (string): * `today` : Candidates filtered according to the grid for today's period
          periodDynamicParameters (string): Filter parameters of dynamic period. Used when periodDynamic is "lastCustomPeriod" or "nextCustomPeriod"
          startDate (string): Start date
          endDate (string): End date
          flags (integer, repeatable): Candidates attached to this flag whom flag's unique identifier = integer are filtered
          candidateStates (integer, repeatable): List of candidate states `id` to filter (described by /api/rest/application/dictionary/setting.state.candidate)
          perimeterManagersType (string): - `main`: The filter **perimeterManagers** is used only on the **Main Manager** of candidates
          availabilityTypes (integer, repeatable): List of availability `id` to filter (described by /api/rest/application/dictionary/setting.availability)
          languages (string, repeatable): List of languages spoken `id` to filter (described by /api/rest/application/dictionary/setting.languageSpoken)
          evaluations (string, repeatable): List of evaluations `id` to filter (described by /api/rest/application/dictionary/setting.evaluation)
          sources (string, repeatable): List of sources `id` to filter (described by /api/rest/application/dictionary/setting.source)
          candidateTypes (integer, repeatable): List of candidate types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.resource)
          columns (string, repeatable): List of columns
          onlyVisible (boolean, default True): The user has to have the global right `showGroupe` set to `true` or call this api into mode `god`.
          encoding (string): If the output format is **csv** then **encoding** filter should be one of
          providerCompanies (integer, repeatable): List of provider companies' `id` to filter
          coordinates (string): Geographic coordinates for proximity search, in the format `latitude,longitude`.
          location (string): Free-text address for geocoding-based proximity search (e.g. city name, address).
          geoDistance (integer): Search radius in kilometers for proximity search.
          appEntityFields (string, repeatable): List of app entity responses filtered by `<appId>_<fieldId>:<responseValue>` and with html characters encoded
          shields (string, repeatable): Filter candidates by their shield status (conditional fields completion level)
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: lastName | firstName | title | availability | availabilityType | numberOfActivePositionings | mainManager.lastName | updateDate | state | experience | creationDate | evaluation | hrManager.lastName | source | distance
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/candidates", params=params, validate=validate))

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /candidates
        
        Create a candidate
        
        Request body schema: candidatesBody-post
        """
        return Document(await self._client.request("POST", "/candidates", json=body, params=params, validate=validate))

    async def default(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /candidates/default
        
        Get empty candidate's default information data
        """
        return Document(await self._client.request("GET", "/candidates/default", params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /candidates/{id}
        
        Delete the candidate
        """
        return Document(await self._client.request("DELETE", f"/candidates/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /candidates/{id}
        
        Get candidate's basic data
        """
        return Document(await self._client.request("GET", f"/candidates/{id}", params=params, validate=validate))

    async def actions(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /candidates/{id}/actions
        
        Get candidate's actions
        
        Query params:
          actionTypes (integer, repeatable): List of action types `id`, related to the action's candidate, to filter (described by /api/rest/application/dictionary/setting.action.candidate)
          returnRelatedActions (boolean, default False): Return related parent and child/sibbling actions
          countTopTypes (integer): Count distinct types of actions and return values in meta
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: startDate | type | text
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/candidates/{id}/actions", params=params, validate=validate))

    async def administrative(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /candidates/{id}/administrative
        
        Get candidate's administrative data
        """
        return Document(await self._client.request("GET", f"/candidates/{id}/administrative", params=params, validate=validate))

    async def update_administrative(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /candidates/{id}/administrative
        
        Update administrative data related to a candidate
        
        Request body schema: candidatesAdministrativeBody-put
        """
        return Document(await self._client.request("PUT", f"/candidates/{id}/administrative", json=body, params=params, validate=validate))

    async def ai_matching(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /candidates/{id}/ai/matching
        
        Get list of opportunities matching this candidate
        """
        return Document(await self._client.request("GET", f"/candidates/{id}/ai/matching", params=params, validate=validate))

    async def ai_summary(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /candidates/{id}/ai/summary
        
        Get ai generated resource's summary
        """
        return Document(await self._client.request("GET", f"/candidates/{id}/ai/summary", params=params, validate=validate))

    async def attached_flags(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /candidates/{id}/attached-flags
        
        Get candidate's attached flags
        """
        return Document(await self._client.request("GET", f"/candidates/{id}/attached-flags", params=params, validate=validate))

    async def download(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /candidates/{id}/download
        
        Get resource's formatted file content
        
        Query params:
          language (string, one of: fr | en | es): Language used for the file content
          template (string): template ID
        """
        return Document(await self._client.request("GET", f"/candidates/{id}/download", params=params, validate=validate))

    async def information(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /candidates/{id}/information
        
        Get candidate's information data
        """
        return Document(await self._client.request("GET", f"/candidates/{id}/information", params=params, validate=validate))

    async def update_information(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /candidates/{id}/information
        
        Update information data related to a candidate
        
        Query params:
          importResumes (boolean): If `true` if you want to import candidate's resumes into the new resource when candidate is hired
          importFiles (boolean): If `true` if you want to import candidate's files into the new resource when candidate is hired
          importContractFiles (boolean): If `true` if you want to import candidate's cp,tract file into the new resource when candidate is hired
          importContract (boolean, default True): If `true` if you want to import candidate's contract into the updated resource when candidate is hired again
          importFields (string): List of resource's fields to update from candidate when candidate is hired again. Fields available
        
        Request body schema: candidatesInformationBody-put
        """
        return Document(await self._client.request("PUT", f"/candidates/{id}/information", json=body, params=params, validate=validate))

    async def merge(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /candidates/{id}/merge
        
        Test a merge or start a merge between two candidates.
        
        Request body schema: candidatesMergeBody-post
        """
        return Document(await self._client.request("POST", f"/candidates/{id}/merge", json=body, params=params, validate=validate))

    async def positionings(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /candidates/{id}/positionings
        
        Get candidate's positionings
        
        Query params:
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: updateDate | opportunity.title | opportunity.state | state | opportunity.company.name | opportunity.mainManager.lastName
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/candidates/{id}/positionings", params=params, validate=validate))

    async def rights(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /candidates/{id}/rights
        
        Get candidate's rights
        """
        return Document(await self._client.request("GET", f"/candidates/{id}/rights", params=params, validate=validate))

    async def tasks(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /candidates/{id}/tasks
        
        Get candidate's tasks
        """
        return Document(await self._client.request("GET", f"/candidates/{id}/tasks", params=params, validate=validate))

    async def technical_data(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /candidates/{id}/technical-data
        
        Get candidate's technical data
        
        Query params:
          language (string, one of: fr | en | es): Language used for the file content
        """
        return Document(await self._client.request("GET", f"/candidates/{id}/technical-data", params=params, validate=validate))

    async def update_technical_data(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /candidates/{id}/technical-data
        
        Update technical data related to a candidate
        
        Request body schema: candidatesTechnicalDataBody-put
        """
        return Document(await self._client.request("PUT", f"/candidates/{id}/technical-data", json=body, params=params, validate=validate))

    async def technical_datas(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /candidates/{id}/technical-datas
        
        Get candidate's technical datas
        
        Query params:
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: updateDate | isReferent
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/candidates/{id}/technical-datas", params=params, validate=validate))



class CompaniesAPI:
    """Endpoints under /companies."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /companies
        
        Search companies
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/companies.csv?keywords=CSOC100*
        
        Query params:
          keywords (string): If `keywords = CSOC**ID1** CSOC**ID2**` then companies
          keywordsType (string, default default): * `default` : Companies are filtered following `keywords` found into their name, town, country, expertiseArea and information
          returnMoreData (string, repeatable): Returns the following attributes or relationships, if specified and user is allowed to
          states (integer, repeatable): List of company states `id` to filter (described by /api/rest/application/dictionary/setting.state.company)
          expertiseAreas (string, repeatable): List of company expertise areas `id` to filter (described by /api/rest/application/dictionary/setting.expertiseArea)
          origins (string, repeatable): List of company origins `id` to filter (described by /api/rest/application/dictionary/setting.origin)
          period (string): * `created` : Companies created between `startDate` and `endDate` are filtered
          periodActions (integer, repeatable): List of actions `id` (../bddboondmanager/classes/TAB_ACTION.html#property_ACTION_TYPE described by /api/rest/application/dictionary/setting.action.contact = integer
          periodDynamic (string): * `today` : Companies filtered according to the grid for today's period
          periodDynamicParameters (string): Filter parameters of dynamic period. Used when periodDynamic is "lastCustomPeriod" or "nextCustomPeriod"
          startDate (string): Start date
          endDate (string): End date
          flags (integer, repeatable): Companies attached to this flag whom flag's unique identifier = integer are filtered
          columns (string, repeatable): List of columns
          encoding (string): If the output format is **csv** then **encoding** filter should be one of
          appEntityFields (string, repeatable): List of app entity responses filtered by `<appId>_<fieldId>:<responseValue>` and with html characters encoded
          influencers (integer, repeatable): List of company influencers `id` to filter
          shields (string, repeatable): Filter companies by their shield status (conditional fields completion level)
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: name | information | town | state | expertiseArea | mainManager.lastName | updateDate
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/companies", params=params, validate=validate))

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /companies
        
        Create a company
        
        Request body schema: companiesBody-post
        """
        return Document(await self._client.request("POST", "/companies", json=body, params=params, validate=validate))

    async def default(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /companies/default
        
        Get empty company's default information data
        """
        return Document(await self._client.request("GET", "/companies/default", params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /companies/{id}
        
        Delete the company
        """
        return Document(await self._client.request("DELETE", f"/companies/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /companies/{id}
        
        Get company's basic data
        """
        return Document(await self._client.request("GET", f"/companies/{id}", params=params, validate=validate))

    async def actions(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /companies/{id}/actions
        
        Get company's actions
        
        Query params:
          actionTypes (integer, repeatable): List of action types `id`, related to the action's entity (Contact, Company), to filter (described by /api/rest/application/dictionary/setting.action)
          searchSubsidiaries (boolean, default False): Search actions on subsidiaries
          returnRelatedActions (boolean, default False): Return related parent and child/sibbling actions
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: startDate | type | text
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/companies/{id}/actions", params=params, validate=validate))

    async def attached_flags(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /companies/{id}/attached-flags
        
        Get company's attached flags
        """
        return Document(await self._client.request("GET", f"/companies/{id}/attached-flags", params=params, validate=validate))

    async def contacts(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /companies/{id}/contacts
        
        Get company's contacts
        
        Query params:
          keywords (string): If `keywords = CCON**ID1**` then contacts
          states (integer, repeatable): List of contact states `id` to filter (described by /api/rest/application/dictionary/setting.state.contact)
          typesOf (integer, repeatable): List of contact typesOf `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.contact)
          sort (string, repeatable): Order by a given column
          order (string, one of: desc | asc, default asc): Order's type
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
        """
        return Document(await self._client.request("GET", f"/companies/{id}/contacts", params=params, validate=validate))

    async def information(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /companies/{id}/information
        
        Get company's information data
        """
        return Document(await self._client.request("GET", f"/companies/{id}/information", params=params, validate=validate))

    async def update_information(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /companies/{id}/information
        
        Update information data related to a company
        
        Query params:
          cascade (string): * `state` : All company's contacts are also updated following company's state
        
        Request body schema: companiesInformationBody-put
        """
        return Document(await self._client.request("PUT", f"/companies/{id}/information", json=body, params=params, validate=validate))

    async def invoices(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /companies/{id}/invoices
        
        Get company's invoices
        
        Query params:
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: turnoverIncludingTax | creationDate | turnoverExcludingTax | expectedPaymentDate | state | reference
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/companies/{id}/invoices", params=params, validate=validate))

    async def merge(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /companies/{id}/merge
        
        Test a merge or start a merge between two companies.
        
        Request body schema: companiesMergeBody-post
        """
        return Document(await self._client.request("POST", f"/companies/{id}/merge", json=body, params=params, validate=validate))

    async def opportunities(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /companies/{id}/opportunities
        
        Get company's opportunities
        
        Query params:
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: creationDate | title | state | totalWeightedTurnOverExcludingTax | mainManager.lastName
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/companies/{id}/opportunities", params=params, validate=validate))

    async def orders(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /companies/{id}/orders
        
        Get company's orders
        
        Query params:
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: creationDate | reference | state | customerAgreement | turnoverInvoicedExcludingTax | turnoverOrderedExcludingTax | deltaInvoicedExcludingTax
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/companies/{id}/orders", params=params, validate=validate))

    async def projects(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /companies/{id}/projects
        
        Get company's projects
        
        Query params:
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: startDate | endDate | reference | mainManager.lastName
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/companies/{id}/projects", params=params, validate=validate))

    async def provider_invoices(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /companies/{id}/provider-invoices
        
        Get company's provider invoices
        
        Query params:
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: invoiceDate | reference | state | amountExcludingTax | amountIncludingTax
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/companies/{id}/provider-invoices", params=params, validate=validate))

    async def purchases(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /companies/{id}/purchases
        
        Get company's purchases
        
        Query params:
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: title | state | creationDate | project.reference | mainManager.lastName
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/companies/{id}/purchases", params=params, validate=validate))

    async def rights(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /companies/{id}/rights
        
        Get company's rights
        """
        return Document(await self._client.request("GET", f"/companies/{id}/rights", params=params, validate=validate))

    async def settings(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /companies/{id}/settings
        
        Get company's setting data
        """
        return Document(await self._client.request("GET", f"/companies/{id}/settings", params=params, validate=validate))

    async def update_settings(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /companies/{id}/settings
        
        Update setting data related to a company
        
        Request body schema: companiesSettingsBody-put
        """
        return Document(await self._client.request("PUT", f"/companies/{id}/settings", json=body, params=params, validate=validate))

    async def tasks(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /companies/{id}/tasks
        
        Get company's tasks
        """
        return Document(await self._client.request("GET", f"/companies/{id}/tasks", params=params, validate=validate))



class ConditionalFieldsAPI:
    """Endpoints under /conditional-fields."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /conditional-fields
        
        Search conditional fields rules.
        
        Conditional fields define validation rules for entity attributes based on state, type, and agency.
        These rules determine the shield status (completion level) for entities.
        
        Query params:
          modules (string, repeatable): List of modules to filter
          display (string, one of: list | cards, default list): Display mode for results
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
        """
        return Document(await self._client.request("GET", "/conditional-fields", params=params, validate=validate))

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /conditional-fields
        
        Create a conditional field
        
        Request body schema: conditionalFieldsBody-post
        """
        return Document(await self._client.request("POST", "/conditional-fields", json=body, params=params, validate=validate))

    async def default(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /conditional-fields/default
        
        Get empty conditional field's default basic data
        """
        return Document(await self._client.request("GET", "/conditional-fields/default", params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /conditional-fields/{id}
        
        Delete the conditional field
        """
        return Document(await self._client.request("DELETE", f"/conditional-fields/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /conditional-fields/{id}
        
        Get conditional field's basic data
        """
        return Document(await self._client.request("GET", f"/conditional-fields/{id}", params=params, validate=validate))

    async def update(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /conditional-fields/{id}
        
        Update basic data related to a conditional field
        
        Request body schema: conditionalFieldsBody-put
        """
        return Document(await self._client.request("PUT", f"/conditional-fields/{id}", json=body, params=params, validate=validate))



class ContactsAPI:
    """Endpoints under /contacts."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /contacts
        
        Search contacts
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/contacts.csv?keywords=CCON100*
        
        Query params:
          keywords (string): If `keywords = CCON**ID1** CSOC**ID2**` then contacts
          keywordsType (string, default default): * `default` : Contacts are filtered following `keywords` found into their last name, first name, company's name, function and technical perimeter
          returnMoreData (string, repeatable): Returns the following attributes or relationships, if specified and user is allowed to
          states (integer, repeatable): List of contact states `id` to filter (described by /api/rest/application/dictionary/setting.state.contact)
          companyStates (integer, repeatable): List of company states `id` to filter (described by /api/rest/application/dictionary/setting.state.company)
          typesOf (integer, repeatable): List of contact typesOf `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.contact)
          activityAreas (string, repeatable): List of contact activity areas `id` to filter (described by /api/rest/application/dictionary/setting.activityArea)
          tools (string, repeatable): List of contact tools `id` to filter (described by /api/rest/application/dictionary/setting.tool)
          expertiseAreas (string, repeatable): List of company expertise areas `id` to filter (described by /api/rest/application/dictionary/setting.expertiseArea)
          origins (string, repeatable): List of contact origins `id` to filter (described by /api/rest/application/dictionary/setting.origin)
          period (string): * `created` : Contacts created between `startDate` and `endDate` are filtered
          periodActions (integer, repeatable): List of actions `id` (../bddboondmanager/classes/TAB_ACTION.html#property_ACTION_TYPE described by /api/rest/application/dictionary/setting.action.contact = integer
          periodDynamic (string): * `today` : Contacts filtered according to the grid for today's period
          periodDynamicParameters (string): Filter parameters of dynamic period. Used when periodDynamic is "lastCustomPeriod" or "nextCustomPeriod"
          startDate (string): Start date
          endDate (string): End date
          flags (integer, repeatable): Contacts attached to this flag whom flag's unique identifier = integer are filtered
          columns (string, repeatable): List of columns
          encoding (string): If the output format is **csv** then **encoding** filter should be one of
          exportToDownloadCenter (boolean, default False): Export purchases formatted file to the download center
          appEntityFields (string, repeatable): List of app entity responses filtered by `<appId>_<fieldId>:<responseValue>` and with html characters encoded
          influencers (integer, repeatable): List of contact influencers `id` to filter
          completeness (string, repeatable): Filter contacts by field completeness (filled or empty).
          shields (string, repeatable): Filter contacts by their shield status (conditional fields completion level)
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: company.name | town | lastName | firstName | function | state | company.expertiseArea | mainManager.lastName | updateDate
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/contacts", params=params, validate=validate))

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /contacts
        
        Create a contact
        
        Request body schema: contactsBody-post
        """
        return Document(await self._client.request("POST", "/contacts", json=body, params=params, validate=validate))

    async def default(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /contacts/default
        
        Get empty contact's default information data
        
        Query params:
          company (integer, REQUIRED): Company's `id` on which contact depends
        """
        return Document(await self._client.request("GET", "/contacts/default", params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /contacts/{id}
        
        Delete the contact
        """
        return Document(await self._client.request("DELETE", f"/contacts/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /contacts/{id}
        
        Get contact's basic data
        """
        return Document(await self._client.request("GET", f"/contacts/{id}", params=params, validate=validate))

    async def actions(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /contacts/{id}/actions
        
        Get contact's actions
        
        Query params:
          actionTypes (integer, repeatable): List of action types `id`, related to the action's contact, to filter (described by /api/rest/application/dictionary/setting.action.contact)
          returnRelatedActions (boolean, default False): Return related parent and child/sibbling actions
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: startDate | type | text | dependsOn.lastName
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/contacts/{id}/actions", params=params, validate=validate))

    async def attached_flags(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /contacts/{id}/attached-flags
        
        Get contact's attached flags
        """
        return Document(await self._client.request("GET", f"/contacts/{id}/attached-flags", params=params, validate=validate))

    async def information(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /contacts/{id}/information
        
        Get contact's information data
        """
        return Document(await self._client.request("GET", f"/contacts/{id}/information", params=params, validate=validate))

    async def update_information(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /contacts/{id}/information
        
        Update information data related to a contact
        
        Request body schema: contactsInformationBody-put
        """
        return Document(await self._client.request("PUT", f"/contacts/{id}/information", json=body, params=params, validate=validate))

    async def invoices(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /contacts/{id}/invoices
        
        Get contact's invoices
        
        Query params:
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: turnoverIncludingTax | creationDate | turnoverExcludingTax | expectedPaymentDate | state | reference | order.project.contact.lastName
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/contacts/{id}/invoices", params=params, validate=validate))

    async def merge(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /contacts/{id}/merge
        
        Test a merge or start a merge between two contacts.
        
        Request body schema: contactsMergeBody-post
        """
        return Document(await self._client.request("POST", f"/contacts/{id}/merge", json=body, params=params, validate=validate))

    async def opportunities(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /contacts/{id}/opportunities
        
        Get contact's opportunities
        
        Query params:
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: creationDate | title | state | totalWeightedTurnOverExcludingTax | mainManager.lastName
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/contacts/{id}/opportunities", params=params, validate=validate))

    async def orders(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /contacts/{id}/orders
        
        Get contact's orders
        
        Query params:
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: creationDate | reference | state | customerAgreement | project.contact.lastName | turnoverInvoicedExcludingTax | turnoverOrderedExcludingTax | deltaInvoicedExcludingTax
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/contacts/{id}/orders", params=params, validate=validate))

    async def projects(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /contacts/{id}/projects
        
        Get contact's projects
        
        Query params:
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: startDate | endDate | reference | contact.lastName | mainManager.lastName
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/contacts/{id}/projects", params=params, validate=validate))

    async def purchases(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /contacts/{id}/purchases
        
        Get contact's purchases
        
        Query params:
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: title | state | creationDate | project.reference | contact.lastName | mainManager.lastName
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/contacts/{id}/purchases", params=params, validate=validate))

    async def rights(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /contacts/{id}/rights
        
        Get contact's rights
        
        Query params:
          company (integer): Company's `id` on which contact depends
        """
        return Document(await self._client.request("GET", f"/contacts/{id}/rights", params=params, validate=validate))

    async def tasks(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /contacts/{id}/tasks
        
        Get contact's tasks
        """
        return Document(await self._client.request("GET", f"/contacts/{id}/tasks", params=params, validate=validate))



class ContractsAPI:
    """Endpoints under /contracts."""

    def __init__(self, client) -> None:
        self._client = client

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /contracts
        
        Create a contract
        
        Request body schema: contractsBody-post
        """
        return Document(await self._client.request("POST", "/contracts", json=body, params=params, validate=validate))

    async def default(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /contracts/default
        
        Get empty contract's default basic data
        
        Query params:
          resource (integer): Resource's `id` on which contract depends. `candidate` parameter can not be set too.
          parentContract (integer): Contract's `id` on which contract depends
          candidate (integer): Candidate's `id` on which contract depends. `resource` parameter can not be set too.
        """
        return Document(await self._client.request("GET", "/contracts/default", params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /contracts/{id}
        
        Delete the contract
        """
        return Document(await self._client.request("DELETE", f"/contracts/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /contracts/{id}
        
        Get contract's basic data
        """
        return Document(await self._client.request("GET", f"/contracts/{id}", params=params, validate=validate))

    async def update(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /contracts/{id}
        
        Update basic data related to a contract
        
        Request body schema: contractsBody-put
        """
        return Document(await self._client.request("PUT", f"/contracts/{id}", json=body, params=params, validate=validate))

    async def advantages(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /contracts/{id}/advantages
        
        Get contract's advantages
        
        Query params:
          advantageTypes (integer, repeatable): List of advantages types `reference` to filter (described by /api/rest/agencies on view `resources`)
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: creationDate | typeOf.name
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/contracts/{id}/advantages", params=params, validate=validate))

    async def download(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /contracts/{id}/download
        
        Get contract formatted file content
        
        Query params:
          language (string, one of: fr | en | es): Language used for the file content
          template (string): template ID
        """
        return Document(await self._client.request("GET", f"/contracts/{id}/download", params=params, validate=validate))

    async def rights(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /contracts/{id}/rights
        
        Get contract's rights
        
        Query params:
          resource (integer): Resource's `id` on which contract depends. `candidate` parameter can not be set too.
          parentContract (integer): Contract's `id` on which contract depends
          candidate (integer): Candidate's `id` on which contract depends. `resource` parameter can not be set too.
        """
        return Document(await self._client.request("GET", f"/contracts/{id}/rights", params=params, validate=validate))

    async def tasks(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /contracts/{id}/tasks
        
        Get contract's tasks
        """
        return Document(await self._client.request("GET", f"/contracts/{id}/tasks", params=params, validate=validate))



class DashboardsAPI:
    """Endpoints under /dashboards."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /dashboards
        
        Search dashboards for Current User
        """
        return Document(await self._client.request("GET", "/dashboards", params=params, validate=validate))

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /dashboards
        
        Create a dashboard
        
        Request body schema: dashboardsBody-post
        """
        return Document(await self._client.request("POST", "/dashboards", json=body, params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /dashboards/{id}
        
        Delete the dashboard
        """
        return Document(await self._client.request("DELETE", f"/dashboards/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /dashboards/{id}
        
        Get dashboard's basic data
        """
        return Document(await self._client.request("GET", f"/dashboards/{id}", params=params, validate=validate))

    async def update(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /dashboards/{id}
        
        Update dashboard's basic data
        
        Request body schema: dashboardsBody-put
        """
        return Document(await self._client.request("PUT", f"/dashboards/{id}", json=body, params=params, validate=validate))



class DeliveriesAPI:
    """Endpoints under /deliveries."""

    def __init__(self, client) -> None:
        self._client = client

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /deliveries
        
        Create a delivery
        
        Query params:
          forceTransferCreation (boolean, default False): true if a slave has to be created
          contact (integer): Contact's `id` on which new opportunity and project will depends
          company (integer): Company's `id` on which new opportunity and project will depends
          projectTypeOf (integer): Opportunity type `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.project).
          opportunityTitle (string): Opportunity's `title` on which new opportunity will depends
          addPositioning (boolean, default False): true if a positioning has to be added to the opportunity on which project depends
          sendMailToDependsOnManager (boolean): If `true` to send an email
          sendMailToProjectManager (boolean): If `true` to send an email
        
        Request body schema: deliveriesBody-post
        """
        return Document(await self._client.request("POST", "/deliveries", json=body, params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /deliveries/{id}
        
        Delete the delivery
        """
        return Document(await self._client.request("DELETE", f"/deliveries/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /deliveries/{id}
        
        Get delivery's basic data
        """
        return Document(await self._client.request("GET", f"/deliveries/{id}", params=params, validate=validate))

    async def update(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /deliveries/{id}
        
        Update basic data related to a delivery
        
        Query params:
          forceTransferCreation (boolean, default False): true if a slave has to be created
          contact (integer): Contact's `id` on which new opportunity and project will depends
          company (integer): Company's `id` on which new opportunity and project will depends
          projectTypeOf (integer): Project type `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.project).
          opportunityTitle (string): Opportunity's `title` on which new opportunity will depends
        
        Request body schema: deliveriesBody-put
        """
        return Document(await self._client.request("PUT", f"/deliveries/{id}", json=body, params=params, validate=validate))

    async def advantages(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /deliveries/{id}/advantages
        
        Get delivery's advantages
        
        Query params:
          advantageTypes (integer, repeatable): List of advantages types `reference` to filter (described by /api/rest/agencies on view `resources`)
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: creationDate | typeOf.name
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/deliveries/{id}/advantages", params=params, validate=validate))

    async def delivery_order_download(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /deliveries/{id}/delivery-order-download
        
        Get delivery formatted file content
        
        Query params:
          deliveryOrder (integer, REQUIRED): Delivery order `id` (described by /api/rest/application/dictionary/setting.deliveryOrder)
          language (string, one of: fr | en | es): Language used for the file content
          contact (integer): Contact's `id` on which formatted file depends
        """
        return Document(await self._client.request("GET", f"/deliveries/{id}/delivery-order-download", params=params, validate=validate))

    async def download(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /deliveries/{id}/download
        
        Get delivery formatted file content
        
        Query params:
          language (string, one of: fr | en | es): Language used for the file content
          template (string): template ID
        """
        return Document(await self._client.request("GET", f"/deliveries/{id}/download", params=params, validate=validate))

    async def renew(self, id, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /deliveries/{id}/renew
        
        Renew this delivery by creating a new one
        """
        return Document(await self._client.request("POST", f"/deliveries/{id}/renew", json=body, params=params, validate=validate))

    async def rights(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /deliveries/{id}/rights
        
        Get delivery's rights
        """
        return Document(await self._client.request("GET", f"/deliveries/{id}/rights", params=params, validate=validate))

    async def send(self, id, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /deliveries/{id}/send
        
        Send delivery's formatted filed by mail
        
        Query params:
          contact (integer): Contact's `id` on which formatted file depends
          deliveryOrder (integer): Delivery order `id` (described by /api/rest/application/dictionary/setting.deliveryOrder)
          template (string): template ID
        """
        return Document(await self._client.request("POST", f"/deliveries/{id}/send", json=body, params=params, validate=validate))

    async def tasks(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /deliveries/{id}/tasks
        
        Get delivery's tasks
        """
        return Document(await self._client.request("GET", f"/deliveries/{id}/tasks", params=params, validate=validate))



class DeliveriesGroupmentsAPI:
    """Endpoints under /deliveries-groupments."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /deliveries-groupments
        
        Search deliveries & groupments
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/deliveries-groupments.csv?keywords=MIS100*
        
        Query params:
          keywords (string): If `keywords = MIS**ID1** PRJ**ID2** COMP**ID3** CCON**ID4** CSOC**ID5** AO**ID6** PROD**ID7** CTR**ID8** GRP**ID9**` then deliveries/groupments
          projectTypes (integer, repeatable): List of project types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.project)
          projectStates (integer, repeatable): List of project states `id` to filter (described by /api/rest/application/dictionary/setting.state.project)
          deliveryStates (integer, repeatable): List of delivery states `id` to filter (described by /api/rest/application/dictionary/setting.state.delivery)
          expertiseAreas (string, repeatable): List of expertise areas `id` to filter (described by /api/rest/application/dictionary/setting.expertiseArea)
          activityAreas (string): List of activity areas `id` to filter (described by /api/rest/application/dictionary/setting.activityArea)
          transferType (string): * `master` : Only master deliveries are filtered
          sumAdditionalData (boolean, default True): Sum projects additional data
          showGroupment (boolean, default True): Show groupments
          period (string): * `started` : Deliveries/Groupments started between `startDate` and `endDate`  are filtered
          periodDynamic (string): * `today` : Deliveries/Groupments filtered according to the grid for today's period
          periodDynamicParameters (string): Filter parameters of dynamic period. Used when periodDynamic is "lastCustomPeriod" or "nextCustomPeriod"
          startDate (string): Start date
          endDate (string): End date
          flags (integer, repeatable): Projects attached to this flag whom flag's unique identifier = integer are filtered
          companies (integer, repeatable): List of companies `id` on which delivery item depends
          columns (string, repeatable): List of columns
          encoding (string): If the output format is **csv** then **encoding** filter should be one of
          appEntityFields (string, repeatable): List of app entity responses filtered by `<appId>_<fieldId>:<responseValue>` and with html characters encoded
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: startDate | endDate | id | project.reference | project.company.name | project.mainManager.lastName | intermediaryCompany.name
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/deliveries-groupments", params=params, validate=validate))



class DevicesAPI:
    """Endpoints under /devices."""

    def __init__(self, client) -> None:
        self._client = client

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /devices/{id}
        
        Delete the device
        """
        return Document(await self._client.request("DELETE", f"/devices/{id}", params=params, validate=validate))

    async def delete_session(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /devices/{id}/session
        
        Delete the session
        """
        return Document(await self._client.request("DELETE", f"/devices/{id}/session", params=params, validate=validate))



class DocumentsAPI:
    """Endpoints under /documents."""

    def __init__(self, client) -> None:
        self._client = client

    async def create(self, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /documents
        
        Create a document
        """
        return Document(await self._client.request("POST", "/documents", json=body, params=params, validate=validate))

    async def viewer(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /documents/viewer
        
        Search documents for app's viewer.
        
        You must have an app's viewer installed.
        
        Query params:
          documents (string, repeatable): Documents whom document's unique identifier are filtered
        """
        return Document(await self._client.request("GET", "/documents/viewer", params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /documents/{id}
        
        Delete the document
        """
        return Document(await self._client.request("DELETE", f"/documents/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /documents/{id}
        
        Get document content
        """
        return Document(await self._client.request("GET", f"/documents/{id}", params=params, validate=validate))

    async def update(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /documents/{id}
        
        Update information data related to a document
        
        Request body schema: documentsProfileBody-put
        """
        return Document(await self._client.request("PUT", f"/documents/{id}", json=body, params=params, validate=validate))



class DownloadCenterAPI:
    """Endpoints under /download-center."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /download-center
        
        Manage download center
        
        Query params:
          perimeterManagers (integer, repeatable): Download center's manager manager's unique identifier are filtered.
          folder (string): Download center's folder of this search's manager
        """
        return Document(await self._client.request("GET", "/download-center", params=params, validate=validate))

    async def delete_by_folder(self, perimeter_manager, folder, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /download-center/{perimeterManager}/{folder}
        
        Delete the download center's folder
        """
        return Document(await self._client.request("DELETE", f"/download-center/{perimeter_manager}/{folder}", params=params, validate=validate))

    async def by_folder(self, perimeter_manager, folder, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /download-center/{perimeterManager}/{folder}
        
        Search download center's files
        
        Query params:
          key (string): Folder's `key` when no user is logged in
          customerCode (string): Customer's code when no user is logged in
        """
        return Document(await self._client.request("GET", f"/download-center/{perimeter_manager}/{folder}", params=params, validate=validate))

    async def by_folder_download(self, perimeter_manager, folder, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /download-center/{perimeterManager}/{folder}/download
        
        Get download center's folder content
        
        Query params:
          key (string): Folder's `key` when no user is logged in
          customerCode (string): Customer's code when no user is logged in
        """
        return Document(await self._client.request("GET", f"/download-center/{perimeter_manager}/{folder}/download", params=params, validate=validate))

    async def delete_by_folder_visitor_access(self, perimeter_manager, folder, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /download-center/{perimeterManager}/{folder}/visitor-access
        
        Delete the visitor access to a download center's file
        """
        return Document(await self._client.request("DELETE", f"/download-center/{perimeter_manager}/{folder}/visitor-access", params=params, validate=validate))

    async def by_folder_visitor_access(self, perimeter_manager, folder, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /download-center/{perimeterManager}/{folder}/visitor-access
        
        Create a visitor access to a download center's file
        """
        return Document(await self._client.request("POST", f"/download-center/{perimeter_manager}/{folder}/visitor-access", json=body, params=params, validate=validate))

    async def delete_by_folder_by_file(self, perimeter_manager, folder, file, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /download-center/{perimeterManager}/{folder}/{file}
        
        Delete the download center's file
        """
        return Document(await self._client.request("DELETE", f"/download-center/{perimeter_manager}/{folder}/{file}", params=params, validate=validate))

    async def by_folder_by_file(self, perimeter_manager, folder, file, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /download-center/{perimeterManager}/{folder}/{file}
        
        Get download center's file content
        
        Query params:
          key (string): Folder's `key` when no user is logged in
          customerCode (string): Customer's code when no user is logged in
        """
        return Document(await self._client.request("GET", f"/download-center/{perimeter_manager}/{folder}/{file}", params=params, validate=validate))



class EInvoicingAPI:
    """Endpoints under /e-invoicing."""

    def __init__(self, client) -> None:
        self._client = client

    async def schemes(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /e-invoicing/schemes
        
        get e-invoicing schemes
        """
        return Document(await self._client.request("GET", "/e-invoicing/schemes", params=params, validate=validate))



class ExpensesAPI:
    """Endpoints under /expenses."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /expenses
        
        Search expenses
        
        This API is accessible only if :
        * x-JWT security scheme is used
        * `allRights` into the payload is `true`
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/expenses.csv?keywords=TPS1*
        
        Query params:
          keywords (string): If `keywords = COMP**ID1** PRJ**ID2** CCON**ID3** CSOC**ID4**` then expenses
          activityType (string, one of: absence | internal | production)
          category (string, one of: actual | fixed)
          resourceTypes (integer, repeatable): List of resource types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.resource)
          excludeResourceTypes (integer, repeatable): List of resource types `id` not filtered (described by /api/rest/application/dictionary/setting.typeOf.resource)
          period (string): * `inProgress` : Expenses between `startDate` and `endDate` are filtered
          startDate (string): Start date
          endDate (string): End date
          encoding (string): If the output format is **csv** then **encoding** filter should be one of
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: category | startDate | resource.lastName
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/expenses", params=params, validate=validate))



class ExpensesReportsAPI:
    """Endpoints under /expenses-reports."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /expenses-reports
        
        Search expenses
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/expenses-reports.csv?keywords=EXP1*
        
        Query params:
          startMonth (string, REQUIRED): Start month
          endMonth (string, REQUIRED): End month
          keywords (string): If `keywords = EXP**ID1** COMP**ID2**` then expenses
          perimeterAgenciesType (string, default resources): - `resources`: The filter **perimeterAgencies** is used only on the **agency** of resources
          resourceTypes (integer, repeatable): List of resource types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.resource)
          validationStates (string, repeatable, one of: waitingForValidation | validated | rejected)
          closed (boolean): If `true` returns only expenses which are closed, if `false` returns only expenses which are not closed
          encoding (string): If the output format is **csv** then **encoding** filter should be one of
          extractType (string, default notDetailed): If the output format is **csv** then **extractType** filter should be one of
          exportToDownloadCenter (string): Export expenses formatted file and/or documents to the download center
          paid (string, repeatable, one of: waiting | done): List of possible filters on payment receiving
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: term | paid | state | resource.lastName | closed
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/expenses-reports", params=params, validate=validate))

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /expenses-reports
        
        Create an expenses
        
        Request body schema: expensesReportsBody-post
        """
        return Document(await self._client.request("POST", "/expenses-reports", json=body, params=params, validate=validate))

    async def default(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /expenses-reports/default
        
        Get empty expenses default basic data
        
        Query params:
          resource (integer, REQUIRED): Resource's `id` on which expenses depends
          term (string, REQUIRED): Start month
          agency (integer): Agency's `id` on which expenses depends
        """
        return Document(await self._client.request("GET", "/expenses-reports/default", params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /expenses-reports/{id}
        
        Delete the expenses
        """
        return Document(await self._client.request("DELETE", f"/expenses-reports/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /expenses-reports/{id}
        
        Get expenses basic data
        """
        return Document(await self._client.request("GET", f"/expenses-reports/{id}", params=params, validate=validate))

    async def update(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /expenses-reports/{id}
        
        Update basic data related to an expenses
        
        Request body schema: expensesReportsBody-put
        """
        return Document(await self._client.request("PUT", f"/expenses-reports/{id}", json=body, params=params, validate=validate))

    async def certification(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /expenses-reports/{id}/certification
        
        Launch certification on expensesreport
        
        Request body schema: expensesReportsCertificationBody-post
        """
        return Document(await self._client.request("POST", f"/expenses-reports/{id}/certification", json=body, params=params, validate=validate))

    async def download(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /expenses-reports/{id}/download
        
        Get expenses formatted file content
        
        Query params:
          type (string, REQUIRED): Type of formatted file
          language (string, one of: fr | en | es): Language used for the file content
          project (integer): Project's `id` on which formatted file depends.
          onlyReinvoicedExpenses (boolean, default False): Available only if **type** is `customer`
          showResourceFullName (boolean, default False): Available only if **type** is `customer`
          showInformationComments (boolean, default False): Available only if **type** is `customer`
        """
        return Document(await self._client.request("GET", f"/expenses-reports/{id}/download", params=params, validate=validate))

    async def pay(self, id, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /expenses-reports/{id}/pay
        
        Pay an expenses
        """
        return Document(await self._client.request("POST", f"/expenses-reports/{id}/pay", json=body, params=params, validate=validate))

    async def reject(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /expenses-reports/{id}/reject
        
        Reject an expenses
        
        Request body schema: expensesReportsRejectBody-post
        """
        return Document(await self._client.request("POST", f"/expenses-reports/{id}/reject", json=body, params=params, validate=validate))

    async def rights(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /expenses-reports/{id}/rights
        
        Get expenses rights
        
        Query params:
          resource (integer): Resource's `id` on which expenses depends
          term (string): Start month
          agency (integer): Agency's `id` on which expenses depends
        """
        return Document(await self._client.request("GET", f"/expenses-reports/{id}/rights", params=params, validate=validate))

    async def unvalidate(self, id, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /expenses-reports/{id}/unvalidate
        
        Unvalidate an expenses
        
        Query params:
          expectedValidator (integer, REQUIRED): Resource's `id` on which expenses depends
        """
        return Document(await self._client.request("POST", f"/expenses-reports/{id}/unvalidate", json=body, params=params, validate=validate))

    async def validate(self, id, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /expenses-reports/{id}/validate
        
        Validate an expenses
        
        Query params:
          expectedValidator (integer, REQUIRED): Resource's `id` on which expenses depends
        """
        return Document(await self._client.request("POST", f"/expenses-reports/{id}/validate", json=body, params=params, validate=validate))



class FlagsAPI:
    """Endpoints under /flags."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /flags
        
        Search flags
        
        Query params:
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: name | mainManager.lastName
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/flags", params=params, validate=validate))

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /flags
        
        Create a flag
        
        Request body schema: flagsBody-post
        """
        return Document(await self._client.request("POST", "/flags", json=body, params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /flags/{id}
        
        Delete the flag
        """
        return Document(await self._client.request("DELETE", f"/flags/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /flags/{id}
        
        Get flag's basic data
        """
        return Document(await self._client.request("GET", f"/flags/{id}", params=params, validate=validate))

    async def update(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /flags/{id}
        
        Update basic data related to a flag
        
        Request body schema: flagsBody-put
        """
        return Document(await self._client.request("PUT", f"/flags/{id}", json=body, params=params, validate=validate))



class FollowedDocumentsAPI:
    """Endpoints under /followed-documents."""

    def __init__(self, client) -> None:
        self._client = client

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /followed-documents
        
        Create a document to follow
        
        Request body schema: followedDocumentsBody-post
        """
        return Document(await self._client.request("POST", "/followed-documents", json=body, params=params, validate=validate))

    async def default(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /followed-documents/default
        
        Get empty document to follow Default's basic data
        
        Query params:
          dependsOn (integer): The id of the entity that the document to follow is created for.
          followedDocument (integer): if it is a renewal, it is a document to follow id of the parent
        """
        return Document(await self._client.request("GET", "/followed-documents/default", params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /followed-documents/{id}
        
        Delete the document to follow up
        """
        return Document(await self._client.request("DELETE", f"/followed-documents/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /followed-documents/{id}
        
        Get basic data of document to follow
        """
        return Document(await self._client.request("GET", f"/followed-documents/{id}", params=params, validate=validate))

    async def update(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /followed-documents/{id}
        
        Update basic data related to a document to follow up
        
        Request body schema: followedDocumentsBody-put
        """
        return Document(await self._client.request("PUT", f"/followed-documents/{id}", json=body, params=params, validate=validate))

    async def rights(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /followed-documents/{id}/rights
        
        Get rights of documents to follow
        
        Query params:
          dependsOn (integer): The id of the entity that the document to follow is created for.
          parentRenewal (integer): if it is a renewal, it is a document to follow id of the parent
        """
        return Document(await self._client.request("GET", f"/followed-documents/{id}/rights", params=params, validate=validate))



class FormsAPI:
    """Endpoints under /forms."""

    def __init__(self, client) -> None:
        self._client = client

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /forms
        
        Create a form
        
        Request body schema: formsBody-post
        """
        return Document(await self._client.request("POST", "/forms", json=body, params=params, validate=validate))

    async def default(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /forms/default
        
        Get empty form's default basic data
        
        Query params:
          template (integer): The id of the template that the form is created for.
          resource (integer): The id of the entity that the form is created for.
        """
        return Document(await self._client.request("GET", "/forms/default", params=params, validate=validate))

    async def templates(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /forms/templates
        
        Search form's templates
        """
        return Document(await self._client.request("GET", "/forms/templates", params=params, validate=validate))

    async def post_templates(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /forms/templates
        
        Create a form's template
        
        Request body schema: formsTemplatesBody-post
        """
        return Document(await self._client.request("POST", "/forms/templates", json=body, params=params, validate=validate))

    async def templates_default(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /forms/templates/default
        
        Get empty form's template's default basic data
        """
        return Document(await self._client.request("GET", "/forms/templates/default", params=params, validate=validate))

    async def delete_templates_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /forms/templates/{id}
        
        Delete the form's template
        """
        return Document(await self._client.request("DELETE", f"/forms/templates/{id}", params=params, validate=validate))

    async def templates_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /forms/templates/{id}
        
        Get form's template's basic data
        """
        return Document(await self._client.request("GET", f"/forms/templates/{id}", params=params, validate=validate))

    async def update_templates_by_id(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /forms/templates/{id}
        
        Update form's template's basic data
        
        Request body schema: formsTemplatesBody-put
        """
        return Document(await self._client.request("PUT", f"/forms/templates/{id}", json=body, params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /forms/{id}
        
        Delete the form
        """
        return Document(await self._client.request("DELETE", f"/forms/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /forms/{id}
        
        Get form's basic data
        """
        return Document(await self._client.request("GET", f"/forms/{id}", params=params, validate=validate))

    async def update(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /forms/{id}
        
        Update form's basic data
        
        Request body schema: formsBody-put
        """
        return Document(await self._client.request("PUT", f"/forms/{id}", json=body, params=params, validate=validate))

    async def remind(self, id, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /forms/{id}/remind
        
        Remind a form
        """
        return Document(await self._client.request("POST", f"/forms/{id}/remind", json=body, params=params, validate=validate))

    async def rights(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /forms/{id}/rights
        
        Get form's rights
        """
        return Document(await self._client.request("GET", f"/forms/{id}/rights", params=params, validate=validate))

    async def tasks(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /forms/{id}/tasks
        
        Get form's tasks
        """
        return Document(await self._client.request("GET", f"/forms/{id}/tasks", params=params, validate=validate))



class GadgetsAPI:
    """Endpoints under /gadgets."""

    def __init__(self, client) -> None:
        self._client = client

    async def values(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /gadgets/{id}/values
        
        Get gadget's values
        """
        return Document(await self._client.request("GET", f"/gadgets/{id}/values", params=params, validate=validate))



class GoogleAPI:
    """Endpoints under /google."""

    def __init__(self, client) -> None:
        self._client = client

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /google/{id}
        
        Log out user
        """
        return Document(await self._client.request("DELETE", f"/google/{id}", params=params, validate=validate))



class GroupmentsAPI:
    """Endpoints under /groupments."""

    def __init__(self, client) -> None:
        self._client = client

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /groupments
        
        Create a groupment
        
        Request body schema: groupmentsBody-post
        """
        return Document(await self._client.request("POST", "/groupments", json=body, params=params, validate=validate))

    async def default(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /groupments/default
        
        Get empty groupment's default information data
        
        Query params:
          project (integer, REQUIRED): Project's `id` on which groupment depends.
        """
        return Document(await self._client.request("GET", "/groupments/default", params=params, validate=validate))

    async def duplicate(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /groupments/duplicate
        
        Duplicate groupment
        
        Query params:
          startDate (string, REQUIRED): Start date
          endDate (string, REQUIRED): End date
          groupment (integer): Groupment's `id` to duplicate.
        
        Request body schema: groupmentsDuplicateBody-post
        """
        return Document(await self._client.request("POST", "/groupments/duplicate", json=body, params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /groupments/{id}
        
        Delete the groupment
        """
        return Document(await self._client.request("DELETE", f"/groupments/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /groupments/{id}
        
        Get groupment's basic data
        """
        return Document(await self._client.request("GET", f"/groupments/{id}", params=params, validate=validate))

    async def update(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /groupments/{id}
        
        Update basic data related to a groupment
        
        Query params:
          forceDates (boolean, default False): If true, groupment date will be updated and all associated deliveries will be updated too (with this dates)
        
        Request body schema: groupmentsBody-put
        """
        return Document(await self._client.request("PUT", f"/groupments/{id}", json=body, params=params, validate=validate))

    async def rights(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /groupments/{id}/rights
        
        Get groupment's rights
        
        Query params:
          project (integer): Project's `id` on which groupment depends.
        """
        return Document(await self._client.request("GET", f"/groupments/{id}/rights", params=params, validate=validate))



class ImportAPI:
    """Endpoints under /import."""

    def __init__(self, client) -> None:
        self._client = client

    async def actions(self, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /import/actions
        
        Import actions
        """
        return Document(await self._client.request("POST", "/import/actions", json=body, params=params, validate=validate))

    async def candidates(self, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /import/candidates
        
        Import candidates
        """
        return Document(await self._client.request("POST", "/import/candidates", json=body, params=params, validate=validate))

    async def contacts(self, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /import/contacts
        
        Import contacts
        """
        return Document(await self._client.request("POST", "/import/contacts", json=body, params=params, validate=validate))

    async def opportunities(self, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /import/opportunities
        
        Import opportunities
        """
        return Document(await self._client.request("POST", "/import/opportunities", json=body, params=params, validate=validate))

    async def resources(self, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /import/resources
        
        Import resources
        """
        return Document(await self._client.request("POST", "/import/resources", json=body, params=params, validate=validate))



class InactivitiesAPI:
    """Endpoints under /inactivities."""

    def __init__(self, client) -> None:
        self._client = client

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /inactivities
        
        Create an inactivity
        
        Request body schema: inactivitiesBody-post
        """
        return Document(await self._client.request("POST", "/inactivities", json=body, params=params, validate=validate))

    async def default(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /inactivities/default
        
        Get empty inactivity's default information data
        
        Query params:
          resource (integer, REQUIRED): Resource's `id` on which inactivity depends.
        """
        return Document(await self._client.request("GET", "/inactivities/default", params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /inactivities/{id}
        
        Delete the inactivity
        """
        return Document(await self._client.request("DELETE", f"/inactivities/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /inactivities/{id}
        
        Get inactivity's basic data
        """
        return Document(await self._client.request("GET", f"/inactivities/{id}", params=params, validate=validate))

    async def update(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /inactivities/{id}
        
        Update basic data related to an inactivity
        
        Request body schema: inactivitiesBody-put
        """
        return Document(await self._client.request("PUT", f"/inactivities/{id}", json=body, params=params, validate=validate))

    async def rights(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /inactivities/{id}/rights
        
        Get inactivity's rights
        
        Query params:
          resource (integer): Resource's `id` on which inactivity depends.
        """
        return Document(await self._client.request("GET", f"/inactivities/{id}/rights", params=params, validate=validate))



class InvoicesAPI:
    """Endpoints under /invoices."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /invoices
        
        Search invoices
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/invoices.csv?keywords=FACT1*
        
        Query params:
          keywords (string): If `keywords = FACT**ID1** BDC**ID2** PRJ**ID3** CCON**ID4** CSOC**ID5**` then invoices
          projectTypes (integer, repeatable): List of project types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.project)
          paymentMethods (integer, repeatable): List of payment methods `id` to filter (described by /api/rest/application/dictionary/setting.paymentMethod)
          states (integer, repeatable): List of invoice states `id` to filter (described by /api/rest/application/dictionary/setting.state.invoice)
          companies (integer, repeatable): List of companies `id` on which invoices item depends
          closed (boolean): If `true` returns only invoices/credit notes which are closed, if `false` returns only invoices/credit notes which are not closed
          creditNote (boolean): If `true` returns only credit notes, if `false` returns only bills
          period (string): * `created` : Invoices created between `startDate` and `endDate` are filtered
          periodDynamic (string): * `today` : Invoices filtered according to the grid for today's period
          periodDynamicParameters (string): Filter parameters of dynamic period. Used when periodDynamic is "lastCustomPeriod" or "nextCustomPeriod"
          startDate (string): Start date
          endDate (string): End date
          amountCurrency (integer): Currency `id` to filter (described by /api/rest/application/dictionary/setting.currency)
          amountType (string): * `equal` : Invoices `amountColumn` equal to `amount`
          amountColumn (string): * `totalExcludingTax` : Invoices amount filtered by `totalExcludingTax` column
          amount (number): Invoices `amountColumn` equal to `amount`
          amountMin (number): Invoices `amountColumn` superior or equal to `amountMin`
          amountMax (number): Invoices `amountColumn` inferior or equal to `amountMax`
          flags (integer, repeatable): Invoices attached to this flag whom flag's unique identifier = integer are filtered
          encoding (string): If the output format is **csv** then **encoding** filter should be one of
          extractType (string, default notDetailed): If the output format is **csv** then **extractType** filter should be one of
          exportToDownloadCenter (string): Export invoices to the download center along with or without the attached documents from the related timesheets
          taxReportStates (number): invoice tax report state (e-invoicing) value to filter
          sendingStates (number): invoice sending state (e-invoicing) value to filter
          toControl (boolean): invoices having at least 1 billable item where to control is true
          columns (string, repeatable): List of columns
          appEntityFields (string, repeatable): List of app entity responses filtered by `<appId>_<fieldId>:<responseValue>` and with html characters encoded
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: turnoverInvoicedIncludingTax | date | reference | turnoverInvoicedExcludingTax | expectedPaymentDate | state | order.number | order.project.reference | order.project.company.name | order.mainManager.lastName | closed | startDate | endDate | intermediaryCompany.name
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/invoices", params=params, validate=validate))

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /invoices
        
        Create an invoice depending on query parameters
        
        Query params:
          method (string): How to create invoice
        
        Request body schema: invoicesBody-post
        """
        return Document(await self._client.request("POST", "/invoices", json=body, params=params, validate=validate))

    async def bulk_send(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /invoices/bulk-send
        
        Bulk send invoices and update state after
        
        Request body schema: invoicesBulkSendBody-post
        """
        return Document(await self._client.request("POST", "/invoices/bulk-send", json=body, params=params, validate=validate))

    async def cart(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /invoices/cart
        
        Get new invoice data from cart definition
        
        Query params:
          order (integer, REQUIRED): Order id
          startDate (string, REQUIRED): Start date
          endDate (string, REQUIRED): End date
          typesOf (string): * `times` : Only times items are filled
          schedule (integer): Schedule id
        """
        return Document(await self._client.request("GET", "/invoices/cart", params=params, validate=validate))

    async def default(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /invoices/default
        
        Get empty invoice's default information data
        
        Query params:
          order (integer, REQUIRED): Order's `id` on which invoice depends
          isCreditNote (boolean)
          schedule (integer): Schedule's `id` on which invoice depends
          term (string): Start month
          autoFillItemsWithTimesExpensesPurchases (string): * `times` : Only times items are filled
        """
        return Document(await self._client.request("GET", "/invoices/default", params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /invoices/{id}
        
        Delete the invoice
        """
        return Document(await self._client.request("DELETE", f"/invoices/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /invoices/{id}
        
        Get invoice's basic data
        """
        return Document(await self._client.request("GET", f"/invoices/{id}", params=params, validate=validate))

    async def actions(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /invoices/{id}/actions
        
        Get invoice's actions
        
        Query params:
          actionTypes (integer, repeatable): List of action types `id`, related to the action's invoice, to filter (described by /api/rest/application/dictionary/setting.action.invoice)
          returnRelatedActions (boolean, default False): Return related parent and child/sibbling actions
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: startDate | type | text
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/invoices/{id}/actions", params=params, validate=validate))

    async def update_adjust(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /invoices/{id}/adjust
        
        Adjust invoice
        
        Request body schema: invoicesAdjustBody-put
        """
        return Document(await self._client.request("PUT", f"/invoices/{id}/adjust", json=body, params=params, validate=validate))

    async def attached_flags(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /invoices/{id}/attached-flags
        
        Get invoice's attached flags
        """
        return Document(await self._client.request("GET", f"/invoices/{id}/attached-flags", params=params, validate=validate))

    async def billable_items(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /invoices/{id}/billable-items
        
        Get invoice's billable items
        
        Query params:
          keywords (string): If `keywords = BILL**ID1** INVREC**ID2**` then
          states (integer, repeatable): List of billable item typesOf to filter
          typesOf (integer, repeatable): List of project types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.project)
          toControl (boolean)
          validationStates (string, repeatable, one of: waitingForValidation | validated | rejected)
          resources (integer, repeatable): List of resources `id` on which billable item depends
          companies (integer, repeatable): List of companies `id` on which billable item depends
          projects (integer, repeatable): List of projects `id` on which billable item depends
          projectTypes (integer, repeatable): List of project types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.project)
          projectStates (integer, repeatable): List of project states `id` to filter (described by /api/rest/application/dictionary/setting.state.project)
          orders (integer, repeatable): List of orders `id` on which billable item depends
          period (string): * `created` : Projects created between `startDate` and `endDate`  are filtered
          periodDynamic (string): * `today` : Projects filtered according to the grid for today's period
          periodDynamicParameters (string): Filter parameters of dynamic period. Used when periodDynamic is "lastCustomPeriod" or "nextCustomPeriod"
          startDate (string): Start date
          endDate (string): End date
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: startDate | endDate | project | customer | toControl
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/invoices/{id}/billable-items", params=params, validate=validate))

    async def check(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /invoices/{id}/check
        
        Check invoice properties / states (like e-invoicing)
        """
        return Document(await self._client.request("GET", f"/invoices/{id}/check", params=params, validate=validate))

    async def download(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /invoices/{id}/download
        
        Get invoice formatted file content
        
        Query params:
          attachment (boolean): Download signed timesheet if `true`
          format (string, one of: native | cii | legal): Format asked for download invoice file. Default is "native"
        """
        return Document(await self._client.request("GET", f"/invoices/{id}/download", params=params, validate=validate))

    async def information(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /invoices/{id}/information
        
        Get invoice's information data
        """
        return Document(await self._client.request("GET", f"/invoices/{id}/information", params=params, validate=validate))

    async def update_information(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /invoices/{id}/information
        
        Update information data related to an invoice
        
        Query params:
          notifyManagerOnReconcile (boolean): If true order manager will be notified when invoice is reconcile to a banking transaction
        
        Request body schema: invoicesInformationBody-put
        """
        return Document(await self._client.request("PUT", f"/invoices/{id}/information", json=body, params=params, validate=validate))

    async def preview(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /invoices/{id}/preview
        
        Get invoice document
        
        Query params:
          format (string, one of: native | legal): Document to retrieve. Default is "native"
        """
        return Document(await self._client.request("GET", f"/invoices/{id}/preview", params=params, validate=validate))

    async def rights(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /invoices/{id}/rights
        
        Get invoice's rights
        
        Query params:
          order (integer): Order's `id` on which invoice depends
          isCreditNote (boolean)
          schedule (integer): Schedule's `id` on which invoice depends
          term (string): Start month
          autoFillItemsWithTimesExpensesPurchases (string): * `times` : Only times items are filled
        """
        return Document(await self._client.request("GET", f"/invoices/{id}/rights", params=params, validate=validate))

    async def send(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /invoices/{id}/send
        
        Send invoice by mail
        
        Query params:
          channel (string): How to send invoice
          format (string): in which format invoice will be sent
        
        Request body schema: invoices-sendBodyPost
        """
        return Document(await self._client.request("POST", f"/invoices/{id}/send", json=body, params=params, validate=validate))

    async def tasks(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /invoices/{id}/tasks
        
        Get invoice's tasks
        """
        return Document(await self._client.request("GET", f"/invoices/{id}/tasks", params=params, validate=validate))



class InvoicingConnectionsAPI:
    """Endpoints under /invoicing-connections."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /invoicing-connections
        
        Search Invoicing connectors
        
        Query params:
          channelCodes (string, repeatable, one of: peppol): List of channel code
          agencies (integer, repeatable)
        """
        return Document(await self._client.request("GET", "/invoicing-connections", params=params, validate=validate))

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /invoicing-connections
        
        Create new connector
        
        Request body schema: invoicingConnectionsBody-post
        """
        return Document(await self._client.request("POST", "/invoicing-connections", json=body, params=params, validate=validate))

    async def authorize(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /invoicing-connections/authorize
        
        Start the OAuth flow for an OAuth-only provider (e.g. Pennylane).
        The connection metadata, the selected agencies and a CSRF state are persisted
        in the user's session, then the URL of the provider's consent screen is
        returned. The actual InvoicingConnection record is created later, when the
        provider redirects the user back to /invoicing-connections/callback.
        
        Request body schema: invoicingConnectionsAuthorizeBody-post
        """
        return Document(await self._client.request("POST", "/invoicing-connections/authorize", json=body, params=params, validate=validate))

    async def callback(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /invoicing-connections/callback
        
        Endpoint the OAuth provider redirects the user back to after the consent
        screen. Exchanges the authorization code for access + refresh tokens,
        creates the InvoicingConnection record, then redirects the browser to the
        invoicing-connections administration page (`?status=success` or
        `?status=error&message=…`).
        
        On the very first hit (cross-site redirect from the provider), the session
        cookie may not be sent because of `SameSite=Strict`. The endpoint then
        serves a minimal HTML page that performs a same-site redirect with
        `&bounced=1` so the cookie is sent on the second hit.
        
        Query params:
          code (string, REQUIRED): Authorization code returned by the OAuth provider
          state (string, REQUIRED): CSRF state token previously stored in the user's session
          bounced (string): Internal flag set on the same-site bounce; never set by the provider
          error (string): Error code returned by the provider when the user denies consent
        """
        return Document(await self._client.request("GET", "/invoicing-connections/callback", params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /invoicing-connections/{id}
        
        remove connector
        """
        return Document(await self._client.request("DELETE", f"/invoicing-connections/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /invoicing-connections/{id}
        
        get connector's data
        """
        return Document(await self._client.request("GET", f"/invoicing-connections/{id}", params=params, validate=validate))

    async def update(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /invoicing-connections/{id}
        
        Update connector's data
        
        Request body schema: invoicingConnectionsBody-put
        """
        return Document(await self._client.request("PUT", f"/invoicing-connections/{id}", json=body, params=params, validate=validate))



class LogsAPI:
    """Endpoints under /logs."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /logs
        
        Search logs entity (Resource, Candidate, Project, Opportunity, Order, Invoice, Contact)
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/logs.csv?keywords=COMP100*
        
        Query params:
          keywords (string): If `keywords = COMP**ID1** CAND**ID2** PRJ**ID3** CCON**ID4** CSOC**ID5** AO**ID6** BDC**ID7** FACT**ID8** PROD**ID9** ACH**ID10** APP**ID11** PMT**ID12** MIS**ID13** INA**ID14** GRP**ID15** ACT**ID16** BU**ID17** POLE**ID18** ROLE**ID19** AJU**ID20** POS**ID21** TPS**ID22** FRS**ID23** ABS**ID24** LOG**ID25** CTR**ID26** ADV**ID27** QUOT**ID28** CUST**ID29** DEV**ID30** VAL**ID31** APPENTITY**ID32** TGT**ID33** TODOLST**ID34** FRMTPL**ID35** FRM**ID36** PUSHTPL**ID37** FLAG**ID38** WBH**ID39** ROLETPL**ID40** DSHBRD**ID41** DAS**ID42** SCH**ID43** PRFT**ID44** OFFER**ID45** GLOBAL` then
          logTypes (string, repeatable): List of log type to filter, cf. unique identifier
          logActions (string, repeatable): List of log action to filter, cf. unique identifier
          logAuths (string, repeatable): List of log auth to filter, cf. unique identifier
          maxResults (number, default 30): number of results per page (capped at 100)
          period (string): * `created` : Logs created between `startDate` and `endDate` are filtered
          periodDynamic (string): * `today` : Logs filtered according to the grid for today's period
          periodDynamicParameters (string): Filter parameters of dynamic period. Used when periodDynamic is "lastCustomPeriod" or "nextCustomPeriod"
          startDate (string): Start date
          endDate (string): End date
          encoding (string): If the output format is **csv** then **encoding** filter should be one of
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          sort (string, repeatable): Order by a given column: creationDate | action | typeOf
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/logs", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /logs/{id}
        
        Get log's basic data
        """
        return Document(await self._client.request("GET", f"/logs/{id}", params=params, validate=validate))



class MandatoryLeaveAPI:
    """Endpoints under /mandatory-leave."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /mandatory-leave
        
        Search mandatory leave
        
        Query params:
          keywords (string): If `keywords = MAL**ID1**` then mandatory leave
          resourceTypes (integer, repeatable): List of resource types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.resource)
          resourceStates (integer, repeatable): List of resource states `id` to filter (described by /api/rest/application/dictionary/setting.state.resource)
          states (integer, repeatable): List of states to filter 'deactivated' or 'activated'
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: title | state | period | agency
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/mandatory-leave", params=params, validate=validate))

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /mandatory-leave
        
        Create a mandatory absence
        
        Request body schema: mandatoryLeavesBody-post
        """
        return Document(await self._client.request("POST", "/mandatory-leave", json=body, params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /mandatory-leave/{id}
        
        Delete the mandatory leave
        """
        return Document(await self._client.request("DELETE", f"/mandatory-leave/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /mandatory-leave/{id}
        
        Get mandatory leave basic data
        """
        return Document(await self._client.request("GET", f"/mandatory-leave/{id}", params=params, validate=validate))

    async def information(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /mandatory-leave/{id}/information
        
        Get mandatory leave basic data
        """
        return Document(await self._client.request("GET", f"/mandatory-leave/{id}/information", params=params, validate=validate))

    async def update_information(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /mandatory-leave/{id}/information
        
        Update basic data related to a mandatory leave
        
        Request body schema: mandatoryLeavesInformationBody-put
        """
        return Document(await self._client.request("PUT", f"/mandatory-leave/{id}/information", json=body, params=params, validate=validate))

    async def resources(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /mandatory-leave/{id}/resources
        
        Get mandatory leave resources
        """
        return Document(await self._client.request("GET", f"/mandatory-leave/{id}/resources", params=params, validate=validate))

    async def update_resources(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /mandatory-leave/{id}/resources
        
        Exclude/include resources in mandatory leave
        
        Request body schema: mandatoryLeavesResourcesBody-put
        """
        return Document(await self._client.request("PUT", f"/mandatory-leave/{id}/resources", json=body, params=params, validate=validate))

    async def rights(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /mandatory-leave/{id}/rights
        
        Get mandatory leave rights
        """
        return Document(await self._client.request("GET", f"/mandatory-leave/{id}/rights", params=params, validate=validate))



class MarketplaceAPI:
    """Endpoints under /marketplace."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /marketplace
        
        Search marketplace's apps
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/invoices.csv?keywords=FACT1*
        
        Query params:
          keywords (string): If `keywords = APP**ID1** VENDOR**ID2**` then marketplace's apps
          categories (string, repeatable): List of apps categories
          integrations (string, repeatable): List of apps categories
          onlyMyApps (boolean, default False): Only apps which belong to this user's customer are filtered
          validations (string, repeatable, default validated): List of apps categories
          visibilities (string, repeatable, default public): List of apps categories
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: name | vendor.name | isValidated
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/marketplace", params=params, validate=validate))

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /marketplace
        
        Create a marketplace's apps
        
        Request body schema: marketplaceBody-post
        """
        return Document(await self._client.request("POST", "/marketplace", json=body, params=params, validate=validate))

    async def default(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /marketplace/default
        
        Get empty marketplace's App default information data
        
        Query params:
          integration (string): * `iFrame`
        """
        return Document(await self._client.request("GET", "/marketplace/default", params=params, validate=validate))

    async def refresh_token(self, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /marketplace/refresh-token
        
        Refresh App token
        """
        return Document(await self._client.request("POST", "/marketplace/refresh-token", json=body, params=params, validate=validate))

    async def configure(self, app_code, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /marketplace/{appCode}/configure
        
        Get marketplace's App access
        """
        return Document(await self._client.request("GET", f"/marketplace/{app_code}/configure", params=params, validate=validate))

    async def update_configure(self, app_code, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /marketplace/{appCode}/configure
        
        Update marketplace's App access
        
        Request body schema: marketplaceConfigureBody-put
        """
        return Document(await self._client.request("PUT", f"/marketplace/{app_code}/configure", json=body, params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /marketplace/{id}
        
        Delete a marketplace's App
        """
        return Document(await self._client.request("DELETE", f"/marketplace/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /marketplace/{id}
        
        Get marketplace's App basic data
        """
        return Document(await self._client.request("GET", f"/marketplace/{id}", params=params, validate=validate))

    async def update(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /marketplace/{id}
        
        Update basic data related to a marketplace's App
        
        Request body schema: marketplaceBody-put
        """
        return Document(await self._client.request("PUT", f"/marketplace/{id}", json=body, params=params, validate=validate))

    async def data_visualization(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /marketplace/{id}/data-visualization
        
        Get marketplace's App data visualization.
        
        Returns API call statistics aggregated by day and by customer, based on Elasticsearch logs.
        
        Query params:
          startDate (date): Start date for the data visualization period.
          endDate (date): End date for the data visualization period.
          numberOfCustomers (integer, default 10): Maximum number of customers to return in the APICallsByCustomer aggregation.
        """
        return Document(await self._client.request("GET", f"/marketplace/{id}/data-visualization", params=params, validate=validate))

    async def install(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /marketplace/{id}/install
        
        Install marketplace's App
        
        Request body schema: marketplaceInstallBody-post
        """
        return Document(await self._client.request("POST", f"/marketplace/{id}/install", json=body, params=params, validate=validate))

    async def delete_logo(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /marketplace/{id}/logo
        
        Delete the logo
        """
        return Document(await self._client.request("DELETE", f"/marketplace/{id}/logo", params=params, validate=validate))

    async def update_logo(self, id, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /marketplace/{id}/logo
        
        Update logo
        """
        return Document(await self._client.request("PUT", f"/marketplace/{id}/logo", json=body, params=params, validate=validate))

    async def publish(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /marketplace/{id}/publish
        
        Send publication request by mail
        
        Request body schema: marketplacePublishBody-post
        """
        return Document(await self._client.request("POST", f"/marketplace/{id}/publish", json=body, params=params, validate=validate))

    async def rights(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /marketplace/{id}/rights
        
        Get marketplace's App rights
        """
        return Document(await self._client.request("GET", f"/marketplace/{id}/rights", params=params, validate=validate))

    async def translations(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /marketplace/{id}/translations
        
        Get marketplace's App translations
        """
        return Document(await self._client.request("GET", f"/marketplace/{id}/translations", params=params, validate=validate))

    async def update_translations(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /marketplace/{id}/translations
        
        Update marketplace's App translations
        
        Request body schema: marketplace-translations-put
        """
        return Document(await self._client.request("PUT", f"/marketplace/{id}/translations", json=body, params=params, validate=validate))

    async def delete_uninstall(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /marketplace/{id}/uninstall
        
        Uninstall marketplace's App
        """
        return Document(await self._client.request("DELETE", f"/marketplace/{id}/uninstall", params=params, validate=validate))

    async def validate(self, id, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /marketplace/{id}/validate
        
        Validate marketplace's App
        """
        return Document(await self._client.request("POST", f"/marketplace/{id}/validate", json=body, params=params, validate=validate))



class MicrosoftAPI:
    """Endpoints under /microsoft."""

    def __init__(self, client) -> None:
        self._client = client

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /microsoft/{id}
        
        Log out user
        """
        return Document(await self._client.request("DELETE", f"/microsoft/{id}", params=params, validate=validate))



class NotificationsAPI:
    """Endpoints under /notifications."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /notifications
        
        Search notification for the current user.
        
        Query params:
          category (string, REQUIRED): Filter notifications per category. The available categories are
          state (string): Filter notification per state. The available states are
          parentType (string): Filter notification on specific parent type. Parent type can be any module type.
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
        """
        return Document(await self._client.request("GET", "/notifications", params=params, validate=validate))

    async def update_markas(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /notifications/markas
        
        Update state of all users notification with a specific category.
        
        Request body schema: notificationsMarkasBody-put
        """
        return Document(await self._client.request("PUT", "/notifications/markas", json=body, params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /notifications/{id}
        
        Get the notification
        """
        return Document(await self._client.request("GET", f"/notifications/{id}", params=params, validate=validate))

    async def update(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /notifications/{id}
        
        Update part of notification.
        
        Request body schema: notificationsBody-put
        """
        return Document(await self._client.request("PUT", f"/notifications/{id}", json=body, params=params, validate=validate))



class OpportunitiesAPI:
    """Endpoints under /opportunities."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /opportunities
        
        Search opportunities
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/opportunities.csv?keywords=AO100*
        
        Query params:
          keywords (string): If `keywords = AO**ID1** PROD**ID2** CAND**ID3** COMP**ID4** CCON**ID5** CSOC**ID6**` then opportunities
          returnMoreData (string, repeatable): Returns the following attributes or relationships, if specified and user is allowed to
          perimeterManagersType (string): - `main`: The filter **perimeterManagers** is used only on the **Main Manager** of opportunities
          positioningStates (string, repeatable): * `none` :  Opportunities with none positionings are filtered
          period (string): * `created` : Opportunities created between `startDate` and `endDate` are filtered
          periodActions (integer, repeatable): List of actions `id` (../bddboondmanager/classes/TAB_ACTION.html#property_ACTION_TYPE described by /api/rest/application/dictionary/setting.action.opportunity = integer
          periodDynamic (string): * `today` : Opportunities filtered according to the grid for today's period
          periodDynamicParameters (string): Filter parameters of dynamic period. Used when periodDynamic is "lastCustomPeriod" or "nextCustomPeriod"
          startDate (string): Start date
          endDate (string): End date
          opportunityStates (integer, repeatable): List of opportunity states `id` to filter (described by /api/rest/application/dictionary/setting.state.opportunity)
          opportunityTypes (string, repeatable): List of opportunity types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.project)
          expertiseAreas (string, repeatable): List of expertise areas `id` to filter (described by /api/rest/application/dictionary/setting.expertiseArea)
          activityAreas (string): List of activity areas `id` to filter (described by /api/rest/application/dictionary/setting.activityArea)
          tools (string, repeatable): List of tools `id` to filter (described by /api/rest/application/dictionary/setting.tool)
          places (string, repeatable): List of mobility areas `id` to filter (described by /api/rest/application/dictionary/setting.mobilityArea)
          durations (integer, repeatable): List of durations `id` to filter (described by /api/rest/application/dictionary/setting.duration)
          origins (string, repeatable): List of origins `id` to filter (described by /api/rest/application/dictionary/setting.origin)
          flags (integer, repeatable): Opportunities attached to this flag whom flag's unique identifier = integer are filtered
          onlyVisible (boolean, default True): The user has to have the global right `showGroupe` set to `true` or call this api into mode `god`.
          columns (string, repeatable): List of columns
          encoding (string): If the output format is **csv** then **encoding** filter should be one of
          appEntityFields (string, repeatable): List of app entity responses filtered by `<appId>_<fieldId>:<responseValue>` and with html characters encoded
          shields (string, repeatable): Filter opportunities by their shield status (conditional fields completion level)
          opportunityAlerts (boolean): * true : display only opportunities with alerts
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: creationDate | title | company.name | place | numberOfActivePositionings | startDate | endDate | duration | state | alertCount | closingDate | updateDate | answerDate | totalWeightedTurnOverExcludingTax | mainManager.lastName
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/opportunities", params=params, validate=validate))

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /opportunities
        
        Create an opportunity
        
        Request body schema: opportunitiesBody-post
        """
        return Document(await self._client.request("POST", "/opportunities", json=body, params=params, validate=validate))

    async def ai_parsing_by_job_id(self, job_id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /opportunities/ai/parsing/{jobId}
        
        Retrieve the current status of a parsing job previously created via
        `POST /api/opportunities/{id}/ai/assistant`.
        
        **Ownership**: Only the user who created the job can access it.
        
        **Statuses** (string):
        * `pending` — still processing
        * `draft` — intermediate, not yet used
        * `done` — opportunity created
        * `failed` — see `errors` for details
        """
        return Document(await self._client.request("GET", f"/opportunities/ai/parsing/{job_id}", params=params, validate=validate))

    async def default(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /opportunities/default
        
        Get empty opportunity's default information data
        
        Query params:
          contact (integer): Contact's `id` on which opportunity depends
          company (integer): Company's `id` on which opportunity depends
          typeOf (integer): Type of opportunity to create
          agency (integer): Agency's `id` on which opportunity depends
          withAIQuota (boolean): If true, includes meta.ai.quota in the response
        """
        return Document(await self._client.request("GET", "/opportunities/default", params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /opportunities/{id}
        
        Delete the opportunity
        """
        return Document(await self._client.request("DELETE", f"/opportunities/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /opportunities/{id}
        
        Get opportunity's basic data
        """
        return Document(await self._client.request("GET", f"/opportunities/{id}", params=params, validate=validate))

    async def actions(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /opportunities/{id}/actions
        
        Get opportunity's actions
        
        Query params:
          actionTypes (integer, repeatable): List of action types `id`, related to the action's opportunity, to filter (described by /api/rest/application/dictionary/setting.action.opportunity)
          returnRelatedActions (boolean, default False): Return related parent and child/sibbling actions
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: startDate | type | text
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/opportunities/{id}/actions", params=params, validate=validate))

    async def ai_assistant(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /opportunities/{id}/ai/assistant
        
        Submit uploaded files, a text description, contact actions and/or voice notes for asynchronous AI parsing.
        Returns immediately with a job ID. The parsing is processed in the background via RabbitMQ.
        The front-end receives an SSE event (`ai.parsing.done` or `ai.parsing.failed`) when processing completes.
        
        **Accepted file types**:
        * Documents (`files`): pdf, doc, docx, txt, ppt, pptx
        * Voice notes (`audio`): webm, mp4, ogg
        
        **Sources** (at least one required):
        * `files` — uploaded file references
        * `description` — free-text description
        * `actions` + `contact` — actions from a contact (max 5)
        * `audio` — voice note references
        
        **Limits**:
        * Maximum 10 documents per request
        * Maximum 5 voice notes per request
        * Maximum 5 actions per request
        * Maximum 100 MB total payload size
        * At least one source is required (files, description, actions or audio)
        
        Voice notes are forwarded to the AI provider as `audio[N]` multipart entries
        (separate from `files[N]`). They are deleted from storage once the
        opportunity has been successfully created — they are not kept as attachments
        on the resulting opportunity.
        
        **AI quota**: Each call consumes one AI request from the customer's quota.
        
        Request body schema: opportunitiesAiAssistantBody-post
        """
        return Document(await self._client.request("POST", f"/opportunities/{id}/ai/assistant", json=body, params=params, validate=validate))

    async def ai_matching(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /opportunities/{id}/ai/matching
        
        Get list of profile matching this opportunity
        """
        return Document(await self._client.request("GET", f"/opportunities/{id}/ai/matching", params=params, validate=validate))

    async def attached_flags(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /opportunities/{id}/attached-flags
        
        Get opportunity's attached flags
        """
        return Document(await self._client.request("GET", f"/opportunities/{id}/attached-flags", params=params, validate=validate))

    async def download(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /opportunities/{id}/download
        
        Get opportunity formatted file content
        
        Query params:
          language (string, one of: fr | en | es): Language used for the file content
          template (string): template ID
        """
        return Document(await self._client.request("GET", f"/opportunities/{id}/download", params=params, validate=validate))

    async def information(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /opportunities/{id}/information
        
        Get opportunity's information data
        """
        return Document(await self._client.request("GET", f"/opportunities/{id}/information", params=params, validate=validate))

    async def update_information(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /opportunities/{id}/information
        
        Update information data related to an opportunity
        
        Request body schema: opportunitiesInformationBody-put
        """
        return Document(await self._client.request("PUT", f"/opportunities/{id}/information", json=body, params=params, validate=validate))

    async def positionings(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /opportunities/{id}/positionings
        
        Get opportunity's positionings
        
        Query params:
          positioningStates (integer, repeatable): List of positioning states `id` to filter (described by /api/rest/application/dictionary/setting.state.positioning)
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: updateDate | resource.lastName | candidate.lastName | product.name | opportunity.title | state | opportunity.company.name | mainManager.lastName | resource.mainManager.lastName | candidate.mainManager.lastName | product.mainManager.lastName | opportunity.mainManager.lastName
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/opportunities/{id}/positionings", params=params, validate=validate))

    async def projects(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /opportunities/{id}/projects
        
        Get opportunity's projects
        
        Query params:
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: startDate | endDate | reference | mainManager.lastName
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/opportunities/{id}/projects", params=params, validate=validate))

    async def rights(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /opportunities/{id}/rights
        
        Get opportunity's rights
        
        Query params:
          contact (integer): Contact's `id` on which opportunity depends
        """
        return Document(await self._client.request("GET", f"/opportunities/{id}/rights", params=params, validate=validate))

    async def simulation(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /opportunities/{id}/simulation
        
        Get opportunity's simulation data
        """
        return Document(await self._client.request("GET", f"/opportunities/{id}/simulation", params=params, validate=validate))

    async def update_simulation(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /opportunities/{id}/simulation
        
        Update simulation data related to an opportunity
        
        Request body schema: opportunitiesSimulationBody-put
        """
        return Document(await self._client.request("PUT", f"/opportunities/{id}/simulation", json=body, params=params, validate=validate))

    async def tasks(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /opportunities/{id}/tasks
        
        Get opportunity's tasks
        """
        return Document(await self._client.request("GET", f"/opportunities/{id}/tasks", params=params, validate=validate))



class OrdersAPI:
    """Endpoints under /orders."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /orders
        
        Search orders
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/orders.csv?keywords=BDC1*
        
        Query params:
          keywords (string): If `keywords = BDC**ID1** PRJ**ID2** CCON**ID3** CSOC**ID4**` then orders
          projectTypes (integer, repeatable): List of project types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.project)
          paymentMethods (integer, repeatable): List of payment methods `id` to filter (described by /api/rest/application/dictionary/setting.paymentMethod)
          states (integer, repeatable): List of order states `id` to filter (described by /api/rest/application/dictionary/setting.state.order)
          companies (integer, repeatable): List of companies `id` on which order item depends
          customerAgreement (boolean): If `true` returns only received customer agreement, if `false` returns pending customer agreement
          billableItemTypes (integer, repeatable): List of billable item typesOf `id` to filter (described by /api/rest/application/dictionary/models.billableitem.attributes.typeOf)
          exceededOrderedTurnover (boolean): If `true` returns only ordered turnover exceeded, if `false` returns only ordered turnover not exceeded
          period (string): * `created` : Orders created between `startDate` and `endDate` are filtered
          periodDynamic (string): * `today` : Orders filtered according to the grid for today's period
          periodDynamicParameters (string): Filter parameters of dynamic period. Used when periodDynamic is "lastCustomPeriod" or "nextCustomPeriod"
          startDate (string): Start date
          endDate (string): End date
          flags (integer, repeatable): Orders attached to this flag whom flag's unique identifier = integer are filtered
          encoding (string): If the output format is **csv** then **encoding** filter should be one of
          columns (string, repeatable): List of columns
          appEntityFields (string, repeatable): List of app entity responses filtered by `<appId>_<fieldId>:<responseValue>` and with html characters encoded
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: date | number | state | project.reference | customerAgreement | turnoverInvoicedExcludingTax | turnoverOrderedExcludingTax | deltaInvoicedExcludingTax | project.company.name | mainManager.lastName | intermediaryCompany.name | exceededOrderedTurnover
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/orders", params=params, validate=validate))

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /orders
        
        Create an order
        
        Request body schema: ordersBody-post
        """
        return Document(await self._client.request("POST", "/orders", json=body, params=params, validate=validate))

    async def default(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /orders/default
        
        Get empty order's default information data
        
        Query params:
          project (integer, REQUIRED): Project's `id` on which order depends
          deliveries (integer, repeatable): List of deliveries `id`
          purchases (integer, repeatable): List of purchases `id`
        """
        return Document(await self._client.request("GET", "/orders/default", params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /orders/{id}
        
        Delete the order
        """
        return Document(await self._client.request("DELETE", f"/orders/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /orders/{id}
        
        Get order's basic data
        """
        return Document(await self._client.request("GET", f"/orders/{id}", params=params, validate=validate))

    async def actions(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /orders/{id}/actions
        
        Get order's actions
        
        Query params:
          actionTypes (integer, repeatable): List of action types `id`, related to the action's order, to filter (described by /api/rest/application/dictionary/setting.action.order)
          returnRelatedActions (boolean, default False): Return related parent and child/sibbling actions
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: startDate | type | text
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/orders/{id}/actions", params=params, validate=validate))

    async def attached_flags(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /orders/{id}/attached-flags
        
        Get order's attached flags
        """
        return Document(await self._client.request("GET", f"/orders/{id}/attached-flags", params=params, validate=validate))

    async def download(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /orders/{id}/download
        
        Get order formatted file content
        
        Query params:
          language (string, one of: fr | en | es): Language used for the file content
          template (string): template ID
        """
        return Document(await self._client.request("GET", f"/orders/{id}/download", params=params, validate=validate))

    async def information(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /orders/{id}/information
        
        Get order's information data
        """
        return Document(await self._client.request("GET", f"/orders/{id}/information", params=params, validate=validate))

    async def update_information(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /orders/{id}/information
        
        Update information data related to an order
        
        Request body schema: ordersInformationBody-put
        """
        return Document(await self._client.request("PUT", f"/orders/{id}/information", json=body, params=params, validate=validate))

    async def invoices(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /orders/{id}/invoices
        
        Get order's invoices
        
        Query params:
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/orders/{id}/invoices", params=params, validate=validate))

    async def rights(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /orders/{id}/rights
        
        Get order's rights
        
        Query params:
          project (integer): Project's `id` on which order depends
          deliveries (integer, repeatable): List of deliveries `id`
          purchases (integer, repeatable): List of purchases `id`
        """
        return Document(await self._client.request("GET", f"/orders/{id}/rights", params=params, validate=validate))

    async def tasks(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /orders/{id}/tasks
        
        Get order's tasks
        """
        return Document(await self._client.request("GET", f"/orders/{id}/tasks", params=params, validate=validate))



class PaymentsAPI:
    """Endpoints under /payments."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /payments
        
        Search payments
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/payments.csv?keywords=ACH1*
        
        Query params:
          keywords (string): If `keywords = ACH**ID1** CCON**ID2** CSOC**ID3** PRJ**ID4** COMP**ID5**` then payments
          subscriptionTypes (integer, repeatable): List of subscription types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.subscription)
          purchaseTypes (integer, repeatable): List of purchase types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.purchase)
          paymentStates (integer, repeatable): List of payment states `id` to filter (described by /api/rest/application/dictionary/setting.state.payment)
          paymentMethods (integer, repeatable): List of payment methods `id` to filter (described by /api/rest/application/dictionary/setting.paymentMethod)
          period (string): * `created` : Payments created between `startDate` and `endDate` are filtered
          periodDynamic (string): * `today` : Payments filtered according to the grid for today's period
          periodDynamicParameters (string): Filter parameters of dynamic period. Used when periodDynamic is "lastCustomPeriod" or "nextCustomPeriod"
          startDate (string): Start date
          endDate (string): End date
          flags (integer, repeatable): Purchases attached to this flag whom flag's unique identifier = integer are filtered
          encoding (string): If the output format is **csv** then **encoding** filter should be one of
          exportToDownloadCenter (boolean, default False): Export payments documents to the download center
          deliveryPurchases (boolean): include or exclude payments from purchases linked to a delivery if defined
          columns (string, repeatable): List of columns
          excludeProviderInvoice (boolean, default False): Exclude payment with provider invoice from result
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: expectedDate | performedDate | state | date | purchase.title | project.reference | purchase.company.name | mainManager.lastName
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/payments", params=params, validate=validate))

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /payments
        
        Create a payment
        
        Request body schema: paymentsBody-post
        """
        return Document(await self._client.request("POST", "/payments", json=body, params=params, validate=validate))

    async def default(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /payments/default
        
        Get empty payment's default basic data
        
        Query params:
          purchase (integer, REQUIRED): Purchase's `id` on which payment depends
          term (string): Start month
        """
        return Document(await self._client.request("GET", "/payments/default", params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /payments/{id}
        
        Delete the payment
        """
        return Document(await self._client.request("DELETE", f"/payments/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /payments/{id}
        
        Get payment's basic data
        """
        return Document(await self._client.request("GET", f"/payments/{id}", params=params, validate=validate))

    async def update(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /payments/{id}
        
        Update basic data related to a payment
        
        Request body schema: paymentsBody-put
        """
        return Document(await self._client.request("PUT", f"/payments/{id}", json=body, params=params, validate=validate))

    async def rights(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /payments/{id}/rights
        
        Get payment's rights
        
        Query params:
          purchase (integer): Purchase's `id` on which payment depends
          term (string): Start month
        """
        return Document(await self._client.request("GET", f"/payments/{id}/rights", params=params, validate=validate))

    async def tasks(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /payments/{id}/tasks
        
        Get payment's tasks
        """
        return Document(await self._client.request("GET", f"/payments/{id}/tasks", params=params, validate=validate))



class PlanningAbsencesAPI:
    """Endpoints under /planning-absences."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /planning-absences
        
        Search planning absences
        
        Query params:
          startDate (string, REQUIRED): Start date
          endDate (string, REQUIRED): End date
          keywords (string): If `keywordsType` is not defined & `keywords = COMP**ID1** COMP**ID2**` then resources
          resourceTypes (integer, repeatable): List of resource types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.resource)
          resourceStates (integer, repeatable): List of resource states `id` to filter (described by /api/rest/application/dictionary/setting.state.resource)
          period (string, one of: allResources | withAbsences | withoutAbsences | present, default withAbsences): Period type
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: lastName
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/planning-absences", params=params, validate=validate))



class PolesAPI:
    """Endpoints under /poles."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /poles
        
        Search poles
        """
        return Document(await self._client.request("GET", "/poles", params=params, validate=validate))

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /poles
        
        Create a pole
        
        Request body schema: polesBody-post
        """
        return Document(await self._client.request("POST", "/poles", json=body, params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /poles/{id}
        
        Delete the pole
        """
        return Document(await self._client.request("DELETE", f"/poles/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /poles/{id}
        
        Get pole's basic data
        """
        return Document(await self._client.request("GET", f"/poles/{id}", params=params, validate=validate))

    async def update(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /poles/{id}
        
        Update basic data related to a pole
        
        Request body schema: polesBody-put
        """
        return Document(await self._client.request("PUT", f"/poles/{id}", json=body, params=params, validate=validate))



class PositioningsAPI:
    """Endpoints under /positionings."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /positionings
        
        Search positionings
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/positionings.csv?keywords=POS100*
        
        Query params:
          keywords (string): If `keywords = AO**ID1** PROD**ID2** CAND**ID3** COMP**ID4** CCON**ID5** CSOC**ID6** POS**ID7**` then positionings
          perimeterManagersType (string, default opportunities): - `opportunities`: The filter **perimeterManagers** is used only on the **Main Manager** or **hrManagers** of opportunities
          positioningType (string, default resourcesOrCandidates): - `resourcesOrCandidates`: Resources or Candidates are filtered
          entityTypes (integer, repeatable): * If `positioningType = resourcesOrCandidates` : List of resource types `id` or candidate types (prefix with `9_id`) to filter (where `id` is described by /api/rest/application/dictionary/setting.typeOf.resource)
          opportunityTypes (integer, repeatable): List of opportunity types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.project)
          positioningStates (integer, repeatable): List of positioning states `id` to filter (described by /api/rest/application/dictionary/setting.state.positioning)
          opportunityStates (integer, repeatable): List of opportunity states `id` to filter (described by /api/rest/application/dictionary/setting.state.opportunity)
          returnMoreData (string, repeatable): Returns the following attributes or relationships, if specified and user is allowed to
          period (string): * `created` : Positionings created between `startDate` and `endDate` are filtered
          periodDynamic (string): * `today` : Positionings filtered according to the grid for today's period
          periodDynamicParameters (string): Filter parameters of dynamic period. Used when periodDynamic is "lastCustomPeriod" or "nextCustomPeriod"
          startDate (string): Start date
          endDate (string): End date
          flags (integer, repeatable): Positionings attached to this flag whom flag's unique identifier = integer are filtered
          columns (string, repeatable): List of columns
          encoding (string): If the output format is **csv** then **encoding** filter should be one of
          shields (string, repeatable): Filter positionings by their shield status (conditional fields completion level)
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: updateDate | dependsOn.lastName | dependsOn.name | opportunity.title | state | opportunity.company.name | mainManager.lastName | dependsOn.mainManager.lastName | opportunity.mainManager.lastName
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/positionings", params=params, validate=validate))

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /positionings
        
        Create a positioning.
        
        If state is `won` it will attach this positioning to a new project or an existing one.
        
        Query params:
          sendMailToDependsOnManager (boolean): If `true` to send an email
          sendMailToOpportunityManager (boolean): If `true` to send an email
        
        Request body schema: positioningsBody-post
        """
        return Document(await self._client.request("POST", "/positionings", json=body, params=params, validate=validate))

    async def update_bulk_update(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /positionings/bulk-update
        
        Bulk update positionings
        
        Query params:
          positioningType (string, default resourcesOrCandidates): - `resourcesOrCandidates`: Resources or Candidates are filtered
        
        Request body schema: positioningsBulkUpdateBody-put
        """
        return Document(await self._client.request("PUT", "/positionings/bulk-update", json=body, params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /positionings/{id}
        
        Delete the positioning
        """
        return Document(await self._client.request("DELETE", f"/positionings/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /positionings/{id}
        
        Get positioning's basic data
        """
        return Document(await self._client.request("GET", f"/positionings/{id}", params=params, validate=validate))

    async def update(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /positionings/{id}
        
        Update basic data related to a positioning.
        
        If state is `won` it will attach this positioning to a new project or an existing one.
        
        If the user has no right to create a project, a candidate positioning on a non-recruitment
        opportunity can only be set to `won` if the candidate is hired — otherwise the request is
        rejected with error `3300`.
        
        Request body schema: positioningsBody-put
        """
        return Document(await self._client.request("PUT", f"/positionings/{id}", json=body, params=params, validate=validate))

    async def attached_flags(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /positionings/{id}/attached-flags
        
        Get positioning's attached flags
        """
        return Document(await self._client.request("GET", f"/positionings/{id}/attached-flags", params=params, validate=validate))

    async def rights(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /positionings/{id}/rights
        
        Get positioning's rights
        """
        return Document(await self._client.request("GET", f"/positionings/{id}/rights", params=params, validate=validate))

    async def tasks(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /positionings/{id}/tasks
        
        Get positioning's tasks
        """
        return Document(await self._client.request("GET", f"/positionings/{id}/tasks", params=params, validate=validate))



class ProductsAPI:
    """Endpoints under /products."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /products
        
        Search products
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/products.csv?keywords=PROD100*
        
        Query params:
          keywords (string): If `keywords = PROD**ID1** PROD**ID2**` then products
          productStates (integer, repeatable): List of product states `id` to filter (described by /api/rest/application/dictionary/setting.state.product)
          productTypes (integer, repeatable): List of product types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.subscription)
          flags (integer, repeatable): Products attached to this flag whom flag's unique identifier = integer are filtered
          period (string): * `<appId>_running` : App entities whose the period field between `startDate` and `endDate` are filtered
          periodDynamic (string): * `today` : Orders filtered according to the grid for today's period
          periodDynamicParameters (string): Filter parameters of dynamic period. Used when periodDynamic is "lastCustomPeriod" or "nextCustomPeriod"
          startDate (string): Start date
          endDate (string): End date
          encoding (string): If the output format is **csv** then **encoding** filter should be one of
          appEntityFields (string, repeatable): List of app entity responses filtered by `<appId>_<fieldId>:<responseValue>` and with html characters encoded
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: reference | name | type | priceExcludingTax | mainManager.lastName
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/products", params=params, validate=validate))

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /products
        
        Create a product
        
        Request body schema: productsBody-post
        """
        return Document(await self._client.request("POST", "/products", json=body, params=params, validate=validate))

    async def default(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /products/default
        
        Get empty product's default information data
        """
        return Document(await self._client.request("GET", "/products/default", params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /products/{id}
        
        Delete the product
        """
        return Document(await self._client.request("DELETE", f"/products/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /products/{id}
        
        Get product's basic data
        """
        return Document(await self._client.request("GET", f"/products/{id}", params=params, validate=validate))

    async def attached_flags(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /products/{id}/attached-flags
        
        Get product's attached flags
        """
        return Document(await self._client.request("GET", f"/products/{id}/attached-flags", params=params, validate=validate))

    async def information(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /products/{id}/information
        
        Get product's information data
        """
        return Document(await self._client.request("GET", f"/products/{id}/information", params=params, validate=validate))

    async def update_information(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /products/{id}/information
        
        Update information data related to a product
        
        Request body schema: productsInformationBody-put
        """
        return Document(await self._client.request("PUT", f"/products/{id}/information", json=body, params=params, validate=validate))

    async def opportunities(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /products/{id}/opportunities
        
        Get product's opportunities
        
        Query params:
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: creationDate | title | state | totalWeightedTurnOverExcludingTax | company.name | mainManager.lastName
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/products/{id}/opportunities", params=params, validate=validate))

    async def projects(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /products/{id}/projects
        
        Get product's projects
        
        Query params:
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: startDate | endDate | reference | company.name | mainManager.lastName
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/products/{id}/projects", params=params, validate=validate))

    async def rights(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /products/{id}/rights
        
        Get product's rights
        """
        return Document(await self._client.request("GET", f"/products/{id}/rights", params=params, validate=validate))

    async def tasks(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /products/{id}/tasks
        
        Get product's tasks
        """
        return Document(await self._client.request("GET", f"/products/{id}/tasks", params=params, validate=validate))



class ProjectsAPI:
    """Endpoints under /projects."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /projects
        
        Search projects
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/projects.csv?keywords=PRJ100*
        
        Query params:
          keywords (string): If `keywords = PRJ**ID1** MIS**ID2** COMP**ID3** CCON**ID4** CSOC**ID5** AO**ID6** PROD**ID7** CTR**ID8**` then projects
          projectTypes (integer, repeatable): List of project types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.project)
          projectStates (integer, repeatable): List of project states `id` to filter (described by /api/rest/application/dictionary/setting.state.project)
          period (string): * `created` : Projects created between `startDate` and `endDate`  are filtered
          periodDynamic (string): * `today` : Projects filtered according to the grid for today's period
          periodDynamicParameters (string): Filter parameters of dynamic period. Used when periodDynamic is "lastCustomPeriod" or "nextCustomPeriod"
          startDate (string): Start date
          endDate (string): End date
          expertiseAreas (string, repeatable): List of expertise areas `id` to filter (described by /api/rest/application/dictionary/setting.expertiseArea)
          activityAreas (string): List of activity areas `id` to filter (described by /api/rest/application/dictionary/setting.activityArea)
          flags (integer, repeatable): Projects attached to this flag whom flag's unique identifier = integer are filtered
          companies (integer, repeatable): List of companies `id` on which project item depends
          columns (string, repeatable): List of columns
          encoding (string): If the output format is **csv** then **encoding** filter should be one of
          appEntityFields (string, repeatable): List of app entity responses filtered by `<appId>_<fieldId>:<responseValue>` and with html characters encoded
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: startDate | endDate | reference | company.name | mainManager.lastName | intermediaryCompany.name
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/projects", params=params, validate=validate))

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /projects
        
        Create a project which mode is only 'product' or `fixed'
        
        Request body schema: projectsBody-post
        """
        return Document(await self._client.request("POST", "/projects", json=body, params=params, validate=validate))

    async def carts(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /projects/carts
        
        Get project's carts
        
        Query params:
          projects (integer, repeatable): List of projects `id` on which billable item depends
          cartStates (integer, repeatable): List of cart states `id` to filter
          projectTypes (integer, repeatable): List of project types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.project)
          projectStates (integer, repeatable): List of project states `id` to filter (described by /api/rest/application/dictionary/setting.state.project)
          orderTypeOf (integer, repeatable): List of order typeOf to filter
          customerAgreement (boolean): If `true` returns only received customer agreement, if `false` returns pending customer agreement
          startDate (string): Start date
          endDate (string): End date
          untilDate (string): search project having billable items until this date (default is today)
          companies (integer, repeatable): List of companies `id` on which billable item depends
          perimeterManagersType (string, default opportunities): - `projects`: The filter **perimeterManagers** is used only on the **Main Manager** of projects
          exceededOrderedTurnover (boolean): If `true` returns only ordered turnover exceeded, if `false` returns only ordered turnover not exceeded
          period (string): * `billing` : Carts whose billing period is between `startDate` and `endDate` are filtered
          periodDynamic (string): * `today` : Carts filtered according to the grid for today's period
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: reference | company.name
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/projects/carts", params=params, validate=validate))

    async def carts_widgets(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /projects/carts/widgets
        
        Get project's carts
        
        Query params:
          projects (integer, repeatable): List of projects `id` on which billable item depends
          projectTypes (integer, repeatable): List of project types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.project)
          projectStates (integer, repeatable): List of project states `id` to filter (described by /api/rest/application/dictionary/setting.state.project)
          customerAgreement (boolean): If `true` returns only received customer agreement, if `false` returns pending customer agreement
          startDate (string): Start date
          endDate (string): End date
          untilDate (string): search project having billable items until this date (default is today)
          companies (integer, repeatable): List of companies `id` on which billable item depends
          perimeterManagersType (string, default opportunities): - `projects`: The filter **perimeterManagers** is used only on the **Main Manager** of projects
          exceededOrderedTurnover (boolean): If `true` returns only ordered turnover exceeded, if `false` returns only ordered turnover not exceeded
          period (string): * `billing` : Carts whose billing period is between `startDate` and `endDate` are filtered
          periodDynamic (string): * `today` : Carts filtered according to the grid for today's period
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: reference | company.name
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/projects/carts/widgets", params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /projects/{id}
        
        Delete the project
        """
        return Document(await self._client.request("DELETE", f"/projects/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /projects/{id}
        
        Get project's basic data
        """
        return Document(await self._client.request("GET", f"/projects/{id}", params=params, validate=validate))

    async def actions(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /projects/{id}/actions
        
        Get project's actions
        
        Query params:
          actionTypes (integer, repeatable): List of action types `id`, related to the action's project, to filter (described by /api/rest/application/dictionary/setting.action.project and /api/rest/application/dictionary/setting.collaborative.project)
          returnRelatedActions (boolean, default False): Return related parent and child/sibbling actions
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: startDate | type | text
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/projects/{id}/actions", params=params, validate=validate))

    async def advantages(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /projects/{id}/advantages
        
        Get project's advantages
        
        Query params:
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: updateDate | resource.lastName | candidate.lastName | product.name | state
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/projects/{id}/advantages", params=params, validate=validate))

    async def attached_flags(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /projects/{id}/attached-flags
        
        Get project's attached flags
        """
        return Document(await self._client.request("GET", f"/projects/{id}/attached-flags", params=params, validate=validate))

    async def batches_markers(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /projects/{id}/batches-markers
        
        Get project's batches & markers data
        """
        return Document(await self._client.request("GET", f"/projects/{id}/batches-markers", params=params, validate=validate))

    async def update_batches_markers(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /projects/{id}/batches-markers
        
        Update batches & markers data related to a project
        
        Request body schema: projectsBatchesMarkersBody-put
        """
        return Document(await self._client.request("PUT", f"/projects/{id}/batches-markers", json=body, params=params, validate=validate))

    async def deliveries_groupments(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /projects/{id}/deliveries-groupments
        
        Get project's deliveries & groupments
        
        Query params:
          notProductDependsOn (boolean): If 'true' only delivery and groupment depending 'Resource'
          dependsOn (string, repeatable, one of: 0 | 1 | 5 | 6 | 7): * - `0` : Delivery with a resource
          sort (string, repeatable): Order by a given column: startDate | endDate | id | groupment.id | resource.lastName | candidate.lastName | product.name | state
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/projects/{id}/deliveries-groupments", params=params, validate=validate))

    async def information(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /projects/{id}/information
        
        Get project's information data
        """
        return Document(await self._client.request("GET", f"/projects/{id}/information", params=params, validate=validate))

    async def update_information(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /projects/{id}/information
        
        Update information data related to a project
        
        Request body schema: projectsInformationBody-put
        """
        return Document(await self._client.request("PUT", f"/projects/{id}/information", json=body, params=params, validate=validate))

    async def orders(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /projects/{id}/orders
        
        Get project's orders
        
        Query params:
          sort (string, repeatable): Order by a given column: date | startDate | endDate | reference | state | customerAgreement | turnoverInvoicedExcludingTax | turnoverOrderedExcludingTax | deltaInvoicedExcludingTax
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/projects/{id}/orders", params=params, validate=validate))

    async def productivity(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /projects/{id}/productivity
        
        Get projects's productivity data
        """
        return Document(await self._client.request("GET", f"/projects/{id}/productivity", params=params, validate=validate))

    async def purchases(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /projects/{id}/purchases
        
        Get projects's purchases
        
        Query params:
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: title | state | date
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/projects/{id}/purchases", params=params, validate=validate))

    async def rights(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /projects/{id}/rights
        
        Get project's rights
        """
        return Document(await self._client.request("GET", f"/projects/{id}/rights", params=params, validate=validate))

    async def simulation(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /projects/{id}/simulation
        
        Get project's simulation data
        """
        return Document(await self._client.request("GET", f"/projects/{id}/simulation", params=params, validate=validate))

    async def update_simulation(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /projects/{id}/simulation
        
        Update simulation data related to a project
        
        Request body schema: projectsSimulationBody-put
        """
        return Document(await self._client.request("PUT", f"/projects/{id}/simulation", json=body, params=params, validate=validate))

    async def tasks(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /projects/{id}/tasks
        
        Get project's tasks
        """
        return Document(await self._client.request("GET", f"/projects/{id}/tasks", params=params, validate=validate))



class ProviderInvoicesAPI:
    """Endpoints under /provider-invoices."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /provider-invoices
        
        Search provider invoices
        
        Query params:
          keywords (string): If `keywords = COMP**ID1**` then provider invoices
          columns (string, repeatable): List of columns
          exportToDownloadCenter (string): Export provider invoices to the download center along with or without the attached documents
          exportFormat (string): Export format when exportToDownloadCenter is set
          startDate (string): Start date
          endDate (string): End date
          period (string): * `invoiceDate` : Provider invoice invoice date in `startDate` and `endDate`are filtered
          periodDynamic (string): * `today` : Resources filtered according to the grid for today's period
          periodDynamicParameters (string): Filter parameters of dynamic period. Used when periodDynamic is "lastCustomPeriod" or "nextCustomPeriod"
          amountCurrency (integer): Currency `id` to filter (described by /api/rest/application/dictionary/setting.currency)
          amountType (string): * `equal` : Provider invoices `amountColumn` equal to `amount`
          amountColumn (string): * `amountExcludingTax` : Provider invoices amount filtered by `amountExcludingTax` column
          amount (number): Provider invoices `amountColumn` equal to `amount`
          amountMin (number): Provider invoices `amountColumn` superior or equal to `amountMin`
          amountMax (number): Provider invoices `amountColumn` inferior or equal to `amountMax`
          sources (integer, repeatable): List of provider invoice source to filter
          companies (integer, repeatable): List of companies `id` on which billable item depends
          withoutCompany (boolean): If true, only provider invoices without company are returned
          resources (integer, repeatable): List of resources unique identifier on which provider invoices are filtered.
          withoutResource (boolean): If true, only provider invoices without resource associated are returned
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: startDate | endDate | invoiceDate | state
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/provider-invoices", params=params, validate=validate))

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /provider-invoices
        
        Create a provider invoice
        
        Request body schema: providerInvoicesBody-post
        """
        return Document(await self._client.request("POST", "/provider-invoices", json=body, params=params, validate=validate))

    async def default(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /provider-invoices/default
        
        Get empty provider invoice's default basic data
        
        Query params:
          resource (integer): Resource's `id` on which provider invoice depends
        """
        return Document(await self._client.request("GET", "/provider-invoices/default", params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /provider-invoices/{id}
        
        Delete the provider invoice
        """
        return Document(await self._client.request("DELETE", f"/provider-invoices/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /provider-invoices/{id}
        
        Get provider invoice's basic data
        """
        return Document(await self._client.request("GET", f"/provider-invoices/{id}", params=params, validate=validate))

    async def update(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /provider-invoices/{id}
        
        Update provider invoice's basic data
        
        Request body schema: providerInvoicesBody-put
        """
        return Document(await self._client.request("PUT", f"/provider-invoices/{id}", json=body, params=params, validate=validate))

    async def activity_expenses(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /provider-invoices/{id}/activity-expenses
        
        Get provider invoice's activity expenses
        
        Query params:
          startDate (string): Start date
          endDate (string): End date
        """
        return Document(await self._client.request("GET", f"/provider-invoices/{id}/activity-expenses", params=params, validate=validate))

    async def rights(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /provider-invoices/{id}/rights
        
        Get provider invoice's rights
        """
        return Document(await self._client.request("GET", f"/provider-invoices/{id}/rights", params=params, validate=validate))



class PurchasesAPI:
    """Endpoints under /purchases."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /purchases
        
        Search purchases
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/purchases.csv?keywords=ACH1*
        
        Query params:
          keywords (string): If `keywords = ACH**ID1** CCON**ID2** CSOC**ID3** PRJ**ID4** COMP**ID5**` then purchases
          subscriptionTypes (integer, repeatable): List of subscription types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.subscription)
          purchaseStates (integer, repeatable): List of purchase states `id` to filter (described by /api/rest/application/dictionary/setting.state.purchase)
          purchaseTypes (integer, repeatable): List of purchase types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.purchase)
          paymentMethods (integer, repeatable): List of payment methods `id` to filter (described by /api/rest/application/dictionary/setting.paymentMethod)
          period (string): * `created` : Purchases created between `startDate` and `endDate`  are filtered
          periodDynamic (string): * `today` : Purchases filtered according to the grid for today's period
          periodDynamicParameters (string): Filter parameters of dynamic period. Used when periodDynamic is "lastCustomPeriod" or "nextCustomPeriod"
          startDate (string): Start date
          endDate (string): End date
          flags (integer, repeatable): Purchases attached to this flag whom flag's unique identifier = integer are filtered
          encoding (string): If the output format is **csv** then **encoding** filter should be one of
          exportToDownloadCenter (boolean, default False): Export purchases formatted file to the download center
          deliveryPurchases (boolean): include or exclude purchases linked to a delivery if defined
          columns (string, repeatable): List of columns
          appEntityFields (string, repeatable): List of app entity responses filtered by `<appId>_<fieldId>:<responseValue>` and with html characters encoded
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: title | state | date | project.reference | company.name | mainManager.lastName
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/purchases", params=params, validate=validate))

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /purchases
        
        Create a purchase
        
        Request body schema: purchasesBody-post
        """
        return Document(await self._client.request("POST", "/purchases", json=body, params=params, validate=validate))

    async def default(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /purchases/default
        
        Get empty purchase's default information data
        
        Query params:
          project (integer): Project's `id` on which purchase depends
          delivery (integer): Delivery's `id` on which purchase depends
          additionalTurnoverAndCosts (integer): Additional turnover and costs `id` on which purchase depends
          contact (integer): Contact's `id` on which purchase depends
          company (integer): Company's `id` on which purchase depends
        """
        return Document(await self._client.request("GET", "/purchases/default", params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /purchases/{id}
        
        Delete the purchase
        """
        return Document(await self._client.request("DELETE", f"/purchases/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /purchases/{id}
        
        Get purchase's basic data
        """
        return Document(await self._client.request("GET", f"/purchases/{id}", params=params, validate=validate))

    async def attached_flags(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /purchases/{id}/attached-flags
        
        Get purchase's attached flags
        """
        return Document(await self._client.request("GET", f"/purchases/{id}/attached-flags", params=params, validate=validate))

    async def download(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /purchases/{id}/download
        
        Get purchase formatted file content
        
        Query params:
          language (string, one of: fr | en | es): Language used for the file content
          template (string): template ID
        """
        return Document(await self._client.request("GET", f"/purchases/{id}/download", params=params, validate=validate))

    async def information(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /purchases/{id}/information
        
        Get purchase's information data
        """
        return Document(await self._client.request("GET", f"/purchases/{id}/information", params=params, validate=validate))

    async def update_information(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /purchases/{id}/information
        
        Update information data related to a purchase
        
        Request body schema: purchasesInformationBody-put
        """
        return Document(await self._client.request("PUT", f"/purchases/{id}/information", json=body, params=params, validate=validate))

    async def payments(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /purchases/{id}/payments
        
        Get purchase's payments
        
        Query params:
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: expectedDate | performedDate | state | creationDate | project.reference | company.name
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/purchases/{id}/payments", params=params, validate=validate))

    async def rights(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /purchases/{id}/rights
        
        Get purchase's rights
        
        Query params:
          project (integer): Project's `id` on which purchase depends
          additionalTurnoverAndCosts (integer): Additional turnover and costs `id` on which purchase depends
          contact (integer): Contact's `id` on which purchase depends
        """
        return Document(await self._client.request("GET", f"/purchases/{id}/rights", params=params, validate=validate))

    async def simulation(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /purchases/{id}/simulation
        
        Get purchase's simulation
        """
        return Document(await self._client.request("GET", f"/purchases/{id}/simulation", params=params, validate=validate))

    async def tasks(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /purchases/{id}/tasks
        
        Get purchase's tasks
        """
        return Document(await self._client.request("GET", f"/purchases/{id}/tasks", params=params, validate=validate))



class ReportingCompaniesAPI:
    """Endpoints under /reporting-companies."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /reporting-companies
        
        Search companies reporting
        
        Query params:
          startDate (string, REQUIRED): Start date
          endDate (string, REQUIRED): End date
          companiesStates (integer, repeatable): List of companies states `id` to filter (described by /api/rest/application/dictionary/setting.state.company)
          maxCompanies (number, default 1): number of companies per page (number of results will be a multiplication of companies and indicators)
          showPercentage (boolean, default False): Show percentage or real value's type
          companies (integer, repeatable): List of companies `id`
          periodDynamic (string): * `today` : Reporting filtered according to the grid for today's period
          periodDynamicParameters (string): Filter parameters of dynamic period. Used when periodDynamic is "lastCustomPeriod" or "nextCustomPeriod"
          scorecards (string, repeatable): List of scorecard to filter.
          useCache (string, default withoutCache): * `withoutCache` : Returns actual data.
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: name
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/reporting-companies", params=params, validate=validate))



class ReportingProductionPlansAPI:
    """Endpoints under /reporting-production-plans."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /reporting-production-plans
        
        Search production plans reporting
        
        Query params:
          startDate (string, REQUIRED): Start date
          endDate (string, REQUIRED): End date
          keywords (string): If `keywordsType` is not defined & `keywords = COMP**ID1** COMP**ID2**` then resources
          resourceTypes (integer, repeatable): List of resource types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.resource)
          resourceStates (integer, repeatable): List of resource states `id` to filter (described by /api/rest/application/dictionary/setting.state.resource)
          positioningStates (integer, repeatable): List of positioning states `id` to filter (described by /api/rest/application/dictionary/setting.state.positioning)
          positioningPeriod (string, default created): * `created` : Positionings created between `startDate` and `endDate` are filtered
          periodDynamic (string): * `today` : Reporting filtered according to the grid for today's period
          periodDynamicParameters (string): Filter parameters of dynamic period. Used when periodDynamic is "lastCustomPeriod" or "nextCustomPeriod"
          showContracts (boolean, default False): If true then return contracts
          projects (integer, repeatable): List of projects `id`
          contacts (integer, repeatable): List of contacts `id`
          companies (integer, repeatable): List of companies `id`
          availabilityStatus (string, repeatable): List of availability status (only available for advanced/enterprise offers)
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: lastName | firstName | availability
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/reporting-production-plans", params=params, validate=validate))



class ReportingProjectsAPI:
    """Endpoints under /reporting-projects."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /reporting-projects
        
        Search projects reporting
        
        Query params:
          projectTypes (integer, repeatable): List of project types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.project)
          projectStates (integer, repeatable): List of project states `id` to filter (described by /api/rest/application/dictionary/setting.state.project)
          maxProjects (number, default 1): number of projects per page (number of results will be a multiplication of projects and indicators)
          startDate (string): Start date
          endDate (string): End date
          resources (integer, repeatable): List of resources `id`
          projects (integer, repeatable): List of projects `id`
          contacts (integer, repeatable): List of contacts `id`
          companies (integer, repeatable): List of companies `id`
          periodDynamic (string): * `today` : Reporting filtered according to the grid for today's period
          periodDynamicParameters (string): Filter parameters of dynamic period. Used when periodDynamic is "lastCustomPeriod" or "nextCustomPeriod"
          scorecards (string, repeatable): List of scorecard to filter.
          useCache (string, default withoutCache): * `withoutCache` : Returns actual data.
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: reference
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/reporting-projects", params=params, validate=validate))



class ReportingResourcesAPI:
    """Endpoints under /reporting-resources."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /reporting-resources
        
        Search resources reporting
        
        Query params:
          reportingCategory (string, default showByResources): * `showByResources` : In this category, `returnedPeriod` are not available.
          maxResources (number, default 1): number of resources per page (number of results will be a multiplication of resources and indicators)
          resourceTypes (integer, repeatable): List of resource types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.resource)
          resourceStates (integer, repeatable): List of resource states `id` to filter (described by /api/rest/application/dictionary/setting.state.resource)
          period (string): * `onePeriod` : Reporting are returned following a unique period between `startDate` and `endDate`
          periodDynamic (string): * `today` : Reporting filtered according to the grid for today's period
          periodDynamicParameters (string): Filter parameters of dynamic period. Used when periodDynamic is "lastCustomPeriod" or "nextCustomPeriod"
          startDate (string): Start date
          endDate (string): End date
          resources (integer, repeatable): List of resources `id`
          projects (integer, repeatable): List of projects `id`
          contacts (integer, repeatable): List of contacts `id`
          companies (integer, repeatable): List of companies `id`
          scorecards (integer, repeatable): List of scorecard to filter.
          useCache (string, default withoutCache): * `withoutCache` : Returns actual data.
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: lastName
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/reporting-resources", params=params, validate=validate))



class ReportingSynthesisAPI:
    """Endpoints under /reporting-synthesis."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /reporting-synthesis
        
        Search synthesis reporting
        
        Query params:
          startDate (string, REQUIRED): Start date
          reportingType (string, default realData): * `realData` : Reporting returns only real data
          reportingCategory (string, default commercialSynthesis): * `commercialSynthesis` : Reporting returns commercial data. In this category, `resourcesIds` is not available.
          period (string, default onePeriod): * `onePeriod` : Reporting are returned following a unique period between `startDate` and `endDate`
          periodDynamic (string): * `today` : Reporting filtered according to the grid for today's period
          periodDynamicParameters (string): Filter parameters of dynamic period. Used when periodDynamic is "lastCustomPeriod" or "nextCustomPeriod"
          endDate (string): End date
          resources (integer, repeatable): List of resources `id`
          projects (integer, repeatable): List of projects `id`
          contacts (integer, repeatable): List of contacts `id``
          companies (integer, repeatable): List of companies `id`
          scorecards (string, repeatable): List of scorecard to filter.
          useCache (string, default withoutCache): * `withoutCache` : Returns actual data.
          compareIndicators (string, repeatable): List of scorecard to compare.
          compareIndicatorsPeriod (string, default period): * `period` : Add indicators to compare with previous period.
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
        """
        return Document(await self._client.request("GET", "/reporting-synthesis", params=params, validate=validate))



class ResourcesAPI:
    """Endpoints under /resources."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /resources
        
        Search resources
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/resources.csv?keywords=COMP100*
        
        Query params:
          keywords (string): If `keywordsType` is not defined & `keywords = COMP**ID1** COMP**ID2**` then resources
          keywordsType (string, default resumeTd): * `resumeTd` : Resources are filtered following `keywords` found into their resumes and technical document
          returnMoreData (string, repeatable): Returns the following attributes or relationships, if specified and user is allowed to
          excludeResourceTypes (integer, repeatable): List of resource types `id` not filtered (described by /api/rest/application/dictionary/setting.typeOf.resource)
          resourceTypes (integer, repeatable): List of resource types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.resource)
          activityAreas (string, repeatable): List of activity areas `id` to filter (described by /api/rest/application/dictionary/setting.activityArea)
          expertiseAreas (string, repeatable): List of expertise areas `id` to filter (described by /api/rest/application/dictionary/setting.expertiseArea)
          tools (string, repeatable): List of tools `id` to filter (described by /api/rest/application/dictionary/setting.tool)
          mobilityAreas (string): List of mobility areas `id` to filter (described by /api/rest/application/dictionary/setting.mobilityArea)
          experiences (integer, repeatable): List of experiences `id` to filter (described by /api/rest/application/dictionary/setting.experience)
          trainings (string, repeatable): List of trainings `id` to filter (described by /api/rest/application/dictionary/setting.training)
          period (string): * `working` : Resources assigned to deliveries between `startDate` and `endDate` are filtered excluding internal projects
          periodActions (integer, repeatable): List of actions `id` (../bddboondmanager/classes/TAB_ACTION.html#property_ACTION_TYPE described by /api/rest/application/dictionary/setting.action.resource = integer
          periodDynamic (string): * `today` : Resources filtered according to the grid for today's period
          periodDynamicParameters (string): Filter parameters of dynamic period. Used when periodDynamic is "lastCustomPeriod" or "nextCustomPeriod"
          startDate (string): Start date
          endDate (string): End date
          flags (integer, repeatable): Resources attached to this flag whom flag's unique identifier = integer are filtered
          excludeResourceStates (integer, repeatable): List of resource state `id` not filtered (described by /api/rest/application/dictionary/setting.state.resource)
          resourceStates (integer, repeatable): List of resource states `id` to filter (described by /api/rest/application/dictionary/setting.state.resource)
          excludeManager (boolean, default False): if `true` only resources that do not have a manager account are filtered
          languages (string, repeatable): List of languages spoken `id` to filter (described by /api/rest/application/dictionary/setting.languageSpoken)
          columns (string, repeatable): List of columns
          onlyVisible (boolean, default True): The user has to have the global right `showGroupe` set to `true` or call this api into mode `god`.
          encoding (string): If the output format is **csv** then **encoding** filter should be one of
          providerCompanies (integer, repeatable): List of provider companies' `id` to filter
          coordinates (string): Geographic coordinates for proximity search, in the format `latitude,longitude`.
          location (string): Free-text address for geocoding-based proximity search (e.g. city name, address).
          geoDistance (integer): Search radius in kilometers for proximity search.
          availabilityStatus (string, repeatable): List of availability status (only available for advanced/enterprise offers)
          appEntityFields (string, repeatable): List of app entity responses filtered by `<appId>_<fieldId>:<responseValue>` and with html characters encoded
          shields (string, repeatable): Filter resources by their shield status (conditional fields completion level)
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: lastName | firstName | title | state | availability | numberOfActivePositionings | mainManager.lastName | priceExcludingTax | creationDate | updateDate | distance
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/resources", params=params, validate=validate))

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /resources
        
        Create a resource
        
        Request body schema: resourcesBody-post
        """
        return Document(await self._client.request("POST", "/resources", json=body, params=params, validate=validate))

    async def default(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /resources/default
        
        Get empty resource's default information data
        """
        return Document(await self._client.request("GET", "/resources/default", params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /resources/{id}
        
        Delete the resource
        """
        return Document(await self._client.request("DELETE", f"/resources/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /resources/{id}
        
        Get resource's basic data
        """
        return Document(await self._client.request("GET", f"/resources/{id}", params=params, validate=validate))

    async def absences_accounts(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /resources/{id}/absences-accounts
        
        Get resource's absences accounts
        """
        return Document(await self._client.request("GET", f"/resources/{id}/absences-accounts", params=params, validate=validate))

    async def absences_reports(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /resources/{id}/absences-reports
        
        Get resource's requests absences
        
        Query params:
          sort (string, repeatable): Order by a given column: creationDate | state
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/resources/{id}/absences-reports", params=params, validate=validate))

    async def actions(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /resources/{id}/actions
        
        Get resource's actions
        
        Query params:
          actionTypes (integer, repeatable): List of action types `id`, related to the action's resource, to filter (described by /api/rest/application/dictionary/setting.action.resource)
          returnRelatedActions (boolean, default False): Return related parent and child/sibbling actions
          countTopTypes (integer): Count distinct types of actions and return values in meta
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: startDate | type | text
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/resources/{id}/actions", params=params, validate=validate))

    async def administrative(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /resources/{id}/administrative
        
        Get resource's administrative data
        """
        return Document(await self._client.request("GET", f"/resources/{id}/administrative", params=params, validate=validate))

    async def update_administrative(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /resources/{id}/administrative
        
        Update administrative data related to a resource
        
        Request body schema: resourcesAdministrativeBody-put
        """
        return Document(await self._client.request("PUT", f"/resources/{id}/administrative", json=body, params=params, validate=validate))

    async def advantages(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /resources/{id}/advantages
        
        Get resource's advantages
        
        Query params:
          advantageTypes (string, repeatable): List of advantages types `reference` with agency's id `id` to filter (described by /api/rest/agencies on view `resources`).
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: creationDate | typeOf.name
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/resources/{id}/advantages", params=params, validate=validate))

    async def ai_matching(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /resources/{id}/ai/matching
        
        Get list of opportunities matching this resource
        """
        return Document(await self._client.request("GET", f"/resources/{id}/ai/matching", params=params, validate=validate))

    async def ai_summary(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /resources/{id}/ai/summary
        
        Get ai generated candidate's summary
        """
        return Document(await self._client.request("GET", f"/resources/{id}/ai/summary", params=params, validate=validate))

    async def attached_flags(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /resources/{id}/attached-flags
        
        Get resource's attached flags
        """
        return Document(await self._client.request("GET", f"/resources/{id}/attached-flags", params=params, validate=validate))

    async def deliveries_inactivities(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /resources/{id}/deliveries-inactivities
        
        Get resource's deliveries & inactivities
        
        Query params:
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: startDate | endDate | id | project.company.name
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/resources/{id}/deliveries-inactivities", params=params, validate=validate))

    async def download(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /resources/{id}/download
        
        Get resource's formatted file content
        
        Query params:
          language (string, one of: fr | en | es): Language used for the file content
          template (string): template ID
        """
        return Document(await self._client.request("GET", f"/resources/{id}/download", params=params, validate=validate))

    async def expenses_reports(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /resources/{id}/expenses-reports
        
        Get resource's expenses
        
        Query params:
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: term | paid | state
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/resources/{id}/expenses-reports", params=params, validate=validate))

    async def followed_documents(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /resources/{id}/followed-documents
        
        Get resource's documents to follow up
        
        Query params:
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: id | typeOf | expirationDate | state
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/resources/{id}/followed-documents", params=params, validate=validate))

    async def forms(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /resources/{id}/forms
        
        Search resource's forms
        
        Query params:
          dependsOnTypes (string, repeatable): Type on which depend form.
          onlyMyForms (boolean): Return forms where recipient is in keyword
          onlyNotValidated (boolean): Return forms without validateDate
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: recipient | form | state | creationDate | validateDate | createdBy
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/resources/{id}/forms", params=params, validate=validate))

    async def information(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /resources/{id}/information
        
        Get resource's information data
        """
        return Document(await self._client.request("GET", f"/resources/{id}/information", params=params, validate=validate))

    async def update_information(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /resources/{id}/information
        
        Update information data related to a resource.
        
        Request body schema: resourcesInformationBody-put
        """
        return Document(await self._client.request("PUT", f"/resources/{id}/information", json=body, params=params, validate=validate))

    async def positionings(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /resources/{id}/positionings
        
        Get resource's positionings
        
        Query params:
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: updateDate | opportunity.title | opportunity.state | state | opportunity.company.name | opportunity.mainManager.lastName
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/resources/{id}/positionings", params=params, validate=validate))

    async def projects(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /resources/{id}/projects
        
        Get resource's projects
        
        Query params:
          projectTypes (integer, repeatable): List of project types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.project)
          projectStates (integer, repeatable): List of project states `id` to filter (described by /api/rest/application/dictionary/setting.state.project)
          period (string): * `created` : Projects created between `startDate` and `endDate`  are filtered
          startDate (string): Start date
          endDate (string): End date
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: startDate | endDate | reference | company.name
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/resources/{id}/projects", params=params, validate=validate))

    async def provider_invoices(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /resources/{id}/provider-invoices
        
        Get resource's providerinvoices
        
        Query params:
          keywords (string): `keywords = PROINV**ID1** PROINV**ID2**` then providerinvoices
          providerInvoiceStates (integer, repeatable): List of providerinvoice states `id` to filter (described by /api/rest/application/dictionary/setting.state.providerinvoice)
          providerInvoicePaymentStates (integer, repeatable): List of providerinvoice states payment `id` to filter; 0=Not settled, 1=Partially settled, 2=Settled
          period (string): * `invoiceDate` : providerinvoices date between `startDate` and `endDate`  are filtered
          startDate (string): Start date
          endDate (string): End date
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: invoiceDate | reference | state | amountExcludingTax | amountIncludingTax
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/resources/{id}/provider-invoices", params=params, validate=validate))

    async def rights(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /resources/{id}/rights
        
        Get resource's rights
        """
        return Document(await self._client.request("GET", f"/resources/{id}/rights", params=params, validate=validate))

    async def settings_absences_accounts(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /resources/{id}/settings/absences-accounts
        
        Get resource's absences accounts settings
        """
        return Document(await self._client.request("GET", f"/resources/{id}/settings/absences-accounts", params=params, validate=validate))

    async def update_settings_absences_accounts(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /resources/{id}/settings/absences-accounts
        
        Update absences accounts related to a resource
        
        Request body schema: resourcesSettingsAbsencesAccountsBody-put
        """
        return Document(await self._client.request("PUT", f"/resources/{id}/settings/absences-accounts", json=body, params=params, validate=validate))

    async def settings_alerts(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /resources/{id}/settings/alerts
        
        Get resource's alerts settings
        """
        return Document(await self._client.request("GET", f"/resources/{id}/settings/alerts", params=params, validate=validate))

    async def update_settings_alerts(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /resources/{id}/settings/alerts
        
        Update resource's alerts settings
        
        Request body schema: resourcesSettingsAlertsBody-put
        """
        return Document(await self._client.request("PUT", f"/resources/{id}/settings/alerts", json=body, params=params, validate=validate))

    async def settings_alerts_reset(self, id, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /resources/{id}/settings/alerts/reset
        
        Reset resource's alerts settings
        """
        return Document(await self._client.request("POST", f"/resources/{id}/settings/alerts/reset", json=body, params=params, validate=validate))

    async def settings_dashboards(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /resources/{id}/settings/dashboards
        
        Get resource's dashboard settings
        """
        return Document(await self._client.request("GET", f"/resources/{id}/settings/dashboards", params=params, validate=validate))

    async def settings_groups(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /resources/{id}/settings/groups
        
        Get resource's groups settings
        """
        return Document(await self._client.request("GET", f"/resources/{id}/settings/groups", params=params, validate=validate))

    async def update_settings_groups(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /resources/{id}/settings/groups
        
        Update groups settings related to a resource
        
        Request body schema: resourcesSettingsGroupsBody-put
        """
        return Document(await self._client.request("PUT", f"/resources/{id}/settings/groups", json=body, params=params, validate=validate))

    async def settings_intranet(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /resources/{id}/settings/intranet
        
        Get resource's intranet settings
        """
        return Document(await self._client.request("GET", f"/resources/{id}/settings/intranet", params=params, validate=validate))

    async def update_settings_intranet(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /resources/{id}/settings/intranet
        
        Update intranet settings related to a resource
        
        Request body schema: resourcesSettingsIntranetBody-put
        """
        return Document(await self._client.request("PUT", f"/resources/{id}/settings/intranet", json=body, params=params, validate=validate))

    async def settings_notifications(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /resources/{id}/settings/notifications
        
        Get resource's notifications settings
        """
        return Document(await self._client.request("GET", f"/resources/{id}/settings/notifications", params=params, validate=validate))

    async def update_settings_notifications(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /resources/{id}/settings/notifications
        
        Update notifications settings related to a resource
        
        Request body schema: resourcesSettingsNotificationsBody-put
        """
        return Document(await self._client.request("PUT", f"/resources/{id}/settings/notifications", json=body, params=params, validate=validate))

    async def settings_positioning_suggests(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /resources/{id}/settings/positioning-suggests
        
        Get resource's positioning suggest settings
        """
        return Document(await self._client.request("GET", f"/resources/{id}/settings/positioning-suggests", params=params, validate=validate))

    async def update_settings_positioning_suggests(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /resources/{id}/settings/positioning-suggests
        
        Update positioning suggest settings related to a resource
        
        Request body schema: resourcesSettingsPositioningSuggestsBody-put
        """
        return Document(await self._client.request("PUT", f"/resources/{id}/settings/positioning-suggests", json=body, params=params, validate=validate))

    async def settings_reporting(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /resources/{id}/settings/reporting
        
        Get resource's reporting settings
        """
        return Document(await self._client.request("GET", f"/resources/{id}/settings/reporting", params=params, validate=validate))

    async def update_settings_reporting(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /resources/{id}/settings/reporting
        
        Update reporting settings related to a resource
        
        Request body schema: resourcesSettingsReportingBody-put
        """
        return Document(await self._client.request("PUT", f"/resources/{id}/settings/reporting", json=body, params=params, validate=validate))

    async def settings_security(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /resources/{id}/settings/security
        
        Get resource's security setting
        """
        return Document(await self._client.request("GET", f"/resources/{id}/settings/security", params=params, validate=validate))

    async def update_settings_security(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /resources/{id}/settings/security
        
        Update security setting related to a resource
        
        Request body schema: resourcesSettingsSecurityBody-put
        """
        return Document(await self._client.request("PUT", f"/resources/{id}/settings/security", json=body, params=params, validate=validate))

    async def settings_targets(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /resources/{id}/settings/targets
        
        Get resource's targets setting
        """
        return Document(await self._client.request("GET", f"/resources/{id}/settings/targets", params=params, validate=validate))

    async def tasks(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /resources/{id}/tasks
        
        Get resource's tasks
        """
        return Document(await self._client.request("GET", f"/resources/{id}/tasks", params=params, validate=validate))

    async def technical_data(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /resources/{id}/technical-data
        
        Get resource's technical data
        
        Query params:
          language (string, one of: fr | en | es): Language used for the file content
        """
        return Document(await self._client.request("GET", f"/resources/{id}/technical-data", params=params, validate=validate))

    async def update_technical_data(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /resources/{id}/technical-data
        
        Update technical data related to a resource
        
        Request body schema: resourcesTechnicalDataBody-put
        """
        return Document(await self._client.request("PUT", f"/resources/{id}/technical-data", json=body, params=params, validate=validate))

    async def technical_datas(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /resources/{id}/technical-datas
        
        Get resource's technical datas
        
        Query params:
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: updateDate | isReferent
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/resources/{id}/technical-datas", params=params, validate=validate))

    async def times_reports(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /resources/{id}/times-reports
        
        Get resource's timesheets
        
        Query params:
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: term | state
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", f"/resources/{id}/times-reports", params=params, validate=validate))



class RolesAPI:
    """Endpoints under /roles."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /roles
        
        Search roles
        
        Query params:
          keywords (string): If `keywords = ROLE**ID1**` then accounts
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: name
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/roles", params=params, validate=validate))

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /roles
        
        Create a role
        
        Request body schema: rolesBody-post
        """
        return Document(await self._client.request("POST", "/roles", json=body, params=params, validate=validate))

    async def default(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /roles/default
        
        Get empty role's default basic data
        
        Query params:
          role (integer): Role's `id` on which the new role is based on
          roleTemplate (integer): Role template's `id` on which the new role is based on
          accountTemplate (integer): Account's `id` on which the new role is based on
        """
        return Document(await self._client.request("GET", "/roles/default", params=params, validate=validate))

    async def templates(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /roles/templates
        
        Search roles
        
        Query params:
          keywords (string): If `keywords = ROLE**ID1**` then accounts
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: name
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/roles/templates", params=params, validate=validate))

    async def post_templates(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /roles/templates
        
        Create a role
        
        Request body schema: roleTemplatesBody-post
        """
        return Document(await self._client.request("POST", "/roles/templates", json=body, params=params, validate=validate))

    async def templates_default(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /roles/templates/default
        
        Get empty role's default basic data
        
        Query params:
          role (integer): Role's `id` on which the new role is based on
          roleTemplate (integer): Role template's `id` on which the new role is based on
        """
        return Document(await self._client.request("GET", "/roles/templates/default", params=params, validate=validate))

    async def delete_templates_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /roles/templates/{id}
        
        Delete the role
        """
        return Document(await self._client.request("DELETE", f"/roles/templates/{id}", params=params, validate=validate))

    async def templates_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /roles/templates/{id}
        
        Get role's basic data
        """
        return Document(await self._client.request("GET", f"/roles/templates/{id}", params=params, validate=validate))

    async def update_templates_by_id(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /roles/templates/{id}
        
        Update basic data related to a role
        
        Request body schema: roleTemplatesBody-put
        """
        return Document(await self._client.request("PUT", f"/roles/templates/{id}", json=body, params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /roles/{id}
        
        Delete the role
        """
        return Document(await self._client.request("DELETE", f"/roles/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /roles/{id}
        
        Get role's basic data
        """
        return Document(await self._client.request("GET", f"/roles/{id}", params=params, validate=validate))

    async def update(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /roles/{id}
        
        Update basic data related to a role
        
        Request body schema: rolesBody-put
        """
        return Document(await self._client.request("PUT", f"/roles/{id}", json=body, params=params, validate=validate))



class SandboxAPI:
    """Endpoints under /sandbox."""

    def __init__(self, client) -> None:
        self._client = client

    async def create(self, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /sandbox
        
        Create a sandbox
        """
        return Document(await self._client.request("POST", "/sandbox", json=body, params=params, validate=validate))

    async def connect(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /sandbox/connect
        
        Connect to the sandbox
        """
        return Document(await self._client.request("GET", "/sandbox/connect", params=params, validate=validate))



class SavedsearchesAPI:
    """Endpoints under /savedsearches."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /savedsearches
        
        Search user's saved search
        
        Query params:
          keywords (string): Keywords
          sharedOnly (boolean, repeatable): Display all shared saved search only
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: name | module | numberOfSharings
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/savedsearches", params=params, validate=validate))

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /savedsearches
        
        Create a saved search
        
        Request body schema: savedsearchesBody-post
        """
        return Document(await self._client.request("POST", "/savedsearches", json=body, params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /savedsearches/{id}
        
        Delete the saved search
        """
        return Document(await self._client.request("DELETE", f"/savedsearches/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /savedsearches/{id}
        
        Get saved search's basic data
        """
        return Document(await self._client.request("GET", f"/savedsearches/{id}", params=params, validate=validate))

    async def update(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /savedsearches/{id}
        
        Update basic data related to a saved search
        
        Request body schema: savedsearchesBody-put
        """
        return Document(await self._client.request("PUT", f"/savedsearches/{id}", json=body, params=params, validate=validate))



class ShareAPI:
    """Endpoints under /share."""

    def __init__(self, client) -> None:
        self._client = client

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /share
        
        Share a profile
        
        Request body schema: shareBody-post
        """
        return Document(await self._client.request("POST", "/share", json=body, params=params, validate=validate))

    async def default(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /share/default
        
        Get empty share's profile default basic data
        
        Query params:
          resource (integer): Resource's `id` on which share depends
          candidate (integer): Candidate's `id` on which share depends
          opportunity (integer): Opportunity's `id` on which share depends
          project (integer): Project's `id` on which share depends
          product (integer): Product's `id` on which share depends
          purchase (integer): Purchase's `id` on which share depends
          order (integer): Order's `id` on which share depends
          invoice (integer): Invoice's `id` on which share depends
          contact (integer): Contact's `id` on which share depends
          company (integer): Company's `id` on which share depends
          timesReport (integer): Timesheet's `id` on which share depends
          expensesReport (integer): Expenses's `id` on which share depends
          absencesReport (integer): Request of absences `id` on which share depends
          payment (integer): Payment's `id` on which share depends
          action (integer): Action's `id` on which share depends
          delivery (integer): Delivery's `id` on which share depends
          inactivity (integer): Inactivity's `id` on which share depends
          groupment (integer): Groupment's `id` on which share depends
          positioning (integer): Positioning's `id` on which share depends
          contract (integer): Contract's `id` on which share depends
          advantage (integer): Advantage's `id` on which share depends
          appEntity (integer): App entity's `id` on which share depends
          form (integer): Form's `id` on which share depends
          settings (string): * `notUsed` : Not used
        """
        return Document(await self._client.request("GET", "/share/default", params=params, validate=validate))



class SignatureAPI:
    """Endpoints under /signature."""

    def __init__(self, client) -> None:
        self._client = client

    async def delete_many(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /signature
        
        Delete sign request
        """
        return Document(await self._client.request("DELETE", "/signature", params=params, validate=validate))

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /signature
        
        Access signature from visitor access
        
        Query params:
          key (string): Folder's `key` when no user is logged in
          customerCode (string): Customer's code when no user is logged in
        """
        return Document(await self._client.request("GET", "/signature", params=params, validate=validate))

    async def update_many(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /signature
        
        Update signature from visitor access
        
        Request body schema: signaturesBody-put
        """
        return Document(await self._client.request("PUT", "/signature", json=body, params=params, validate=validate))



class SignaturesAPI:
    """Endpoints under /signatures."""

    def __init__(self, client) -> None:
        self._client = client

    async def document_by_id(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /signatures/document/{id}
        
        Get download center's file content
        
        Query params:
          embedded (boolean): Flag to get the displayable or downloadable version of the document
          key (string): Folder's `key` when no user is logged in
          customerCode (string): Customer's code when no user is logged in
        """
        return Document(await self._client.request("GET", f"/signatures/document/{id}", params=params, validate=validate))



class StandardProfilesAPI:
    """Endpoints under /standard-profiles."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /standard-profiles
        
        Search standard profiles
        
        Query params:
          keywords (string): If `keywords = PRFT**ID1** PRFT**ID2**` then standard profiles
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: title | dailyPriceExcludingTax | dailyCostExcludingTax
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/standard-profiles", params=params, validate=validate))

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /standard-profiles
        
        Create a standard profile
        
        Request body schema: standardProfilesBody-post
        """
        return Document(await self._client.request("POST", "/standard-profiles", json=body, params=params, validate=validate))

    async def default(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /standard-profiles/default
        
        Get empty standard profile's default basic data
        """
        return Document(await self._client.request("GET", "/standard-profiles/default", params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /standard-profiles/{id}
        
        Delete the standard profile
        """
        return Document(await self._client.request("DELETE", f"/standard-profiles/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /standard-profiles/{id}
        
        Get standard profile's basic data
        """
        return Document(await self._client.request("GET", f"/standard-profiles/{id}", params=params, validate=validate))

    async def update(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /standard-profiles/{id}
        
        Update standard profile's basic data
        
        Request body schema: standardProfilesBody-put
        """
        return Document(await self._client.request("PUT", f"/standard-profiles/{id}", json=body, params=params, validate=validate))

    async def rights(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /standard-profiles/{id}/rights
        
        Get standard profile's rights
        """
        return Document(await self._client.request("GET", f"/standard-profiles/{id}/rights", params=params, validate=validate))



class SubscriptionAPI:
    """Endpoints under /subscription."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /subscription
        
        Get subscription's basic data
        """
        return Document(await self._client.request("GET", "/subscription", params=params, validate=validate))

    async def update_many(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /subscription
        
        Update basic data related to a subscription
        
        Request body schema: subscriptionBody-put
        """
        return Document(await self._client.request("PUT", "/subscription", json=body, params=params, validate=validate))

    async def invoices(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /subscription/invoices
        
        Search invoices
        
        Query params:
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
        """
        return Document(await self._client.request("GET", "/subscription/invoices", params=params, validate=validate))

    async def invoices_by_id_download(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /subscription/invoices/{id}/download
        
        Get subscription's invoice formatted file content
        """
        return Document(await self._client.request("GET", f"/subscription/invoices/{id}/download", params=params, validate=validate))



class TargetsAPI:
    """Endpoints under /targets."""

    def __init__(self, client) -> None:
        self._client = client

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /targets
        
        Create a target
        
        Request body schema: targetsBody-post
        """
        return Document(await self._client.request("POST", "/targets", json=body, params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /targets/{id}
        
        Delete the target
        """
        return Document(await self._client.request("DELETE", f"/targets/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /targets/{id}
        
        Get target's basic data
        """
        return Document(await self._client.request("GET", f"/targets/{id}", params=params, validate=validate))

    async def update(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /targets/{id}
        
        Update basic data related to a target
        
        Request body schema: targetsBody-put
        """
        return Document(await self._client.request("PUT", f"/targets/{id}", json=body, params=params, validate=validate))



class TasksAPI:
    """Endpoints under /tasks."""

    def __init__(self, client) -> None:
        self._client = client

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /tasks/{id}
        
        Get a task
        
        Query params:
          candidate (integer): Candidate's `id` on which task validation's depends
          company (integer): Company's `id` on which task validation's depends
          contact (integer): Contact's `id` on which task validation's depends
          contract (integer): Contract's `id` on which task validation's depends
          delivery (integer): Delivery's `id` on which task validation's depends
          invoice (integer): Invoice's `id` on which task validation's depends
          opportunity (integer): Opportunity's `id` on which task validation's depends
          order (integer): Order's `id` on which task validation's depends
          payment (integer): Payment's `id` on which task validation's depends
          positioning (integer): Positioning's `id` on which task depends
          product (integer): Product's `id` on which task validation's depends
          project (integer): Project's `id` on which task validation's depends
          purchase (integer): Purchase's `id` on which task validation's depends
          quotation (integer): Quotation's `id` on which task validation's depends
          resource (integer): Resource's `id` on which task validation's depends
          appEntity (integer): App entity's `id` on which task validation's depends
        """
        return Document(await self._client.request("GET", f"/tasks/{id}", params=params, validate=validate))

    async def check(self, id, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /tasks/{id}/check
        
        Check a task
        
        Query params:
          candidate (integer): Candidate's `id` on which task validation's depends
          company (integer): Company's `id` on which task validation's depends
          contact (integer): Contact's `id` on which task validation's depends
          contract (integer): Contract's `id` on which task validation's depends
          delivery (integer): Delivery's `id` on which task validation's depends
          invoice (integer): Invoice's `id` on which task validation's depends
          opportunity (integer): Opportunity's `id` on which task validation's depends
          order (integer): Order's `id` on which task validation's depends
          payment (integer): Payment's `id` on which task validation's depends
          positioning (integer): Positioning's `id` on which task depends
          product (integer): Product's `id` on which task validation's depends
          project (integer): Project's `id` on which task validation's depends
          purchase (integer): Purchase's `id` on which task validation's depends
          quotation (integer): Quotation's `id` on which task validation's depends
          resource (integer): Resource's `id` on which task validation's depends
          appEntity (integer): App entity's `id` on which task validation's depends
        """
        return Document(await self._client.request("POST", f"/tasks/{id}/check", json=body, params=params, validate=validate))

    async def uncheck(self, id, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /tasks/{id}/uncheck
        
        Uncheck a task
        
        Query params:
          candidate (integer): Candidate's `id` on which task validation's depends
          company (integer): Company's `id` on which task validation's depends
          contact (integer): Contact's `id` on which task validation's depends
          contract (integer): Contract's `id` on which task validation's depends
          delivery (integer): Delivery's `id` on which task validation's depends
          invoice (integer): Invoice's `id` on which task validation's depends
          opportunity (integer): Opportunity's `id` on which task validation's depends
          order (integer): Order's `id` on which task validation's depends
          payment (integer): Payment's `id` on which task validation's depends
          positioning (integer): Positioning's `id` on which task depends
          product (integer): Product's `id` on which task validation's depends
          project (integer): Project's `id` on which task validation's depends
          purchase (integer): Purchase's `id` on which task validation's depends
          quotation (integer): Quotation's `id` on which task validation's depends
          resource (integer): Resource's `id` on which task validation's depends
          appEntity (integer): App entity's `id` on which task validation's depends
        """
        return Document(await self._client.request("POST", f"/tasks/{id}/uncheck", json=body, params=params, validate=validate))



class TechnicalDatasAPI:
    """Endpoints under /technical-datas."""

    def __init__(self, client) -> None:
        self._client = client

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /technical-datas
        
        Create technical data for a resource or candidate
        
        Request body schema: technicalDatasBody-post
        """
        return Document(await self._client.request("POST", "/technical-datas", json=body, params=params, validate=validate))

    async def default(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /technical-datas/default
        
        Get empty technical Data default basic values
        """
        return Document(await self._client.request("GET", "/technical-datas/default", params=params, validate=validate))

    async def visitor_access(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /technical-datas/visitor-access
        
        Public technical file data
        
        Query params:
          key (string): TD public token's `key` when no user is logged in
          customerCode (string): Customer's code when no user is logged in
        """
        return Document(await self._client.request("GET", "/technical-datas/visitor-access", params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /technical-datas/{id}
        
        Delete the technical data
        """
        return Document(await self._client.request("DELETE", f"/technical-datas/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /technical-datas/{id}
        
        Get technical data's
        """
        return Document(await self._client.request("GET", f"/technical-datas/{id}", params=params, validate=validate))

    async def update(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /technical-datas/{id}
        
        Update technical data's
        
        Request body schema: technicalDatasBody-put
        """
        return Document(await self._client.request("PUT", f"/technical-datas/{id}", json=body, params=params, validate=validate))

    async def update_applyresume(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /technical-datas/{id}/applyresume
        
        Update technical data's by resume
        
        Request body schema: technicalDatasResumeBody-put
        """
        return Document(await self._client.request("PUT", f"/technical-datas/{id}/applyresume", json=body, params=params, validate=validate))

    async def download(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /technical-datas/{id}/download
        
        Get technical data's formatted file content
        
        Query params:
          language (string, one of: fr | en | es): Language used for the file content
          template (string): template ID
        """
        return Document(await self._client.request("GET", f"/technical-datas/{id}/download", params=params, validate=validate))



class ThreadsAPI:
    """Endpoints under /threads."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /threads
        
        Search threads
        
        Query params:
          keywords (string): If `keywords = COMP**ID1** CAND**ID2** PRJ**ID3** CCON**ID4** CSOC**ID5** AO**ID6** BDC**ID7** FACT**ID8** PROD**ID9** ACH**ID10** PMT**ID12** MIS**ID13** INA**ID14** GRP**ID15** ACT**ID16** POS**ID21** TPS**ID22** FRS**ID23** ABS**ID24** CTR**ID26** ADV**ID27** THR**ID28** QUOT**ID29** APPENTITY**ID30**` then
          typeOf (string): type of thread
          period (string): * `created` : Threads created between `startDate` and `endDate` are filtered
          startDate (string): Start date
          endDate (string): End date
          parentThread (integer): Thread parent id
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: typeOf|creationDate|updateDate
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/threads", params=params, validate=validate))

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /threads
        
        Create a thread
        
        Query params:
          parent (integer): Parent's `id`
        
        Request body schema: commentsBody-post
        """
        return Document(await self._client.request("POST", "/threads", json=body, params=params, validate=validate))

    async def default(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /threads/default
        
        Get empty thread's default basic data
        
        Query params:
          typeOf (string, REQUIRED): Type of thread
          resource (integer): Resource's `id` on which thread depends
          candidate (integer): Candidate's `id` on which thread depends
          project (integer): Project's `id` on which thread depends
          contact (integer): Contact's `id` on which thread depends
          company (integer): Company's `id` on which thread depends
          opportunity (integer): Opportunity's `id` on which thread depends
          order (integer): Order's `id` on which thread depends
          invoice (integer): Invoice's `id` on which thread depends
          product (integer): Product's `id` on which thread depends
          purchase (integer): Purchase's `id` on which thread depends
          payment (integer): Payment's `id` on which thread depends
          delivery (integer): Delivery's `id` on which thread depends
          inactivity (integer): Inactivity's `id` on which thread depends
          groupment (integer): Groupment's `id` on which thread depends
          action (integer): Action's `id` on which thread depends
          positioning (integer): Positioning's `id` on which thread depends
          timesReport (integer): Timesheet's `id` on which thread depends
          expensesReport (integer): Expense's `id` on which thread depends
          absencesReport (integer): Absence's `id` on which thread depends
          contract (integer): Contract's `id` on which thread depends
          advantage (integer): Advantage's `id` on which thread depends
          quotation (integer): Quotation's `id` on which thread depends
          appEntity (integer): App entity's `id` on which thread depends
          thread (integer): Thread's `id` on which thread depends
        """
        return Document(await self._client.request("GET", "/threads/default", params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /threads/{id}
        
        Delete thread
        """
        return Document(await self._client.request("DELETE", f"/threads/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /threads/{id}
        
        Get thread's basic data
        """
        return Document(await self._client.request("GET", f"/threads/{id}", params=params, validate=validate))

    async def update(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /threads/{id}
        
        Update thread
        
        Request body schema: commentsBody-put
        """
        return Document(await self._client.request("PUT", f"/threads/{id}", json=body, params=params, validate=validate))



class ThumbnailsAPI:
    """Endpoints under /thumbnails."""

    def __init__(self, client) -> None:
        self._client = client

    async def create(self, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /thumbnails
        
        Create a thumbnail
        """
        return Document(await self._client.request("POST", "/thumbnails", json=body, params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /thumbnails/{id}
        
        Delete the thumbnail
        """
        return Document(await self._client.request("DELETE", f"/thumbnails/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /thumbnails/{id}
        
        Get thumbnail
        """
        return Document(await self._client.request("GET", f"/thumbnails/{id}", params=params, validate=validate))



class TimesAPI:
    """Endpoints under /times."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /times
        
        Search times
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/times.csv?keywords=TPS1 TPSEXP2*
        
        Query params:
          keywords (string): If `keywords = COMP**ID1** PRJ**ID2** CCON**ID3** CSOC**ID4**` then times
          activityType (string, one of: absence | internal | production)
          workUnitTypes (string, repeatable): List of entity workunit types `id`, related to the agency's entity, to filter
          category (string, one of: regular | exceptional)
          resourceTypes (integer, repeatable): List of resource types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.resource)
          excludeResourceTypes (integer, repeatable): List of resource types `id` not filtered (described by /api/rest/application/dictionary/setting.typeOf.resource)
          returnDetailedExceptionalTimes (boolean, default False): If `true` returns endDate, cost, priceExcludingTax for times which category is "exceptional"
          period (string): * `inProgress` : Times between `startDate` and `endDate` are filtered
          startDate (string): Start date
          endDate (string): End date
          encoding (string): If the output format is **csv** then **encoding** filter should be one of
          extractType (string): If the output format is **csv** then **extractType** filter should be one of
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: category | startDate | workUnitType.reference | timesReport.resource.lastName | timesReport.state | delivery.project.company.name | delivery.project.reference | recovering | processed
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/times", params=params, validate=validate))



class TimesReportsAPI:
    """Endpoints under /times-reports."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /times-reports
        
        Search timesheets
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/times-reports.csv?keywords=TPS1*
        
        Query params:
          startMonth (string, REQUIRED): Start month
          endMonth (string, REQUIRED): End month
          keywords (string): If `keywords = TPS**ID1** COMP**ID2**` then timesheets
          resourceTypes (integer, repeatable): List of resource types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.resource)
          validationStates (string, repeatable, one of: waitingForValidation | validated | rejected)
          closed (boolean): If `true` returns only timesheets which are closed, if `false` returns only timesheets which are not closed
          encoding (string): If the output format is **csv** then **encoding** filter should be one of
          extractType (string, default notDetailedInDays): If the output format is **csv** then **extractType** filter should be one of
          exportToDownloadCenter (string): Export timesheets formatted file and/or documents to the download center
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: term | state | resource.lastName | closed
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/times-reports", params=params, validate=validate))

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /times-reports
        
        Create a timesheet
        
        Request body schema: timesReportsBody-post
        """
        return Document(await self._client.request("POST", "/times-reports", json=body, params=params, validate=validate))

    async def default(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /times-reports/default
        
        Get empty timesheet's default basic data
        
        Query params:
          resource (integer, REQUIRED): Resource's `id` on which timesheet depends
          term (string, REQUIRED): Start month
          agency (integer): Agency's `id` on which timesheet depends
        """
        return Document(await self._client.request("GET", "/times-reports/default", params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /times-reports/{id}
        
        Delete the timesheet
        """
        return Document(await self._client.request("DELETE", f"/times-reports/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /times-reports/{id}
        
        Get timesheet's basic data
        """
        return Document(await self._client.request("GET", f"/times-reports/{id}", params=params, validate=validate))

    async def update(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /times-reports/{id}
        
        Update basic data related to a timesheet
        
        Request body schema: timesReportsBody-put
        """
        return Document(await self._client.request("PUT", f"/times-reports/{id}", json=body, params=params, validate=validate))

    async def download(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /times-reports/{id}/download
        
        Get timesheet formatted file content
        
        Query params:
          type (string, REQUIRED): Type of formatted file
          language (string, one of: fr | en | es): Language used for the file content
          project (integer): Project's `id` on which formatted file depends.
          workUnitTypes (integer, repeatable): List of workunit types `reference`.
          showWorkUnitTypeName (boolean, default False): Available only if **type** is `customer`
          showResourceFullName (boolean, default False): Available only if **type** is `customer`
          showInformationComments (boolean, default False): Available only if **type** is `customer`
        """
        return Document(await self._client.request("GET", f"/times-reports/{id}/download", params=params, validate=validate))

    async def reject(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /times-reports/{id}/reject
        
        Reject a timesheet
        
        Query params:
          expectedValidator (integer, REQUIRED): Resource's `id` on which timesheet depends
          reason (string, REQUIRED)
          rejectTypeOf (string, REQUIRED, default correctionForPreviousValidator): * `correctionForPreviousValidator`
        
        Request body schema: timesReportsRejectBody-post
        """
        return Document(await self._client.request("POST", f"/times-reports/{id}/reject", json=body, params=params, validate=validate))

    async def rights(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /times-reports/{id}/rights
        
        Get timesheet's rights
        
        Query params:
          resource (integer): Resource's `id` on which timesheet depends
          term (string): Start month
          agency (integer): Agency's `id` on which timesheet depends
        """
        return Document(await self._client.request("GET", f"/times-reports/{id}/rights", params=params, validate=validate))

    async def signature(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /times-reports/{id}/signature
        
        Create/update signature data related to a timesheet
        
        Query params:
          type (string, REQUIRED): Type of formatted file
          mailValidatorSignature (string, REQUIRED): Email's of validator
          signature (integer): Signature's id
          project (integer): Project's `id` on which signature file depends.
          file (integer): File's `id` on which signature depends
          workUnitTypes (integer, repeatable): List of workunit types `reference`.
          showWorkUnitTypeName (boolean, default False): Available only if **type** is `customer`
          useWorkUnitsForRegularDurations (boolean, default False): Available only if **type** is `customer`
          showResourceFullName (boolean, default False): Available only if **type** is `customer`
          showInformationComments (boolean, default False): Available only if **type** is `customer`
        
        Request body schema: timesReportsRejectBody-post
        """
        return Document(await self._client.request("POST", f"/times-reports/{id}/signature", json=body, params=params, validate=validate))

    async def unvalidate(self, id, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /times-reports/{id}/unvalidate
        
        Unvalidate a timesheet
        
        Query params:
          expectedValidator (integer, REQUIRED): Resource's `id` on which timesheet depends
        """
        return Document(await self._client.request("POST", f"/times-reports/{id}/unvalidate", json=body, params=params, validate=validate))

    async def validate(self, id, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /times-reports/{id}/validate
        
        Validate a timesheet
        
        Query params:
          expectedValidator (integer, REQUIRED): Resource's `id` on which timesheet depends
        """
        return Document(await self._client.request("POST", f"/times-reports/{id}/validate", json=body, params=params, validate=validate))



class TodolistsAPI:
    """Endpoints under /todolists."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /todolists
        
        Search TodoLists
        
        Query params:
          sort (string, repeatable): Order by a given column: title | profile | agency
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/todolists", params=params, validate=validate))

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /todolists
        
        Create a TodoLists
        
        Request body schema: todoListsBody-post
        """
        return Document(await self._client.request("POST", "/todolists", json=body, params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /todolists/{id}
        
        Delete the TodoList
        """
        return Document(await self._client.request("DELETE", f"/todolists/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /todolists/{id}
        
        Get TodoList's data
        """
        return Document(await self._client.request("GET", f"/todolists/{id}", params=params, validate=validate))

    async def update(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /todolists/{id}
        
        Update data related to a TodoList.
        
        Request body schema: todoListsBody-put
        """
        return Document(await self._client.request("PUT", f"/todolists/{id}", json=body, params=params, validate=validate))



class TrustelemAPI:
    """Endpoints under /trustelem."""

    def __init__(self, client) -> None:
        self._client = client

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /trustelem/{id}
        
        Log out user
        """
        return Document(await self._client.request("DELETE", f"/trustelem/{id}", params=params, validate=validate))



class ValidationsAPI:
    """Endpoints under /validations."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /validations
        
        Search validations
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/validations.csv?keywords=TPS1*
        
        Query params:
          startMonth (string, REQUIRED): Start month
          endMonth (string, REQUIRED): End month
          keywords (string): If `keywords = TPS**ID1** EXP**ID2** ABS**ID3** COMP**ID4**` then timesheets
          documentTypes (string, repeatable, one of: absencesReport | timesReport | expensesReport)
          resourceTypes (integer, repeatable): List of resource types `id` to filter (described by /api/rest/application/dictionary/setting.typeOf.resource)
          validationStates (string, repeatable, one of: waitingForValidation | validated | rejected)
          validationAlerts (boolean): * true : display only with alerts
          encoding (string): If the output format is **csv** then **encoding** filter should be one of
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: dependsOn | dependsOn.term | dependsOn.creationDate | state | dependsOn.resource.lastName | expectedValidator.lastName | realValidator.lastName | date
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/validations", params=params, validate=validate))

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /validations
        
        Create validations alert calculation
        
        Request body schema: validationsBody-post
        """
        return Document(await self._client.request("POST", "/validations", json=body, params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /validations/{id}
        
        Delete the validation
        """
        return Document(await self._client.request("DELETE", f"/validations/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /validations/{id}
        
        Get validation's basic data
        """
        return Document(await self._client.request("GET", f"/validations/{id}", params=params, validate=validate))

    async def update(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /validations/{id}
        
        Update basic data related to a validation
        
        Request body schema: validationsBody-put
        """
        return Document(await self._client.request("PUT", f"/validations/{id}", json=body, params=params, validate=validate))



class VendorAPI:
    """Endpoints under /vendor."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /vendor
        
        Get vendor's basic data
        """
        return Document(await self._client.request("GET", "/vendor", params=params, validate=validate))

    async def update_many(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /vendor
        
        Update basic data related to a vendor
        
        Request body schema: vendorBody-put
        """
        return Document(await self._client.request("PUT", "/vendor", json=body, params=params, validate=validate))

    async def delete_logo(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /vendor/logo
        
        Delete the logo
        """
        return Document(await self._client.request("DELETE", "/vendor/logo", params=params, validate=validate))

    async def update_logo(self, body: Any = None, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /vendor/logo
        
        Update logo
        """
        return Document(await self._client.request("PUT", "/vendor/logo", json=body, params=params, validate=validate))



class WebhooksAPI:
    """Endpoints under /webhooks."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /webhooks
        
        Search webhooks
        
        Query params:
          type (string, repeatable, one of: create | update | delete)
          entity (string, repeatable, one of: candidate | resource | advantage | contract | purchase | payment | opportunity | app | positioning | order | invoice | contact | company | project | delivery | inactivity | groupment | businessunit | agency | pole | role | expensesreport | timesreport | absencesreport | action | actiontemplate | quotation | validation | vendor | customer | architecture | flag | target | thread | followeddocument | appentity)
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
        """
        return Document(await self._client.request("GET", "/webhooks", params=params, validate=validate))

    async def create(self, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """POST /webhooks
        
        Create a request of webhook
        
        Request body schema: webhooksBody-post
        """
        return Document(await self._client.request("POST", "/webhooks", json=body, params=params, validate=validate))

    async def delete(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """DELETE /webhooks/{id}
        
        Delete the webhook
        """
        return Document(await self._client.request("DELETE", f"/webhooks/{id}", params=params, validate=validate))

    async def get(self, id, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /webhooks/{id}
        
        Get webhook
        """
        return Document(await self._client.request("GET", f"/webhooks/{id}", params=params, validate=validate))

    async def update(self, id, body: Any, *, params: dict | None = None, validate: bool = True) -> Document:
        """PUT /webhooks/{id}
        
        Update webhook data
        
        Request body schema: webhooksBody-put
        """
        return Document(await self._client.request("PUT", f"/webhooks/{id}", json=body, params=params, validate=validate))



class WorkplacesTimesAPI:
    """Endpoints under /workplaces-times."""

    def __init__(self, client) -> None:
        self._client = client

    async def search(self, *, params: dict | None = None, validate: bool = True) -> Document:
        """GET /workplaces-times
        
        Search workplace's times
        
        _You can specify the output format by appending to the url **.csv**_
        *Example : {BASE_URL}/api/workplace-times.csv?keywords=TPS1 TPSEXP2*
        
        Query params:
          keywords (string): If `keywords = COMP**ID1** CRA**ID2** TPS**ID3**` then workplace's times
          workplaceTypes (string, repeatable): List of entity workplace types `id`, related to the agency's entity, to filter
          period (string): * `inProgress` : Workplace's times between `startDate` and `endDate` are filtered
          startDate (string): Start date
          endDate (string): End date
          encoding (string): If the output format is **csv** then **encoding** filter should be one of
          extractType (string): If the output format is **csv** then **extractType** filter should be one of
          perimeterAgencies (integer, repeatable): Results whom responsibles belong to agency's unique identifier are filtered
          perimeterBusinessUnits (integer, repeatable): Results whom responsibles belong to business unit's unique identifier are filtered
          perimeterPoles (integer, repeatable): Results whom responsibles belong to pole's unique identifier are filtered
          perimeterManagers (integer, repeatable): Results whom responsibles belong to manager's unique identifier are filtered
          narrowPerimeter (boolean): if exists force the kind of join between the types of perimeter used
          perimeterDynamic (string, repeatable): Apply dynamic filtering according to current user context
          page (number, default 1): current page
          maxResults (number, default 30): number of results per page
          sort (string, repeatable): Order by a given column: startDate | timesReport.resource.lastName | timesReport.state | workplaceType.reference
          order (string, one of: desc | asc, default asc): Order's type
        """
        return Document(await self._client.request("GET", "/workplaces-times", params=params, validate=validate))



class BoondManagerAPI:
    """Namespaced access to every endpoint of the BoondManager API.

    Usage::

        doc = await client.api.times_reports.get("1652")
        doc = await client.api.projects.search(params={"keywords": "AZTech"})
    """

    def __init__(self, client) -> None:
        self.absences = AbsencesAPI(client)
        self.absences_reports = AbsencesReportsAPI(client)
        self.accounts = AccountsAPI(client)
        self.actions = ActionsAPI(client)
        self.administrator = AdministratorAPI(client)
        self.advantages = AdvantagesAPI(client)
        self.agencies = AgenciesAPI(client)
        self.alerts = AlertsAPI(client)
        self.analytics = AnalyticsAPI(client)
        self.application = ApplicationAPI(client)
        self.apps = AppsAPI(client)
        self.attached_flags = AttachedFlagsAPI(client)
        self.banking_accounts = BankingAccountsAPI(client)
        self.banking_transactions = BankingTransactionsAPI(client)
        self.billing_deliveries_purchases_balance = BillingDeliveriesPurchasesBalanceAPI(client)
        self.billing_details = BillingDetailsAPI(client)
        self.billing_monthly_balance = BillingMonthlyBalanceAPI(client)
        self.billing_projects_balance = BillingProjectsBalanceAPI(client)
        self.billing_schedules_balance = BillingSchedulesBalanceAPI(client)
        self.boondmanager_contracts = BoondmanagerContractsAPI(client)
        self.business_units = BusinessUnitsAPI(client)
        self.calendars = CalendarsAPI(client)
        self.candidates = CandidatesAPI(client)
        self.companies = CompaniesAPI(client)
        self.conditional_fields = ConditionalFieldsAPI(client)
        self.contacts = ContactsAPI(client)
        self.contracts = ContractsAPI(client)
        self.dashboards = DashboardsAPI(client)
        self.deliveries = DeliveriesAPI(client)
        self.deliveries_groupments = DeliveriesGroupmentsAPI(client)
        self.devices = DevicesAPI(client)
        self.documents = DocumentsAPI(client)
        self.download_center = DownloadCenterAPI(client)
        self.e_invoicing = EInvoicingAPI(client)
        self.expenses = ExpensesAPI(client)
        self.expenses_reports = ExpensesReportsAPI(client)
        self.flags = FlagsAPI(client)
        self.followed_documents = FollowedDocumentsAPI(client)
        self.forms = FormsAPI(client)
        self.gadgets = GadgetsAPI(client)
        self.google = GoogleAPI(client)
        self.groupments = GroupmentsAPI(client)
        self.import_ = ImportAPI(client)
        self.inactivities = InactivitiesAPI(client)
        self.invoices = InvoicesAPI(client)
        self.invoicing_connections = InvoicingConnectionsAPI(client)
        self.logs = LogsAPI(client)
        self.mandatory_leave = MandatoryLeaveAPI(client)
        self.marketplace = MarketplaceAPI(client)
        self.microsoft = MicrosoftAPI(client)
        self.notifications = NotificationsAPI(client)
        self.opportunities = OpportunitiesAPI(client)
        self.orders = OrdersAPI(client)
        self.payments = PaymentsAPI(client)
        self.planning_absences = PlanningAbsencesAPI(client)
        self.poles = PolesAPI(client)
        self.positionings = PositioningsAPI(client)
        self.products = ProductsAPI(client)
        self.projects = ProjectsAPI(client)
        self.provider_invoices = ProviderInvoicesAPI(client)
        self.purchases = PurchasesAPI(client)
        self.reporting_companies = ReportingCompaniesAPI(client)
        self.reporting_production_plans = ReportingProductionPlansAPI(client)
        self.reporting_projects = ReportingProjectsAPI(client)
        self.reporting_resources = ReportingResourcesAPI(client)
        self.reporting_synthesis = ReportingSynthesisAPI(client)
        self.resources = ResourcesAPI(client)
        self.roles = RolesAPI(client)
        self.sandbox = SandboxAPI(client)
        self.savedsearches = SavedsearchesAPI(client)
        self.share = ShareAPI(client)
        self.signature = SignatureAPI(client)
        self.signatures = SignaturesAPI(client)
        self.standard_profiles = StandardProfilesAPI(client)
        self.subscription = SubscriptionAPI(client)
        self.targets = TargetsAPI(client)
        self.tasks = TasksAPI(client)
        self.technical_datas = TechnicalDatasAPI(client)
        self.threads = ThreadsAPI(client)
        self.thumbnails = ThumbnailsAPI(client)
        self.times = TimesAPI(client)
        self.times_reports = TimesReportsAPI(client)
        self.todolists = TodolistsAPI(client)
        self.trustelem = TrustelemAPI(client)
        self.validations = ValidationsAPI(client)
        self.vendor = VendorAPI(client)
        self.webhooks = WebhooksAPI(client)
        self.workplaces_times = WorkplacesTimesAPI(client)


ENDPOINT_INDEX: dict[tuple[str, str], tuple[str, str]] = {
    ("GET", "/absences"): ("absences", "search"),
    ("GET", "/absences-reports"): ("absences_reports", "search"),
    ("POST", "/absences-reports"): ("absences_reports", "create"),
    ("GET", "/absences-reports/default"): ("absences_reports", "default"),
    ("DELETE", "/absences-reports/{id}"): ("absences_reports", "delete"),
    ("GET", "/absences-reports/{id}"): ("absences_reports", "get"),
    ("PUT", "/absences-reports/{id}"): ("absences_reports", "update"),
    ("GET", "/absences-reports/{id}/download"): ("absences_reports", "download"),
    ("POST", "/absences-reports/{id}/reject"): ("absences_reports", "reject"),
    ("GET", "/absences-reports/{id}/rights"): ("absences_reports", "rights"),
    ("POST", "/absences-reports/{id}/unvalidate"): ("absences_reports", "unvalidate"),
    ("POST", "/absences-reports/{id}/validate"): ("absences_reports", "validate"),
    ("GET", "/accounts"): ("accounts", "search"),
    ("POST", "/accounts"): ("accounts", "create"),
    ("GET", "/accounts/default"): ("accounts", "default"),
    ("DELETE", "/accounts/{id}"): ("accounts", "delete"),
    ("GET", "/accounts/{id}"): ("accounts", "get"),
    ("PUT", "/accounts/{id}"): ("accounts", "update"),
    ("GET", "/accounts/{id}/connect"): ("accounts", "connect"),
    ("GET", "/actions"): ("actions", "search"),
    ("POST", "/actions"): ("actions", "create"),
    ("GET", "/actions/default"): ("actions", "default"),
    ("GET", "/actions/templates"): ("actions", "templates"),
    ("POST", "/actions/templates"): ("actions", "post_templates"),
    ("DELETE", "/actions/templates/{id}"): ("actions", "delete_templates_by_id"),
    ("GET", "/actions/templates/{id}"): ("actions", "templates_by_id"),
    ("PUT", "/actions/templates/{id}"): ("actions", "update_templates_by_id"),
    ("DELETE", "/actions/{id}"): ("actions", "delete"),
    ("GET", "/actions/{id}"): ("actions", "get"),
    ("PUT", "/actions/{id}"): ("actions", "update"),
    ("GET", "/actions/{id}/attached-flags"): ("actions", "attached_flags"),
    ("GET", "/actions/{id}/rights"): ("actions", "rights"),
    ("GET", "/administrator"): ("administrator", "search"),
    ("DELETE", "/administrator/logo"): ("administrator", "delete_logo"),
    ("PUT", "/administrator/logo"): ("administrator", "update_logo"),
    ("POST", "/advantages"): ("advantages", "create"),
    ("GET", "/advantages/default"): ("advantages", "default"),
    ("DELETE", "/advantages/{id}"): ("advantages", "delete"),
    ("GET", "/advantages/{id}"): ("advantages", "get"),
    ("PUT", "/advantages/{id}"): ("advantages", "update"),
    ("GET", "/advantages/{id}/rights"): ("advantages", "rights"),
    ("GET", "/agencies"): ("agencies", "search"),
    ("POST", "/agencies"): ("agencies", "create"),
    ("GET", "/agencies/default"): ("agencies", "default"),
    ("DELETE", "/agencies/{id}"): ("agencies", "delete"),
    ("GET", "/agencies/{id}"): ("agencies", "get"),
    ("GET", "/agencies/{id}/activity-expenses"): ("agencies", "activity_expenses"),
    ("PUT", "/agencies/{id}/activity-expenses"): ("agencies", "update_activity_expenses"),
    ("DELETE", "/agencies/{id}/activity-expenses/logo"): ("agencies", "delete_activity_expenses_logo"),
    ("PUT", "/agencies/{id}/activity-expenses/logo"): ("agencies", "update_activity_expenses_logo"),
    ("GET", "/agencies/{id}/billing"): ("agencies", "billing"),
    ("PUT", "/agencies/{id}/billing"): ("agencies", "update_billing"),
    ("DELETE", "/agencies/{id}/billing/logo"): ("agencies", "delete_billing_logo"),
    ("PUT", "/agencies/{id}/billing/logo"): ("agencies", "update_billing_logo"),
    ("GET", "/agencies/{id}/information"): ("agencies", "information"),
    ("PUT", "/agencies/{id}/information"): ("agencies", "update_information"),
    ("GET", "/agencies/{id}/opportunities"): ("agencies", "opportunities"),
    ("PUT", "/agencies/{id}/opportunities"): ("agencies", "update_opportunities"),
    ("GET", "/agencies/{id}/products"): ("agencies", "products"),
    ("PUT", "/agencies/{id}/products"): ("agencies", "update_products"),
    ("GET", "/agencies/{id}/projects"): ("agencies", "projects"),
    ("PUT", "/agencies/{id}/projects"): ("agencies", "update_projects"),
    ("GET", "/agencies/{id}/purchases"): ("agencies", "purchases"),
    ("PUT", "/agencies/{id}/purchases"): ("agencies", "update_purchases"),
    ("GET", "/agencies/{id}/resources"): ("agencies", "resources"),
    ("PUT", "/agencies/{id}/resources"): ("agencies", "update_resources"),
    ("GET", "/agencies/{id}/rights"): ("agencies", "rights"),
    ("GET", "/agencies/{id}/technical-data"): ("agencies", "technical_data"),
    ("PUT", "/agencies/{id}/technical-data"): ("agencies", "update_technical_data"),
    ("GET", "/alerts"): ("alerts", "search"),
    ("GET", "/alerts/configuration"): ("alerts", "configuration"),
    ("PUT", "/alerts/configuration"): ("alerts", "update_configuration"),
    ("GET", "/alerts/{id}/values"): ("alerts", "values"),
    ("GET", "/analytics/reportings/production-by-manager"): ("analytics", "reportings_production_by_manager"),
    ("GET", "/application/assignments"): ("application", "assignments"),
    ("POST", "/application/backup-dictionary"): ("application", "backup_dictionary"),
    ("GET", "/application/current-user"): ("application", "current_user"),
    ("GET", "/application/dictionary"): ("application", "dictionary"),
    ("PUT", "/application/dictionary"): ("application", "update_dictionary"),
    ("GET", "/application/download-dictionary"): ("application", "download_dictionary"),
    ("POST", "/application/dump-database"): ("application", "dump_database"),
    ("GET", "/application/dynamic-filters"): ("application", "dynamic_filters"),
    ("GET", "/application/flags"): ("application", "flags"),
    ("GET", "/application/geocities"): ("application", "geocities"),
    ("GET", "/application/perimeters"): ("application", "perimeters"),
    ("POST", "/application/read-database"): ("application", "read_database"),
    ("PUT", "/application/restore-dictionary"): ("application", "update_restore_dictionary"),
    ("GET", "/application/settings"): ("application", "settings"),
    ("PUT", "/application/settings"): ("application", "update_settings"),
    ("GET", "/application/status"): ("application", "status"),
    ("GET", "/application/weekendAndBankHolidays"): ("application", "weekend_and_bank_holidays"),
    ("GET", "/apps"): ("apps", "search"),
    ("GET", "/apps/absences-accounts/absences-accounts"): ("apps", "absences_accounts_absences_accounts"),
    ("PUT", "/apps/absences-accounts/absences-accounts/{id}"): ("apps", "update_absences_accounts_absences_accounts_by_id"),
    ("POST", "/apps/absences-accounts/import/absences-accounts"): ("apps", "absences_accounts_import__absences_accounts"),
    ("GET", "/apps/accounting-payroll/companies"): ("apps", "accounting_payroll_companies"),
    ("PUT", "/apps/accounting-payroll/companies/{id}"): ("apps", "update_accounting_payroll_companies_by_id"),
    ("GET", "/apps/accounting-payroll/configuration"): ("apps", "accounting_payroll_configuration"),
    ("PUT", "/apps/accounting-payroll/configuration"): ("apps", "update_accounting_payroll_configuration"),
    ("GET", "/apps/accounting-payroll/contracts"): ("apps", "accounting_payroll_contracts"),
    ("GET", "/apps/accounting-payroll/expenses-reports"): ("apps", "accounting_payroll_expenses_reports"),
    ("GET", "/apps/accounting-payroll/invoices"): ("apps", "accounting_payroll_invoices"),
    ("GET", "/apps/accounting-payroll/payments"): ("apps", "accounting_payroll_payments"),
    ("GET", "/apps/accounting-payroll/resources"): ("apps", "accounting_payroll_resources"),
    ("PUT", "/apps/accounting-payroll/resources/{id}"): ("apps", "update_accounting_payroll_resources_by_id"),
    ("GET", "/apps/advanced-candidates/candidates"): ("apps", "advanced_candidates_candidates"),
    ("POST", "/apps/advanced-candidates/candidates"): ("apps", "post_advanced_candidates_candidates"),
    ("GET", "/apps/advanced-candidates/candidates/default"): ("apps", "advanced_candidates_candidates_default"),
    ("GET", "/apps/advanced-candidates/candidates/{id}"): ("apps", "advanced_candidates_candidates_by_id"),
    ("PUT", "/apps/advanced-candidates/candidates/{id}"): ("apps", "update_advanced_candidates_candidates_by_id"),
    ("GET", "/apps/advanced-candidates/candidates/{id}/download"): ("apps", "advanced_candidates_candidates_by_id_download"),
    ("GET", "/apps/advanced-candidates/candidates/{id}/rights"): ("apps", "advanced_candidates_candidates_by_id_rights"),
    ("GET", "/apps/advanced-candidates/candidates/{id}/tasks"): ("apps", "advanced_candidates_candidates_by_id_tasks"),
    ("GET", "/apps/advanced-candidates/resources/{id}"): ("apps", "advanced_candidates_resources_by_id"),
    ("PUT", "/apps/advanced-candidates/resources/{id}"): ("apps", "update_advanced_candidates_resources_by_id"),
    ("GET", "/apps/advanced-projects/configuration"): ("apps", "advanced_projects_configuration"),
    ("PUT", "/apps/advanced-projects/configuration"): ("apps", "update_advanced_projects_configuration"),
    ("GET", "/apps/advanced-projects/projects"): ("apps", "advanced_projects_projects"),
    ("GET", "/apps/advanced-projects/projects/{id}"): ("apps", "advanced_projects_projects_by_id"),
    ("PUT", "/apps/advanced-projects/projects/{id}"): ("apps", "update_advanced_projects_projects_by_id"),
    ("GET", "/apps/advantages/advantages"): ("apps", "advantages_advantages"),
    ("GET", "/apps/answering-validators/answering-machines"): ("apps", "answering_validators_answering_machines"),
    ("POST", "/apps/answering-validators/answering-machines"): ("apps", "post_answering_validators_answering_machines"),
    ("DELETE", "/apps/answering-validators/answering-machines/{id}"): ("apps", "delete_answering_validators_answering_machines_by_id"),
    ("GET", "/apps/backup-database/configuration"): ("apps", "backup_database_configuration"),
    ("PUT", "/apps/backup-database/configuration"): ("apps", "update_backup_database_configuration"),
    ("POST", "/apps/backup-database/dump-database"): ("apps", "backup_database_dump_database"),
    ("GET", "/apps/celebrations/configuration"): ("apps", "celebrations_configuration"),
    ("PUT", "/apps/celebrations/configuration"): ("apps", "update_celebrations_configuration"),
    ("GET", "/apps/celebrations/employees/arrival"): ("apps", "celebrations_employees_arrival"),
    ("GET", "/apps/celebrations/employees/birthday"): ("apps", "celebrations_employees_birthday"),
    ("GET", "/apps/celebrations/employees/seniority"): ("apps", "celebrations_employees_seniority"),
    ("GET", "/apps/celebrations/employees/{id}"): ("apps", "celebrations_employees_by_id"),
    ("PUT", "/apps/celebrations/employees/{id}"): ("apps", "update_celebrations_employees_by_id"),
    ("GET", "/apps/contracts/contracts"): ("apps", "contracts_contracts"),
    ("GET", "/apps/corporama/configuration"): ("apps", "corporama_configuration"),
    ("GET", "/apps/create-activity-documents/resources/{id}"): ("apps", "create_activity_documents_resources_by_id"),
    ("GET", "/apps/data-closing/closed-periods"): ("apps", "data_closing_closed_periods"),
    ("PUT", "/apps/data-closing/closed-periods/{id}"): ("apps", "update_data_closing_closed_periods_by_id"),
    ("GET", "/apps/data-closing/configuration"): ("apps", "data_closing_configuration"),
    ("PUT", "/apps/data-closing/configuration"): ("apps", "update_data_closing_configuration"),
    ("GET", "/apps/data-closing/expenses-reports"): ("apps", "data_closing_expenses_reports"),
    ("PUT", "/apps/data-closing/expenses-reports/{id}"): ("apps", "update_data_closing_expenses_reports_by_id"),
    ("GET", "/apps/data-closing/invoices"): ("apps", "data_closing_invoices"),
    ("PUT", "/apps/data-closing/invoices/{id}"): ("apps", "update_data_closing_invoices_by_id"),
    ("GET", "/apps/data-closing/times-reports"): ("apps", "data_closing_times_reports"),
    ("PUT", "/apps/data-closing/times-reports/{id}"): ("apps", "update_data_closing_times_reports_by_id"),
    ("GET", "/apps/digital-workplace/categories"): ("apps", "digital_workplace_categories"),
    ("POST", "/apps/digital-workplace/categories"): ("apps", "post_digital_workplace_categories"),
    ("DELETE", "/apps/digital-workplace/categories/{id}"): ("apps", "delete_digital_workplace_categories_by_id"),
    ("GET", "/apps/digital-workplace/categories/{id}"): ("apps", "digital_workplace_categories_by_id"),
    ("PUT", "/apps/digital-workplace/categories/{id}"): ("apps", "update_digital_workplace_categories_by_id"),
    ("POST", "/apps/digital-workplace/documents"): ("apps", "digital_workplace_documents"),
    ("GET", "/apps/digital-workplace/documents/viewer"): ("apps", "digital_workplace_documents_viewer"),
    ("DELETE", "/apps/digital-workplace/documents/{id}"): ("apps", "delete_digital_workplace_documents_by_id"),
    ("GET", "/apps/digital-workplace/documents/{id}"): ("apps", "digital_workplace_documents_by_id"),
    ("GET", "/apps/digital-workplace/news"): ("apps", "digital_workplace_news"),
    ("POST", "/apps/digital-workplace/news"): ("apps", "post_digital_workplace_news"),
    ("DELETE", "/apps/digital-workplace/news/{id}"): ("apps", "delete_digital_workplace_news_by_id"),
    ("GET", "/apps/digital-workplace/news/{id}"): ("apps", "digital_workplace_news_by_id"),
    ("PUT", "/apps/digital-workplace/news/{id}"): ("apps", "update_digital_workplace_news_by_id"),
    ("GET", "/apps/doc-templates/configuration"): ("apps", "doc_templates_configuration"),
    ("GET", "/apps/doc-templates/templates"): ("apps", "doc_templates_templates"),
    ("POST", "/apps/doc-templates/templates"): ("apps", "post_doc_templates_templates"),
    ("GET", "/apps/doc-templates/templates/viewer"): ("apps", "doc_templates_templates_viewer"),
    ("DELETE", "/apps/doc-templates/templates/{id}"): ("apps", "delete_doc_templates_templates_by_id"),
    ("GET", "/apps/doc-templates/templates/{id}"): ("apps", "doc_templates_templates_by_id"),
    ("PUT", "/apps/doc-templates/templates/{id}"): ("apps", "update_doc_templates_templates_by_id"),
    ("GET", "/apps/emailing/absencesreports/{id}"): ("apps", "emailing_absencesreports_by_id"),
    ("GET", "/apps/emailing/candidates/{id}"): ("apps", "emailing_candidates_by_id"),
    ("GET", "/apps/emailing/configuration"): ("apps", "emailing_configuration"),
    ("PUT", "/apps/emailing/configuration"): ("apps", "update_emailing_configuration"),
    ("GET", "/apps/emailing/configuration/connection"): ("apps", "emailing_configuration_connection"),
    ("GET", "/apps/emailing/contacts/{id}"): ("apps", "emailing_contacts_by_id"),
    ("GET", "/apps/emailing/expensesreports/{id}"): ("apps", "emailing_expensesreports_by_id"),
    ("GET", "/apps/emailing/invoices/{id}"): ("apps", "emailing_invoices_by_id"),
    ("GET", "/apps/emailing/positionings/{id}"): ("apps", "emailing_positionings_by_id"),
    ("GET", "/apps/emailing/quotations/{id}"): ("apps", "emailing_quotations_by_id"),
    ("GET", "/apps/emailing/resources/{id}"): ("apps", "emailing_resources_by_id"),
    ("GET", "/apps/emailing/resources/{id}/connection"): ("apps", "emailing_resources_by_id_connection"),
    ("GET", "/apps/emailing/resources/{id}/settings"): ("apps", "emailing_resources_by_id_settings"),
    ("PUT", "/apps/emailing/resources/{id}/settings"): ("apps", "update_emailing_resources_by_id_settings"),
    ("POST", "/apps/emailing/share"): ("apps", "emailing_share"),
    ("GET", "/apps/emailing/templates"): ("apps", "emailing_templates"),
    ("POST", "/apps/emailing/templates"): ("apps", "post_emailing_templates"),
    ("GET", "/apps/emailing/templates/last-used"): ("apps", "emailing_templates_last_used"),
    ("DELETE", "/apps/emailing/templates/{id}"): ("apps", "delete_emailing_templates_by_id"),
    ("GET", "/apps/emailing/templates/{id}"): ("apps", "emailing_templates_by_id"),
    ("PUT", "/apps/emailing/templates/{id}"): ("apps", "update_emailing_templates_by_id"),
    ("GET", "/apps/emailing/timesreports/{id}"): ("apps", "emailing_timesreports_by_id"),
    ("GET", "/apps/esignature/candidates/default"): ("apps", "esignature_candidates_default"),
    ("POST", "/apps/esignature/esignatures"): ("apps", "esignature_esignatures"),
    ("DELETE", "/apps/esignature/esignatures/{id}"): ("apps", "delete_esignature_esignatures_by_id"),
    ("GET", "/apps/esignature/esignatures/{id}"): ("apps", "esignature_esignatures_by_id"),
    ("POST", "/apps/esignature/esignatures/{id}/cancel"): ("apps", "esignature_esignatures_by_id_cancel"),
    ("GET", "/apps/exceptional-activity/companies"): ("apps", "exceptional_activity_companies"),
    ("GET", "/apps/exceptional-activity/times"): ("apps", "exceptional_activity_times"),
    ("GET", "/apps/exceptional-activity/times/{id}"): ("apps", "exceptional_activity_times_by_id"),
    ("PUT", "/apps/exceptional-activity/times/{id}"): ("apps", "update_exceptional_activity_times_by_id"),
    ("GET", "/apps/extract-payroll/contracts"): ("apps", "extract_payroll_contracts"),
    ("PUT", "/apps/extract-payroll/contracts/{id}"): ("apps", "update_extract_payroll_contracts_by_id"),
    ("GET", "/apps/extract-payroll/resources/{id}"): ("apps", "extract_payroll_resources_by_id"),
    ("PUT", "/apps/extract-payroll/resources/{id}"): ("apps", "update_extract_payroll_resources_by_id"),
    ("GET", "/apps/extractbi/configuration"): ("apps", "extractbi_configuration"),
    ("PUT", "/apps/extractbi/configuration"): ("apps", "update_extractbi_configuration"),
    ("GET", "/apps/extractbi/requests"): ("apps", "extractbi_requests"),
    ("POST", "/apps/extractbi/requests"): ("apps", "post_extractbi_requests"),
    ("DELETE", "/apps/extractbi/requests/{id}"): ("apps", "delete_extractbi_requests_by_id"),
    ("GET", "/apps/extractbi/requests/{id}"): ("apps", "extractbi_requests_by_id"),
    ("PUT", "/apps/extractbi/requests/{id}"): ("apps", "update_extractbi_requests_by_id"),
    ("GET", "/apps/extractbi/requests/{id}/download"): ("apps", "extractbi_requests_by_id_download"),
    ("GET", "/apps/extractbi/templates"): ("apps", "extractbi_templates"),
    ("POST", "/apps/extractbi/templates"): ("apps", "post_extractbi_templates"),
    ("DELETE", "/apps/extractbi/templates/{id}"): ("apps", "delete_extractbi_templates_by_id"),
    ("GET", "/apps/extractbi/templates/{id}"): ("apps", "extractbi_templates_by_id"),
    ("PUT", "/apps/extractbi/templates/{id}"): ("apps", "update_extractbi_templates_by_id"),
    ("GET", "/apps/extractbi/templates/{id}/rights"): ("apps", "extractbi_templates_by_id_rights"),
    ("POST", "/apps/extractbi/test"): ("apps", "extractbi_test"),
    ("GET", "/apps/gcalendar/get-event"): ("apps", "gcalendar_get_event"),
    ("POST", "/apps/gcalendar/notifications-events"): ("apps", "gcalendar_notifications_events"),
    ("DELETE", "/apps/gcalendar/remove-event"): ("apps", "delete_gcalendar_remove_event"),
    ("GET", "/apps/gcalendar/resources/{id}"): ("apps", "gcalendar_resources_by_id"),
    ("PUT", "/apps/gcalendar/update-event"): ("apps", "update_gcalendar_update_event"),
    ("POST", "/apps/gmail/mails"): ("apps", "gmail_mails"),
    ("GET", "/apps/gmail/mails/{idMail}"): ("apps", "gmail_mails_by_id_mail"),
    ("GET", "/apps/gmail/resources/{id}"): ("apps", "gmail_resources_by_id"),
    ("GET", "/apps/gviewer/download/{id}"): ("apps", "gviewer_download_by_id"),
    ("GET", "/apps/gviewer/resources/{id}"): ("apps", "gviewer_resources_by_id"),
    ("PUT", "/apps/gviewer/resources/{id}"): ("apps", "update_gviewer_resources_by_id"),
    ("GET", "/apps/gviewer/url-documents"): ("apps", "gviewer_url_documents"),
    ("GET", "/apps/hour-accounts/configuration"): ("apps", "hour_accounts_configuration"),
    ("PUT", "/apps/hour-accounts/configuration"): ("apps", "update_hour_accounts_configuration"),
    ("GET", "/apps/hour-accounts/houraccounts"): ("apps", "hour_accounts_houraccounts"),
    ("GET", "/apps/hour-accounts/houraccounts/{id}"): ("apps", "hour_accounts_houraccounts_by_id"),
    ("PUT", "/apps/hour-accounts/houraccounts/{id}"): ("apps", "update_hour_accounts_houraccounts_by_id"),
    ("GET", "/apps/hour-accounts/houraccounts/{id}/rights"): ("apps", "hour_accounts_houraccounts_by_id_rights"),
    ("GET", "/apps/hour-accounts/resources/{id}/rights"): ("apps", "hour_accounts_resources_by_id_rights"),
    ("GET", "/apps/hour-accounts/resources/{id}/settings"): ("apps", "hour_accounts_resources_by_id_settings"),
    ("PUT", "/apps/hour-accounts/resources/{id}/settings"): ("apps", "update_hour_accounts_resources_by_id_settings"),
    ("GET", "/apps/hrflow/configuration"): ("apps", "hrflow_configuration"),
    ("PUT", "/apps/hrflow/configuration"): ("apps", "update_hrflow_configuration"),
    ("POST", "/apps/hrflow/resumes"): ("apps", "hrflow_resumes"),
    ("GET", "/apps/intranet-accounts/resources"): ("apps", "intranet_accounts_resources"),
    ("PUT", "/apps/intranet-accounts/resources/{id}"): ("apps", "update_intranet_accounts_resources_by_id"),
    ("GET", "/apps/markers/markers"): ("apps", "markers_markers"),
    ("DELETE", "/apps/microsoft/events/{idEvent}"): ("apps", "delete_microsoft_events_by_id_event"),
    ("GET", "/apps/microsoft/events/{idEvent}"): ("apps", "microsoft_events_by_id_event"),
    ("PUT", "/apps/microsoft/events/{idEvent}"): ("apps", "update_microsoft_events_by_id_event"),
    ("GET", "/apps/microsoft/events/{idEvent}/find"): ("apps", "microsoft_events_by_id_event_find"),
    ("GET", "/apps/microsoft/extra-id"): ("apps", "microsoft_extra_id"),
    ("GET", "/apps/microsoft/gadget"): ("apps", "microsoft_gadget"),
    ("GET", "/apps/microsoft/get-event"): ("apps", "microsoft_get_event"),
    ("POST", "/apps/microsoft/mails"): ("apps", "microsoft_mails"),
    ("GET", "/apps/microsoft/mails/{idMail}"): ("apps", "microsoft_mails_by_id_mail"),
    ("GET", "/apps/microsoft/manifest"): ("apps", "microsoft_manifest"),
    ("DELETE", "/apps/microsoft/remove-event"): ("apps", "delete_microsoft_remove_event"),
    ("GET", "/apps/microsoft/resources/{id}"): ("apps", "microsoft_resources_by_id"),
    ("PUT", "/apps/microsoft/update-event"): ("apps", "update_microsoft_update_event"),
    ("POST", "/apps/organization-charts/nodes"): ("apps", "organization_charts_nodes"),
    ("DELETE", "/apps/organization-charts/nodes/{id}"): ("apps", "delete_organization_charts_nodes_by_id"),
    ("PUT", "/apps/organization-charts/nodes/{id}"): ("apps", "update_organization_charts_nodes_by_id"),
    ("GET", "/apps/organization-charts/orgcharts"): ("apps", "organization_charts_orgcharts"),
    ("POST", "/apps/organization-charts/orgcharts"): ("apps", "post_organization_charts_orgcharts"),
    ("DELETE", "/apps/organization-charts/orgcharts/{id}"): ("apps", "delete_organization_charts_orgcharts_by_id"),
    ("GET", "/apps/organization-charts/orgcharts/{id}"): ("apps", "organization_charts_orgcharts_by_id"),
    ("POST", "/apps/organization-charts/settings"): ("apps", "organization_charts_settings"),
    ("DELETE", "/apps/organization-charts/settings/{id}"): ("apps", "delete_organization_charts_settings_by_id"),
    ("GET", "/apps/organization-charts/settings/{id}"): ("apps", "organization_charts_settings_by_id"),
    ("PUT", "/apps/organization-charts/settings/{id}"): ("apps", "update_organization_charts_settings_by_id"),
    ("GET", "/apps/plan-production/resources"): ("apps", "plan_production_resources"),
    ("GET", "/apps/post-production/projects"): ("apps", "post_production_projects"),
    ("PUT", "/apps/post-production/projects/{id}"): ("apps", "update_post_production_projects_by_id"),
    ("GET", "/apps/post-production/resources/{id}"): ("apps", "post_production_resources_by_id"),
    ("PUT", "/apps/post-production/resources/{id}"): ("apps", "update_post_production_resources_by_id"),
    ("GET", "/apps/quotations/quotations"): ("apps", "quotations_quotations"),
    ("POST", "/apps/quotations/quotations"): ("apps", "post_quotations_quotations"),
    ("GET", "/apps/quotations/quotations/default"): ("apps", "quotations_quotations_default"),
    ("DELETE", "/apps/quotations/quotations/{id}"): ("apps", "delete_quotations_quotations_by_id"),
    ("GET", "/apps/quotations/quotations/{id}"): ("apps", "quotations_quotations_by_id"),
    ("PUT", "/apps/quotations/quotations/{id}"): ("apps", "update_quotations_quotations_by_id"),
    ("GET", "/apps/quotations/quotations/{id}/download"): ("apps", "quotations_quotations_by_id_download"),
    ("GET", "/apps/quotations/quotations/{id}/rights"): ("apps", "quotations_quotations_by_id_rights"),
    ("POST", "/apps/quotations/quotations/{id}/send"): ("apps", "quotations_quotations_by_id_send"),
    ("GET", "/apps/quotations/quotations/{id}/tasks"): ("apps", "quotations_quotations_by_id_tasks"),
    ("GET", "/apps/resource-planner/projects/{id}"): ("apps", "resource_planner_projects_by_id"),
    ("PUT", "/apps/resource-planner/projects/{id}"): ("apps", "update_resource_planner_projects_by_id"),
    ("GET", "/apps/resource-planner/projects/{id}/rights"): ("apps", "resource_planner_projects_by_id_rights"),
    ("GET", "/apps/resource-planner/resources/{id}"): ("apps", "resource_planner_resources_by_id"),
    ("PUT", "/apps/resource-planner/resources/{id}"): ("apps", "update_resource_planner_resources_by_id"),
    ("GET", "/apps/resource-planner/resources/{id}/rights"): ("apps", "resource_planner_resources_by_id_rights"),
    ("GET", "/apps/saas-editor/configuration"): ("apps", "saas_editor_configuration"),
    ("PUT", "/apps/saas-editor/configuration"): ("apps", "update_saas_editor_configuration"),
    ("GET", "/apps/saas-editor/reporting"): ("apps", "saas_editor_reporting"),
    ("GET", "/apps/sepa/companies/{id}"): ("apps", "sepa_companies_by_id"),
    ("PUT", "/apps/sepa/companies/{id}"): ("apps", "update_sepa_companies_by_id"),
    ("GET", "/apps/sepa/configuration"): ("apps", "sepa_configuration"),
    ("PUT", "/apps/sepa/configuration"): ("apps", "update_sepa_configuration"),
    ("GET", "/apps/sepa/contracts"): ("apps", "sepa_contracts"),
    ("GET", "/apps/sepa/contracts/{id}"): ("apps", "sepa_contracts_by_id"),
    ("PUT", "/apps/sepa/contracts/{id}"): ("apps", "update_sepa_contracts_by_id"),
    ("POST", "/apps/sepa/import/contracts"): ("apps", "sepa_import__contracts"),
    ("POST", "/apps/sepa/import/orders"): ("apps", "sepa_import__orders"),
    ("POST", "/apps/sepa/import/purchases"): ("apps", "sepa_import__purchases"),
    ("POST", "/apps/sepa/import/transfers"): ("apps", "sepa_import__transfers"),
    ("GET", "/apps/sepa/invoices"): ("apps", "sepa_invoices"),
    ("GET", "/apps/sepa/orders"): ("apps", "sepa_orders"),
    ("GET", "/apps/sepa/orders/{id}"): ("apps", "sepa_orders_by_id"),
    ("PUT", "/apps/sepa/orders/{id}"): ("apps", "update_sepa_orders_by_id"),
    ("GET", "/apps/sepa/payments"): ("apps", "sepa_payments"),
    ("GET", "/apps/sepa/purchases"): ("apps", "sepa_purchases"),
    ("GET", "/apps/sepa/purchases/{id}"): ("apps", "sepa_purchases_by_id"),
    ("PUT", "/apps/sepa/purchases/{id}"): ("apps", "update_sepa_purchases_by_id"),
    ("GET", "/apps/special-reporting/reporting"): ("apps", "special_reporting_reporting"),
    ("GET", "/apps/survey/configuration"): ("apps", "survey_configuration"),
    ("PUT", "/apps/survey/configuration"): ("apps", "update_survey_configuration"),
    ("GET", "/apps/survey/enquiries/{id}"): ("apps", "survey_enquiries_by_id"),
    ("PUT", "/apps/survey/enquiries/{id}"): ("apps", "update_survey_enquiries_by_id"),
    ("GET", "/apps/survey/enquiries/{id}/rights"): ("apps", "survey_enquiries_by_id_rights"),
    ("GET", "/apps/survey/satisfaction-indicators"): ("apps", "survey_satisfaction_indicators"),
    ("GET", "/apps/survey/satisfactions"): ("apps", "survey_satisfactions"),
    ("POST", "/apps/{appCode}/install"): ("apps", "install"),
    ("DELETE", "/apps/{appCode}/uninstall"): ("apps", "delete_uninstall"),
    ("GET", "/apps/{appId}/entities"): ("apps", "entities"),
    ("POST", "/apps/{appId}/entities"): ("apps", "post_entities"),
    ("GET", "/apps/{appId}/entities/default"): ("apps", "entities_default"),
    ("GET", "/apps/{appId}/entities/dependson"): ("apps", "entities_dependson"),
    ("DELETE", "/apps/{appId}/entities/{id}"): ("apps", "delete_entities_by_id"),
    ("GET", "/apps/{appId}/entities/{id}"): ("apps", "entities_by_id"),
    ("GET", "/apps/{appId}/entities/{id}/attached-flags"): ("apps", "entities_by_id_attached_flags"),
    ("GET", "/apps/{appId}/entities/{id}/rights"): ("apps", "entities_by_id_rights"),
    ("GET", "/apps/{appId}/entities/{id}/tasks"): ("apps", "entities_by_id_tasks"),
    ("GET", "/apps/{id}"): ("apps", "get"),
    ("DELETE", "/attached-flags"): ("attached_flags", "delete_many"),
    ("POST", "/attached-flags"): ("attached_flags", "create"),
    ("GET", "/banking-accounts"): ("banking_accounts", "search"),
    ("GET", "/banking-transactions"): ("banking_transactions", "search"),
    ("GET", "/banking-transactions/{id}"): ("banking_transactions", "get"),
    ("PUT", "/banking-transactions/{id}"): ("banking_transactions", "update"),
    ("GET", "/billing-deliveries-purchases-balance"): ("billing_deliveries_purchases_balance", "search"),
    ("GET", "/billing-details"): ("billing_details", "search"),
    ("POST", "/billing-details"): ("billing_details", "create"),
    ("POST", "/billing-details/analyze"): ("billing_details", "analyze"),
    ("DELETE", "/billing-details/{id}"): ("billing_details", "delete"),
    ("GET", "/billing-details/{id}"): ("billing_details", "get"),
    ("PUT", "/billing-details/{id}"): ("billing_details", "update"),
    ("GET", "/billing-monthly-balance"): ("billing_monthly_balance", "search"),
    ("GET", "/billing-projects-balance"): ("billing_projects_balance", "search"),
    ("GET", "/billing-schedules-balance"): ("billing_schedules_balance", "search"),
    ("GET", "/boondmanager-contracts/{id}"): ("boondmanager_contracts", "get"),
    ("PUT", "/boondmanager-contracts/{id}"): ("boondmanager_contracts", "update"),
    ("GET", "/business-units"): ("business_units", "search"),
    ("POST", "/business-units"): ("business_units", "create"),
    ("GET", "/business-units/default"): ("business_units", "default"),
    ("DELETE", "/business-units/{id}"): ("business_units", "delete"),
    ("GET", "/business-units/{id}"): ("business_units", "get"),
    ("PUT", "/business-units/{id}"): ("business_units", "update"),
    ("GET", "/calendars"): ("calendars", "search"),
    ("GET", "/calendars/default"): ("calendars", "default"),
    ("GET", "/calendars/{id}"): ("calendars", "get"),
    ("PUT", "/calendars/{id}"): ("calendars", "update"),
    ("GET", "/candidates"): ("candidates", "search"),
    ("POST", "/candidates"): ("candidates", "create"),
    ("GET", "/candidates/default"): ("candidates", "default"),
    ("DELETE", "/candidates/{id}"): ("candidates", "delete"),
    ("GET", "/candidates/{id}"): ("candidates", "get"),
    ("GET", "/candidates/{id}/actions"): ("candidates", "actions"),
    ("GET", "/candidates/{id}/administrative"): ("candidates", "administrative"),
    ("PUT", "/candidates/{id}/administrative"): ("candidates", "update_administrative"),
    ("GET", "/candidates/{id}/ai/matching"): ("candidates", "ai_matching"),
    ("GET", "/candidates/{id}/ai/summary"): ("candidates", "ai_summary"),
    ("GET", "/candidates/{id}/attached-flags"): ("candidates", "attached_flags"),
    ("GET", "/candidates/{id}/download"): ("candidates", "download"),
    ("GET", "/candidates/{id}/information"): ("candidates", "information"),
    ("PUT", "/candidates/{id}/information"): ("candidates", "update_information"),
    ("POST", "/candidates/{id}/merge"): ("candidates", "merge"),
    ("GET", "/candidates/{id}/positionings"): ("candidates", "positionings"),
    ("GET", "/candidates/{id}/rights"): ("candidates", "rights"),
    ("GET", "/candidates/{id}/tasks"): ("candidates", "tasks"),
    ("GET", "/candidates/{id}/technical-data"): ("candidates", "technical_data"),
    ("PUT", "/candidates/{id}/technical-data"): ("candidates", "update_technical_data"),
    ("GET", "/candidates/{id}/technical-datas"): ("candidates", "technical_datas"),
    ("GET", "/companies"): ("companies", "search"),
    ("POST", "/companies"): ("companies", "create"),
    ("GET", "/companies/default"): ("companies", "default"),
    ("DELETE", "/companies/{id}"): ("companies", "delete"),
    ("GET", "/companies/{id}"): ("companies", "get"),
    ("GET", "/companies/{id}/actions"): ("companies", "actions"),
    ("GET", "/companies/{id}/attached-flags"): ("companies", "attached_flags"),
    ("GET", "/companies/{id}/contacts"): ("companies", "contacts"),
    ("GET", "/companies/{id}/information"): ("companies", "information"),
    ("PUT", "/companies/{id}/information"): ("companies", "update_information"),
    ("GET", "/companies/{id}/invoices"): ("companies", "invoices"),
    ("POST", "/companies/{id}/merge"): ("companies", "merge"),
    ("GET", "/companies/{id}/opportunities"): ("companies", "opportunities"),
    ("GET", "/companies/{id}/orders"): ("companies", "orders"),
    ("GET", "/companies/{id}/projects"): ("companies", "projects"),
    ("GET", "/companies/{id}/provider-invoices"): ("companies", "provider_invoices"),
    ("GET", "/companies/{id}/purchases"): ("companies", "purchases"),
    ("GET", "/companies/{id}/rights"): ("companies", "rights"),
    ("GET", "/companies/{id}/settings"): ("companies", "settings"),
    ("PUT", "/companies/{id}/settings"): ("companies", "update_settings"),
    ("GET", "/companies/{id}/tasks"): ("companies", "tasks"),
    ("GET", "/conditional-fields"): ("conditional_fields", "search"),
    ("POST", "/conditional-fields"): ("conditional_fields", "create"),
    ("GET", "/conditional-fields/default"): ("conditional_fields", "default"),
    ("DELETE", "/conditional-fields/{id}"): ("conditional_fields", "delete"),
    ("GET", "/conditional-fields/{id}"): ("conditional_fields", "get"),
    ("PUT", "/conditional-fields/{id}"): ("conditional_fields", "update"),
    ("GET", "/contacts"): ("contacts", "search"),
    ("POST", "/contacts"): ("contacts", "create"),
    ("GET", "/contacts/default"): ("contacts", "default"),
    ("DELETE", "/contacts/{id}"): ("contacts", "delete"),
    ("GET", "/contacts/{id}"): ("contacts", "get"),
    ("GET", "/contacts/{id}/actions"): ("contacts", "actions"),
    ("GET", "/contacts/{id}/attached-flags"): ("contacts", "attached_flags"),
    ("GET", "/contacts/{id}/information"): ("contacts", "information"),
    ("PUT", "/contacts/{id}/information"): ("contacts", "update_information"),
    ("GET", "/contacts/{id}/invoices"): ("contacts", "invoices"),
    ("POST", "/contacts/{id}/merge"): ("contacts", "merge"),
    ("GET", "/contacts/{id}/opportunities"): ("contacts", "opportunities"),
    ("GET", "/contacts/{id}/orders"): ("contacts", "orders"),
    ("GET", "/contacts/{id}/projects"): ("contacts", "projects"),
    ("GET", "/contacts/{id}/purchases"): ("contacts", "purchases"),
    ("GET", "/contacts/{id}/rights"): ("contacts", "rights"),
    ("GET", "/contacts/{id}/tasks"): ("contacts", "tasks"),
    ("POST", "/contracts"): ("contracts", "create"),
    ("GET", "/contracts/default"): ("contracts", "default"),
    ("DELETE", "/contracts/{id}"): ("contracts", "delete"),
    ("GET", "/contracts/{id}"): ("contracts", "get"),
    ("PUT", "/contracts/{id}"): ("contracts", "update"),
    ("GET", "/contracts/{id}/advantages"): ("contracts", "advantages"),
    ("GET", "/contracts/{id}/download"): ("contracts", "download"),
    ("GET", "/contracts/{id}/rights"): ("contracts", "rights"),
    ("GET", "/contracts/{id}/tasks"): ("contracts", "tasks"),
    ("GET", "/dashboards"): ("dashboards", "search"),
    ("POST", "/dashboards"): ("dashboards", "create"),
    ("DELETE", "/dashboards/{id}"): ("dashboards", "delete"),
    ("GET", "/dashboards/{id}"): ("dashboards", "get"),
    ("PUT", "/dashboards/{id}"): ("dashboards", "update"),
    ("POST", "/deliveries"): ("deliveries", "create"),
    ("DELETE", "/deliveries/{id}"): ("deliveries", "delete"),
    ("GET", "/deliveries/{id}"): ("deliveries", "get"),
    ("PUT", "/deliveries/{id}"): ("deliveries", "update"),
    ("GET", "/deliveries/{id}/advantages"): ("deliveries", "advantages"),
    ("GET", "/deliveries/{id}/delivery-order-download"): ("deliveries", "delivery_order_download"),
    ("GET", "/deliveries/{id}/download"): ("deliveries", "download"),
    ("POST", "/deliveries/{id}/renew"): ("deliveries", "renew"),
    ("GET", "/deliveries/{id}/rights"): ("deliveries", "rights"),
    ("POST", "/deliveries/{id}/send"): ("deliveries", "send"),
    ("GET", "/deliveries/{id}/tasks"): ("deliveries", "tasks"),
    ("GET", "/deliveries-groupments"): ("deliveries_groupments", "search"),
    ("DELETE", "/devices/{id}"): ("devices", "delete"),
    ("DELETE", "/devices/{id}/session"): ("devices", "delete_session"),
    ("POST", "/documents"): ("documents", "create"),
    ("GET", "/documents/viewer"): ("documents", "viewer"),
    ("DELETE", "/documents/{id}"): ("documents", "delete"),
    ("GET", "/documents/{id}"): ("documents", "get"),
    ("PUT", "/documents/{id}"): ("documents", "update"),
    ("GET", "/download-center"): ("download_center", "search"),
    ("DELETE", "/download-center/{perimeterManager}/{folder}"): ("download_center", "delete_by_folder"),
    ("GET", "/download-center/{perimeterManager}/{folder}"): ("download_center", "by_folder"),
    ("GET", "/download-center/{perimeterManager}/{folder}/download"): ("download_center", "by_folder_download"),
    ("DELETE", "/download-center/{perimeterManager}/{folder}/visitor-access"): ("download_center", "delete_by_folder_visitor_access"),
    ("POST", "/download-center/{perimeterManager}/{folder}/visitor-access"): ("download_center", "by_folder_visitor_access"),
    ("DELETE", "/download-center/{perimeterManager}/{folder}/{file}"): ("download_center", "delete_by_folder_by_file"),
    ("GET", "/download-center/{perimeterManager}/{folder}/{file}"): ("download_center", "by_folder_by_file"),
    ("GET", "/e-invoicing/schemes"): ("e_invoicing", "schemes"),
    ("GET", "/expenses"): ("expenses", "search"),
    ("GET", "/expenses-reports"): ("expenses_reports", "search"),
    ("POST", "/expenses-reports"): ("expenses_reports", "create"),
    ("GET", "/expenses-reports/default"): ("expenses_reports", "default"),
    ("DELETE", "/expenses-reports/{id}"): ("expenses_reports", "delete"),
    ("GET", "/expenses-reports/{id}"): ("expenses_reports", "get"),
    ("PUT", "/expenses-reports/{id}"): ("expenses_reports", "update"),
    ("POST", "/expenses-reports/{id}/certification"): ("expenses_reports", "certification"),
    ("GET", "/expenses-reports/{id}/download"): ("expenses_reports", "download"),
    ("POST", "/expenses-reports/{id}/pay"): ("expenses_reports", "pay"),
    ("POST", "/expenses-reports/{id}/reject"): ("expenses_reports", "reject"),
    ("GET", "/expenses-reports/{id}/rights"): ("expenses_reports", "rights"),
    ("POST", "/expenses-reports/{id}/unvalidate"): ("expenses_reports", "unvalidate"),
    ("POST", "/expenses-reports/{id}/validate"): ("expenses_reports", "validate"),
    ("GET", "/flags"): ("flags", "search"),
    ("POST", "/flags"): ("flags", "create"),
    ("DELETE", "/flags/{id}"): ("flags", "delete"),
    ("GET", "/flags/{id}"): ("flags", "get"),
    ("PUT", "/flags/{id}"): ("flags", "update"),
    ("POST", "/followed-documents"): ("followed_documents", "create"),
    ("GET", "/followed-documents/default"): ("followed_documents", "default"),
    ("DELETE", "/followed-documents/{id}"): ("followed_documents", "delete"),
    ("GET", "/followed-documents/{id}"): ("followed_documents", "get"),
    ("PUT", "/followed-documents/{id}"): ("followed_documents", "update"),
    ("GET", "/followed-documents/{id}/rights"): ("followed_documents", "rights"),
    ("POST", "/forms"): ("forms", "create"),
    ("GET", "/forms/default"): ("forms", "default"),
    ("GET", "/forms/templates"): ("forms", "templates"),
    ("POST", "/forms/templates"): ("forms", "post_templates"),
    ("GET", "/forms/templates/default"): ("forms", "templates_default"),
    ("DELETE", "/forms/templates/{id}"): ("forms", "delete_templates_by_id"),
    ("GET", "/forms/templates/{id}"): ("forms", "templates_by_id"),
    ("PUT", "/forms/templates/{id}"): ("forms", "update_templates_by_id"),
    ("DELETE", "/forms/{id}"): ("forms", "delete"),
    ("GET", "/forms/{id}"): ("forms", "get"),
    ("PUT", "/forms/{id}"): ("forms", "update"),
    ("POST", "/forms/{id}/remind"): ("forms", "remind"),
    ("GET", "/forms/{id}/rights"): ("forms", "rights"),
    ("GET", "/forms/{id}/tasks"): ("forms", "tasks"),
    ("GET", "/gadgets/{id}/values"): ("gadgets", "values"),
    ("DELETE", "/google/{id}"): ("google", "delete"),
    ("POST", "/groupments"): ("groupments", "create"),
    ("GET", "/groupments/default"): ("groupments", "default"),
    ("POST", "/groupments/duplicate"): ("groupments", "duplicate"),
    ("DELETE", "/groupments/{id}"): ("groupments", "delete"),
    ("GET", "/groupments/{id}"): ("groupments", "get"),
    ("PUT", "/groupments/{id}"): ("groupments", "update"),
    ("GET", "/groupments/{id}/rights"): ("groupments", "rights"),
    ("POST", "/import/actions"): ("import_", "actions"),
    ("POST", "/import/candidates"): ("import_", "candidates"),
    ("POST", "/import/contacts"): ("import_", "contacts"),
    ("POST", "/import/opportunities"): ("import_", "opportunities"),
    ("POST", "/import/resources"): ("import_", "resources"),
    ("POST", "/inactivities"): ("inactivities", "create"),
    ("GET", "/inactivities/default"): ("inactivities", "default"),
    ("DELETE", "/inactivities/{id}"): ("inactivities", "delete"),
    ("GET", "/inactivities/{id}"): ("inactivities", "get"),
    ("PUT", "/inactivities/{id}"): ("inactivities", "update"),
    ("GET", "/inactivities/{id}/rights"): ("inactivities", "rights"),
    ("GET", "/invoices"): ("invoices", "search"),
    ("POST", "/invoices"): ("invoices", "create"),
    ("POST", "/invoices/bulk-send"): ("invoices", "bulk_send"),
    ("GET", "/invoices/cart"): ("invoices", "cart"),
    ("GET", "/invoices/default"): ("invoices", "default"),
    ("DELETE", "/invoices/{id}"): ("invoices", "delete"),
    ("GET", "/invoices/{id}"): ("invoices", "get"),
    ("GET", "/invoices/{id}/actions"): ("invoices", "actions"),
    ("PUT", "/invoices/{id}/adjust"): ("invoices", "update_adjust"),
    ("GET", "/invoices/{id}/attached-flags"): ("invoices", "attached_flags"),
    ("GET", "/invoices/{id}/billable-items"): ("invoices", "billable_items"),
    ("GET", "/invoices/{id}/check"): ("invoices", "check"),
    ("GET", "/invoices/{id}/download"): ("invoices", "download"),
    ("GET", "/invoices/{id}/information"): ("invoices", "information"),
    ("PUT", "/invoices/{id}/information"): ("invoices", "update_information"),
    ("GET", "/invoices/{id}/preview"): ("invoices", "preview"),
    ("GET", "/invoices/{id}/rights"): ("invoices", "rights"),
    ("POST", "/invoices/{id}/send"): ("invoices", "send"),
    ("GET", "/invoices/{id}/tasks"): ("invoices", "tasks"),
    ("GET", "/invoicing-connections"): ("invoicing_connections", "search"),
    ("POST", "/invoicing-connections"): ("invoicing_connections", "create"),
    ("POST", "/invoicing-connections/authorize"): ("invoicing_connections", "authorize"),
    ("GET", "/invoicing-connections/callback"): ("invoicing_connections", "callback"),
    ("DELETE", "/invoicing-connections/{id}"): ("invoicing_connections", "delete"),
    ("GET", "/invoicing-connections/{id}"): ("invoicing_connections", "get"),
    ("PUT", "/invoicing-connections/{id}"): ("invoicing_connections", "update"),
    ("GET", "/logs"): ("logs", "search"),
    ("GET", "/logs/{id}"): ("logs", "get"),
    ("GET", "/mandatory-leave"): ("mandatory_leave", "search"),
    ("POST", "/mandatory-leave"): ("mandatory_leave", "create"),
    ("DELETE", "/mandatory-leave/{id}"): ("mandatory_leave", "delete"),
    ("GET", "/mandatory-leave/{id}"): ("mandatory_leave", "get"),
    ("GET", "/mandatory-leave/{id}/information"): ("mandatory_leave", "information"),
    ("PUT", "/mandatory-leave/{id}/information"): ("mandatory_leave", "update_information"),
    ("GET", "/mandatory-leave/{id}/resources"): ("mandatory_leave", "resources"),
    ("PUT", "/mandatory-leave/{id}/resources"): ("mandatory_leave", "update_resources"),
    ("GET", "/mandatory-leave/{id}/rights"): ("mandatory_leave", "rights"),
    ("GET", "/marketplace"): ("marketplace", "search"),
    ("POST", "/marketplace"): ("marketplace", "create"),
    ("GET", "/marketplace/default"): ("marketplace", "default"),
    ("POST", "/marketplace/refresh-token"): ("marketplace", "refresh_token"),
    ("GET", "/marketplace/{appCode}/configure"): ("marketplace", "configure"),
    ("PUT", "/marketplace/{appCode}/configure"): ("marketplace", "update_configure"),
    ("DELETE", "/marketplace/{id}"): ("marketplace", "delete"),
    ("GET", "/marketplace/{id}"): ("marketplace", "get"),
    ("PUT", "/marketplace/{id}"): ("marketplace", "update"),
    ("GET", "/marketplace/{id}/data-visualization"): ("marketplace", "data_visualization"),
    ("POST", "/marketplace/{id}/install"): ("marketplace", "install"),
    ("DELETE", "/marketplace/{id}/logo"): ("marketplace", "delete_logo"),
    ("PUT", "/marketplace/{id}/logo"): ("marketplace", "update_logo"),
    ("POST", "/marketplace/{id}/publish"): ("marketplace", "publish"),
    ("GET", "/marketplace/{id}/rights"): ("marketplace", "rights"),
    ("GET", "/marketplace/{id}/translations"): ("marketplace", "translations"),
    ("PUT", "/marketplace/{id}/translations"): ("marketplace", "update_translations"),
    ("DELETE", "/marketplace/{id}/uninstall"): ("marketplace", "delete_uninstall"),
    ("POST", "/marketplace/{id}/validate"): ("marketplace", "validate"),
    ("DELETE", "/microsoft/{id}"): ("microsoft", "delete"),
    ("GET", "/notifications"): ("notifications", "search"),
    ("PUT", "/notifications/markas"): ("notifications", "update_markas"),
    ("GET", "/notifications/{id}"): ("notifications", "get"),
    ("PUT", "/notifications/{id}"): ("notifications", "update"),
    ("GET", "/opportunities"): ("opportunities", "search"),
    ("POST", "/opportunities"): ("opportunities", "create"),
    ("GET", "/opportunities/ai/parsing/{jobId}"): ("opportunities", "ai_parsing_by_job_id"),
    ("GET", "/opportunities/default"): ("opportunities", "default"),
    ("DELETE", "/opportunities/{id}"): ("opportunities", "delete"),
    ("GET", "/opportunities/{id}"): ("opportunities", "get"),
    ("GET", "/opportunities/{id}/actions"): ("opportunities", "actions"),
    ("POST", "/opportunities/{id}/ai/assistant"): ("opportunities", "ai_assistant"),
    ("GET", "/opportunities/{id}/ai/matching"): ("opportunities", "ai_matching"),
    ("GET", "/opportunities/{id}/attached-flags"): ("opportunities", "attached_flags"),
    ("GET", "/opportunities/{id}/download"): ("opportunities", "download"),
    ("GET", "/opportunities/{id}/information"): ("opportunities", "information"),
    ("PUT", "/opportunities/{id}/information"): ("opportunities", "update_information"),
    ("GET", "/opportunities/{id}/positionings"): ("opportunities", "positionings"),
    ("GET", "/opportunities/{id}/projects"): ("opportunities", "projects"),
    ("GET", "/opportunities/{id}/rights"): ("opportunities", "rights"),
    ("GET", "/opportunities/{id}/simulation"): ("opportunities", "simulation"),
    ("PUT", "/opportunities/{id}/simulation"): ("opportunities", "update_simulation"),
    ("GET", "/opportunities/{id}/tasks"): ("opportunities", "tasks"),
    ("GET", "/orders"): ("orders", "search"),
    ("POST", "/orders"): ("orders", "create"),
    ("GET", "/orders/default"): ("orders", "default"),
    ("DELETE", "/orders/{id}"): ("orders", "delete"),
    ("GET", "/orders/{id}"): ("orders", "get"),
    ("GET", "/orders/{id}/actions"): ("orders", "actions"),
    ("GET", "/orders/{id}/attached-flags"): ("orders", "attached_flags"),
    ("GET", "/orders/{id}/download"): ("orders", "download"),
    ("GET", "/orders/{id}/information"): ("orders", "information"),
    ("PUT", "/orders/{id}/information"): ("orders", "update_information"),
    ("GET", "/orders/{id}/invoices"): ("orders", "invoices"),
    ("GET", "/orders/{id}/rights"): ("orders", "rights"),
    ("GET", "/orders/{id}/tasks"): ("orders", "tasks"),
    ("GET", "/payments"): ("payments", "search"),
    ("POST", "/payments"): ("payments", "create"),
    ("GET", "/payments/default"): ("payments", "default"),
    ("DELETE", "/payments/{id}"): ("payments", "delete"),
    ("GET", "/payments/{id}"): ("payments", "get"),
    ("PUT", "/payments/{id}"): ("payments", "update"),
    ("GET", "/payments/{id}/rights"): ("payments", "rights"),
    ("GET", "/payments/{id}/tasks"): ("payments", "tasks"),
    ("GET", "/planning-absences"): ("planning_absences", "search"),
    ("GET", "/poles"): ("poles", "search"),
    ("POST", "/poles"): ("poles", "create"),
    ("DELETE", "/poles/{id}"): ("poles", "delete"),
    ("GET", "/poles/{id}"): ("poles", "get"),
    ("PUT", "/poles/{id}"): ("poles", "update"),
    ("GET", "/positionings"): ("positionings", "search"),
    ("POST", "/positionings"): ("positionings", "create"),
    ("PUT", "/positionings/bulk-update"): ("positionings", "update_bulk_update"),
    ("DELETE", "/positionings/{id}"): ("positionings", "delete"),
    ("GET", "/positionings/{id}"): ("positionings", "get"),
    ("PUT", "/positionings/{id}"): ("positionings", "update"),
    ("GET", "/positionings/{id}/attached-flags"): ("positionings", "attached_flags"),
    ("GET", "/positionings/{id}/rights"): ("positionings", "rights"),
    ("GET", "/positionings/{id}/tasks"): ("positionings", "tasks"),
    ("GET", "/products"): ("products", "search"),
    ("POST", "/products"): ("products", "create"),
    ("GET", "/products/default"): ("products", "default"),
    ("DELETE", "/products/{id}"): ("products", "delete"),
    ("GET", "/products/{id}"): ("products", "get"),
    ("GET", "/products/{id}/attached-flags"): ("products", "attached_flags"),
    ("GET", "/products/{id}/information"): ("products", "information"),
    ("PUT", "/products/{id}/information"): ("products", "update_information"),
    ("GET", "/products/{id}/opportunities"): ("products", "opportunities"),
    ("GET", "/products/{id}/projects"): ("products", "projects"),
    ("GET", "/products/{id}/rights"): ("products", "rights"),
    ("GET", "/products/{id}/tasks"): ("products", "tasks"),
    ("GET", "/projects"): ("projects", "search"),
    ("POST", "/projects"): ("projects", "create"),
    ("GET", "/projects/carts"): ("projects", "carts"),
    ("GET", "/projects/carts/widgets"): ("projects", "carts_widgets"),
    ("DELETE", "/projects/{id}"): ("projects", "delete"),
    ("GET", "/projects/{id}"): ("projects", "get"),
    ("GET", "/projects/{id}/actions"): ("projects", "actions"),
    ("GET", "/projects/{id}/advantages"): ("projects", "advantages"),
    ("GET", "/projects/{id}/attached-flags"): ("projects", "attached_flags"),
    ("GET", "/projects/{id}/batches-markers"): ("projects", "batches_markers"),
    ("PUT", "/projects/{id}/batches-markers"): ("projects", "update_batches_markers"),
    ("GET", "/projects/{id}/deliveries-groupments"): ("projects", "deliveries_groupments"),
    ("GET", "/projects/{id}/information"): ("projects", "information"),
    ("PUT", "/projects/{id}/information"): ("projects", "update_information"),
    ("GET", "/projects/{id}/orders"): ("projects", "orders"),
    ("GET", "/projects/{id}/productivity"): ("projects", "productivity"),
    ("GET", "/projects/{id}/purchases"): ("projects", "purchases"),
    ("GET", "/projects/{id}/rights"): ("projects", "rights"),
    ("GET", "/projects/{id}/simulation"): ("projects", "simulation"),
    ("PUT", "/projects/{id}/simulation"): ("projects", "update_simulation"),
    ("GET", "/projects/{id}/tasks"): ("projects", "tasks"),
    ("GET", "/provider-invoices"): ("provider_invoices", "search"),
    ("POST", "/provider-invoices"): ("provider_invoices", "create"),
    ("GET", "/provider-invoices/default"): ("provider_invoices", "default"),
    ("DELETE", "/provider-invoices/{id}"): ("provider_invoices", "delete"),
    ("GET", "/provider-invoices/{id}"): ("provider_invoices", "get"),
    ("PUT", "/provider-invoices/{id}"): ("provider_invoices", "update"),
    ("GET", "/provider-invoices/{id}/activity-expenses"): ("provider_invoices", "activity_expenses"),
    ("GET", "/provider-invoices/{id}/rights"): ("provider_invoices", "rights"),
    ("GET", "/purchases"): ("purchases", "search"),
    ("POST", "/purchases"): ("purchases", "create"),
    ("GET", "/purchases/default"): ("purchases", "default"),
    ("DELETE", "/purchases/{id}"): ("purchases", "delete"),
    ("GET", "/purchases/{id}"): ("purchases", "get"),
    ("GET", "/purchases/{id}/attached-flags"): ("purchases", "attached_flags"),
    ("GET", "/purchases/{id}/download"): ("purchases", "download"),
    ("GET", "/purchases/{id}/information"): ("purchases", "information"),
    ("PUT", "/purchases/{id}/information"): ("purchases", "update_information"),
    ("GET", "/purchases/{id}/payments"): ("purchases", "payments"),
    ("GET", "/purchases/{id}/rights"): ("purchases", "rights"),
    ("GET", "/purchases/{id}/simulation"): ("purchases", "simulation"),
    ("GET", "/purchases/{id}/tasks"): ("purchases", "tasks"),
    ("GET", "/reporting-companies"): ("reporting_companies", "search"),
    ("GET", "/reporting-production-plans"): ("reporting_production_plans", "search"),
    ("GET", "/reporting-projects"): ("reporting_projects", "search"),
    ("GET", "/reporting-resources"): ("reporting_resources", "search"),
    ("GET", "/reporting-synthesis"): ("reporting_synthesis", "search"),
    ("GET", "/resources"): ("resources", "search"),
    ("POST", "/resources"): ("resources", "create"),
    ("GET", "/resources/default"): ("resources", "default"),
    ("DELETE", "/resources/{id}"): ("resources", "delete"),
    ("GET", "/resources/{id}"): ("resources", "get"),
    ("GET", "/resources/{id}/absences-accounts"): ("resources", "absences_accounts"),
    ("GET", "/resources/{id}/absences-reports"): ("resources", "absences_reports"),
    ("GET", "/resources/{id}/actions"): ("resources", "actions"),
    ("GET", "/resources/{id}/administrative"): ("resources", "administrative"),
    ("PUT", "/resources/{id}/administrative"): ("resources", "update_administrative"),
    ("GET", "/resources/{id}/advantages"): ("resources", "advantages"),
    ("GET", "/resources/{id}/ai/matching"): ("resources", "ai_matching"),
    ("GET", "/resources/{id}/ai/summary"): ("resources", "ai_summary"),
    ("GET", "/resources/{id}/attached-flags"): ("resources", "attached_flags"),
    ("GET", "/resources/{id}/deliveries-inactivities"): ("resources", "deliveries_inactivities"),
    ("GET", "/resources/{id}/download"): ("resources", "download"),
    ("GET", "/resources/{id}/expenses-reports"): ("resources", "expenses_reports"),
    ("GET", "/resources/{id}/followed-documents"): ("resources", "followed_documents"),
    ("GET", "/resources/{id}/forms"): ("resources", "forms"),
    ("GET", "/resources/{id}/information"): ("resources", "information"),
    ("PUT", "/resources/{id}/information"): ("resources", "update_information"),
    ("GET", "/resources/{id}/positionings"): ("resources", "positionings"),
    ("GET", "/resources/{id}/projects"): ("resources", "projects"),
    ("GET", "/resources/{id}/provider-invoices"): ("resources", "provider_invoices"),
    ("GET", "/resources/{id}/rights"): ("resources", "rights"),
    ("GET", "/resources/{id}/settings/absences-accounts"): ("resources", "settings_absences_accounts"),
    ("PUT", "/resources/{id}/settings/absences-accounts"): ("resources", "update_settings_absences_accounts"),
    ("GET", "/resources/{id}/settings/alerts"): ("resources", "settings_alerts"),
    ("PUT", "/resources/{id}/settings/alerts"): ("resources", "update_settings_alerts"),
    ("POST", "/resources/{id}/settings/alerts/reset"): ("resources", "settings_alerts_reset"),
    ("GET", "/resources/{id}/settings/dashboards"): ("resources", "settings_dashboards"),
    ("GET", "/resources/{id}/settings/groups"): ("resources", "settings_groups"),
    ("PUT", "/resources/{id}/settings/groups"): ("resources", "update_settings_groups"),
    ("GET", "/resources/{id}/settings/intranet"): ("resources", "settings_intranet"),
    ("PUT", "/resources/{id}/settings/intranet"): ("resources", "update_settings_intranet"),
    ("GET", "/resources/{id}/settings/notifications"): ("resources", "settings_notifications"),
    ("PUT", "/resources/{id}/settings/notifications"): ("resources", "update_settings_notifications"),
    ("GET", "/resources/{id}/settings/positioning-suggests"): ("resources", "settings_positioning_suggests"),
    ("PUT", "/resources/{id}/settings/positioning-suggests"): ("resources", "update_settings_positioning_suggests"),
    ("GET", "/resources/{id}/settings/reporting"): ("resources", "settings_reporting"),
    ("PUT", "/resources/{id}/settings/reporting"): ("resources", "update_settings_reporting"),
    ("GET", "/resources/{id}/settings/security"): ("resources", "settings_security"),
    ("PUT", "/resources/{id}/settings/security"): ("resources", "update_settings_security"),
    ("GET", "/resources/{id}/settings/targets"): ("resources", "settings_targets"),
    ("GET", "/resources/{id}/tasks"): ("resources", "tasks"),
    ("GET", "/resources/{id}/technical-data"): ("resources", "technical_data"),
    ("PUT", "/resources/{id}/technical-data"): ("resources", "update_technical_data"),
    ("GET", "/resources/{id}/technical-datas"): ("resources", "technical_datas"),
    ("GET", "/resources/{id}/times-reports"): ("resources", "times_reports"),
    ("GET", "/roles"): ("roles", "search"),
    ("POST", "/roles"): ("roles", "create"),
    ("GET", "/roles/default"): ("roles", "default"),
    ("GET", "/roles/templates"): ("roles", "templates"),
    ("POST", "/roles/templates"): ("roles", "post_templates"),
    ("GET", "/roles/templates/default"): ("roles", "templates_default"),
    ("DELETE", "/roles/templates/{id}"): ("roles", "delete_templates_by_id"),
    ("GET", "/roles/templates/{id}"): ("roles", "templates_by_id"),
    ("PUT", "/roles/templates/{id}"): ("roles", "update_templates_by_id"),
    ("DELETE", "/roles/{id}"): ("roles", "delete"),
    ("GET", "/roles/{id}"): ("roles", "get"),
    ("PUT", "/roles/{id}"): ("roles", "update"),
    ("POST", "/sandbox"): ("sandbox", "create"),
    ("GET", "/sandbox/connect"): ("sandbox", "connect"),
    ("GET", "/savedsearches"): ("savedsearches", "search"),
    ("POST", "/savedsearches"): ("savedsearches", "create"),
    ("DELETE", "/savedsearches/{id}"): ("savedsearches", "delete"),
    ("GET", "/savedsearches/{id}"): ("savedsearches", "get"),
    ("PUT", "/savedsearches/{id}"): ("savedsearches", "update"),
    ("POST", "/share"): ("share", "create"),
    ("GET", "/share/default"): ("share", "default"),
    ("DELETE", "/signature"): ("signature", "delete_many"),
    ("GET", "/signature"): ("signature", "search"),
    ("PUT", "/signature"): ("signature", "update_many"),
    ("GET", "/signatures/document/{id}"): ("signatures", "document_by_id"),
    ("GET", "/standard-profiles"): ("standard_profiles", "search"),
    ("POST", "/standard-profiles"): ("standard_profiles", "create"),
    ("GET", "/standard-profiles/default"): ("standard_profiles", "default"),
    ("DELETE", "/standard-profiles/{id}"): ("standard_profiles", "delete"),
    ("GET", "/standard-profiles/{id}"): ("standard_profiles", "get"),
    ("PUT", "/standard-profiles/{id}"): ("standard_profiles", "update"),
    ("GET", "/standard-profiles/{id}/rights"): ("standard_profiles", "rights"),
    ("GET", "/subscription"): ("subscription", "search"),
    ("PUT", "/subscription"): ("subscription", "update_many"),
    ("GET", "/subscription/invoices"): ("subscription", "invoices"),
    ("GET", "/subscription/invoices/{id}/download"): ("subscription", "invoices_by_id_download"),
    ("POST", "/targets"): ("targets", "create"),
    ("DELETE", "/targets/{id}"): ("targets", "delete"),
    ("GET", "/targets/{id}"): ("targets", "get"),
    ("PUT", "/targets/{id}"): ("targets", "update"),
    ("GET", "/tasks/{id}"): ("tasks", "get"),
    ("POST", "/tasks/{id}/check"): ("tasks", "check"),
    ("POST", "/tasks/{id}/uncheck"): ("tasks", "uncheck"),
    ("POST", "/technical-datas"): ("technical_datas", "create"),
    ("GET", "/technical-datas/default"): ("technical_datas", "default"),
    ("GET", "/technical-datas/visitor-access"): ("technical_datas", "visitor_access"),
    ("DELETE", "/technical-datas/{id}"): ("technical_datas", "delete"),
    ("GET", "/technical-datas/{id}"): ("technical_datas", "get"),
    ("PUT", "/technical-datas/{id}"): ("technical_datas", "update"),
    ("PUT", "/technical-datas/{id}/applyresume"): ("technical_datas", "update_applyresume"),
    ("GET", "/technical-datas/{id}/download"): ("technical_datas", "download"),
    ("GET", "/threads"): ("threads", "search"),
    ("POST", "/threads"): ("threads", "create"),
    ("GET", "/threads/default"): ("threads", "default"),
    ("DELETE", "/threads/{id}"): ("threads", "delete"),
    ("GET", "/threads/{id}"): ("threads", "get"),
    ("PUT", "/threads/{id}"): ("threads", "update"),
    ("POST", "/thumbnails"): ("thumbnails", "create"),
    ("DELETE", "/thumbnails/{id}"): ("thumbnails", "delete"),
    ("GET", "/thumbnails/{id}"): ("thumbnails", "get"),
    ("GET", "/times"): ("times", "search"),
    ("GET", "/times-reports"): ("times_reports", "search"),
    ("POST", "/times-reports"): ("times_reports", "create"),
    ("GET", "/times-reports/default"): ("times_reports", "default"),
    ("DELETE", "/times-reports/{id}"): ("times_reports", "delete"),
    ("GET", "/times-reports/{id}"): ("times_reports", "get"),
    ("PUT", "/times-reports/{id}"): ("times_reports", "update"),
    ("GET", "/times-reports/{id}/download"): ("times_reports", "download"),
    ("POST", "/times-reports/{id}/reject"): ("times_reports", "reject"),
    ("GET", "/times-reports/{id}/rights"): ("times_reports", "rights"),
    ("POST", "/times-reports/{id}/signature"): ("times_reports", "signature"),
    ("POST", "/times-reports/{id}/unvalidate"): ("times_reports", "unvalidate"),
    ("POST", "/times-reports/{id}/validate"): ("times_reports", "validate"),
    ("GET", "/todolists"): ("todolists", "search"),
    ("POST", "/todolists"): ("todolists", "create"),
    ("DELETE", "/todolists/{id}"): ("todolists", "delete"),
    ("GET", "/todolists/{id}"): ("todolists", "get"),
    ("PUT", "/todolists/{id}"): ("todolists", "update"),
    ("DELETE", "/trustelem/{id}"): ("trustelem", "delete"),
    ("GET", "/validations"): ("validations", "search"),
    ("POST", "/validations"): ("validations", "create"),
    ("DELETE", "/validations/{id}"): ("validations", "delete"),
    ("GET", "/validations/{id}"): ("validations", "get"),
    ("PUT", "/validations/{id}"): ("validations", "update"),
    ("GET", "/vendor"): ("vendor", "search"),
    ("PUT", "/vendor"): ("vendor", "update_many"),
    ("DELETE", "/vendor/logo"): ("vendor", "delete_logo"),
    ("PUT", "/vendor/logo"): ("vendor", "update_logo"),
    ("GET", "/webhooks"): ("webhooks", "search"),
    ("POST", "/webhooks"): ("webhooks", "create"),
    ("DELETE", "/webhooks/{id}"): ("webhooks", "delete"),
    ("GET", "/webhooks/{id}"): ("webhooks", "get"),
    ("PUT", "/webhooks/{id}"): ("webhooks", "update"),
    ("GET", "/workplaces-times"): ("workplaces_times", "search"),
}
