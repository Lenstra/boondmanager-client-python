"""Vendored BoondManager API spec: endpoint registry + request-body schemas.

The bundle (_spec/spec.json.gz) is generated from BoondManager's public RAML
build by scripts/fetch_spec.py. It drives two things:

- pre-send request-body validation (the API silently drops non-conforming
  items while returning 200, so catching mismatches client-side is the only
  reliable guard);
- the generated method surface in api.py.
"""

from __future__ import annotations

import gzip
import json
import keyword
import re
from functools import lru_cache
from importlib import resources


@lru_cache(maxsize=1)
def _bundle() -> dict:
    data = (resources.files("boondmanager") / "_spec" / "spec.json.gz").read_bytes()
    return json.loads(gzip.decompress(data))


def endpoints() -> list[dict]:
    """All endpoints: [{"path": "/times-reports/{id}", "methods": {...}}, ...]"""
    return _bundle()["endpoints"]


def schema(name: str) -> dict | None:
    """Request-body JSON schema by name (e.g. "timesReportsBody-put")."""
    return _bundle()["schemas"].get(name)


def snake(segment: str) -> str:
    """kebab-case / camelCase path segment -> python identifier."""
    s = segment.replace("-", "_")
    s = re.sub(r"(?<=[a-z0-9])([A-Z])", r"_\1", s).lower()
    return s + "_" if keyword.iskeyword(s) else s


@lru_cache(maxsize=1)
def _routes() -> list[tuple[list[str], dict]]:
    return [(e["path"].strip("/").split("/"), e) for e in endpoints()]


@lru_cache(maxsize=256)
def match(method: str, path: str) -> dict | None:
    """Find the endpoint method entry for a concrete request.

    Returns {"path": ..., "description": ..., "body_schema": ...} or None if
    the path is not in the spec. Literal segments beat {param} segments, so
    /times-reports/default resolves before /times-reports/{id}.
    """
    method = method.lower()
    segments = path.strip("/").split("/")
    best: tuple[int, dict] | None = None
    for tmpl, entry in _routes():
        if len(tmpl) != len(segments) or method not in entry["methods"]:
            continue
        literals = 0
        for t, s in zip(tmpl, segments):
            if t.startswith("{"):
                continue
            if t != s:
                break
            literals += 1
        else:
            if best is None or literals > best[0]:
                best = (literals, entry)
    if best is None:
        return None
    entry = best[1]
    return {"path": entry["path"], **entry["methods"][method]}
