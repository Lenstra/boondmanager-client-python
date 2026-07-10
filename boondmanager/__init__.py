"""Async Python client for the BoondManager API, driven by its published spec.

Three layers, pick the highest one that covers the need:

1. Domain objects — ``client.fetch_timesheet(id)`` returns a ``Timesheet``
   grid (``ts.row(project=...).set(date, dur)``, ``await ts.save()``) that
   hides every wire-format quirk of timesheet editing.
2. Curated helpers on ``BoondManagerClient`` — ``get_times_report``,
   ``create_absences_report``, ... returning pydantic models.
3. Full generated surface — ``client.api.<group>.<method>()`` covers all 844
   endpoints and returns ``Document`` (JSON:API navigation). Find methods by
   grepping ``docs/API.md`` or via ``boondmanager.api.ENDPOINT_INDEX``; each
   docstring lists the endpoint's query parameters and body schema.

Every request body is validated against BoondManager's own JSON schemas
before sending (``BoondManagerValidationError``) because the API silently
drops non-conforming payload items while returning 200.
"""

from .api import BoondManagerAPI
from .client import BoondManagerClient
from .exceptions import (
    BoondManagerAPIError,
    BoondManagerError,
    BoondManagerSilentDropError,
    BoondManagerValidationError,
    TimesheetNotEditableError,
)
from .jsonapi import Document, Entity
from .models import (
    AbsencePeriod,
    AbsencesReport,
    AbsencesReportAttributes,
    BatchRef,
    Company,
    CreateAbsencePeriod,
    CurrentUser,
    DeliveryRef,
    EditableRow,
    Positioning,
    Project,
    ProjectRef,
    ProjectSummary,
    Resource,
    ResourceAttributes,
    TimeEntry,
    TimesReport,
    TimesReportAttributes,
    TimesReportRow,
    WorkUnitType,
)
from .timesheets import Timesheet, TimesheetRow

__all__ = [
    # Client
    "BoondManagerClient",
    "BoondManagerAPI",
    # Exceptions
    "BoondManagerError",
    "BoondManagerAPIError",
    "BoondManagerValidationError",
    "BoondManagerSilentDropError",
    "TimesheetNotEditableError",
    # High-level domain objects
    "Timesheet",
    "TimesheetRow",
    # JSON:API navigation
    "Document",
    "Entity",
    # Models — read
    "CurrentUser",
    "Resource",
    "ResourceAttributes",
    "TimesReport",
    "TimesReportAttributes",
    "TimesReportRow",
    "EditableRow",
    "TimeEntry",
    "WorkUnitType",
    "ProjectRef",
    "DeliveryRef",
    "BatchRef",
    "Company",
    "Positioning",
    "Project",
    "ProjectSummary",
    "AbsencesReport",
    "AbsencesReportAttributes",
    "AbsencePeriod",
    # Models — write
    "CreateAbsencePeriod",
]
