"""Exceptions for the BoondManager client."""

from __future__ import annotations


class BoondManagerError(Exception):
    """Base exception for all BoondManager client errors."""


class BoondManagerAPIError(BoondManagerError):
    """An HTTP error returned by the BoondManager API."""

    def __init__(self, status_code: int, endpoint: str, detail: str) -> None:
        self.status_code = status_code
        self.endpoint = endpoint
        self.detail = detail
        super().__init__(f"BoondManager {status_code} on {endpoint}: {detail}")


class BoondManagerValidationError(BoondManagerError):
    """The request body does not match BoondManager's published JSON schema.

    Raised BEFORE the request is sent. The API returns 200 while silently
    dropping non-conforming payload items, so a schema mismatch that reaches
    the server manifests as unexplained data loss — this error surfaces it
    with the exact violations instead.
    """

    def __init__(self, endpoint: str, schema_name: str, errors: list[str]) -> None:
        self.endpoint = endpoint
        self.schema_name = schema_name
        self.errors = errors
        details = "\n  - ".join(errors)
        super().__init__(
            f"Request body for {endpoint} violates schema {schema_name}:\n  - {details}"
        )


class BoondManagerSilentDropError(BoondManagerError):
    """The API accepted a write (200) but persisted fewer items than sent.

    This happens when an item is schema-valid but semantically rejected
    (e.g. a row/delivery/project id that does not exist or is not allowed).
    """

    def __init__(self, endpoint: str, detail: str) -> None:
        self.endpoint = endpoint
        super().__init__(f"BoondManager silently dropped data on {endpoint}: {detail}")


class TimesheetNotEditableError(BoondManagerError):
    """The timesheet is validated/closed and cannot be modified."""

    def __init__(self, report_id: str, state: str) -> None:
        self.report_id = report_id
        self.state = state
        super().__init__(f"Timesheet {report_id} is not editable (state: {state})")
