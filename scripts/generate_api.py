"""Generate boondmanager/api.py (namespaced API surface) from the spec bundle.

Endpoints are grouped by their first path segment into namespace classes:

    GET    /times-reports                -> client.api.times_reports.search(params=...)
    POST   /times-reports                -> client.api.times_reports.create(body)
    GET    /times-reports/{id}           -> client.api.times_reports.get(id)
    PUT    /times-reports/{id}           -> client.api.times_reports.update(id, body)
    DELETE /times-reports/{id}           -> client.api.times_reports.delete(id)
    POST   /times-reports/{id}/validate  -> client.api.times_reports.validate(id)
    GET    /times-reports/default        -> client.api.times_reports.default()
    GET    /resources/{id}/times-reports -> client.api.resources.times_reports(id)

All methods return boondmanager.jsonapi.Document.

Run from the package root (after scripts/fetch_spec.py):

    uv run python scripts/generate_api.py
"""

from __future__ import annotations

import gzip
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from boondmanager.spec import snake  # noqa: E402

OUT = ROOT / "boondmanager" / "api.py"
DOCS_OUT = ROOT / "docs" / "API.md"

DOCS_HEADER = """\
# BoondManager client — API index (generated, do not edit)

One line per endpoint method of `client.api`. Grep this file to find the
right call, then read its docstring in `boondmanager/api.py` for query
parameters and body schema.

Conventions:

- `client.api.<group>.<method>(...)` — all methods are async and return a
  `boondmanager.jsonapi.Document` (dict-compatible; `.one`/`.many`/`.included()`).
- `params` marked with `*` are required query parameters.
- Prefer the higher-level layers when they cover your need:
  `client.fetch_timesheet(id)` for timesheet editing (see
  `boondmanager/timesheets.py`), and the curated helpers on
  `BoondManagerClient` (`get_times_report`, `create_absences_report`, ...).
"""


def docs_line(name: str, verb: str, path: str, info: dict) -> str:
    args = path_params(path)
    if verb in ("post", "put"):
        args.append("body")
    required = [p["name"] + "*" for p in info.get("params", []) if p.get("required")]
    if required:
        args.append("params={" + ", ".join(required) + "}")
    desc = (info.get("description") or "").strip().splitlines()
    summary = desc[0].strip() if desc else ""
    return f"- `{name}({', '.join(args)})` — {verb.upper()} {path}" + (
        f" — {summary}" if summary else ""
    )

HEADER = '''"""Generated BoondManager API surface — DO NOT EDIT.

Regenerate with scripts/fetch_spec.py + scripts/generate_api.py.

One namespace per API resource, one method per endpoint+verb, covering the
whole BoondManager API v{version} ({n_methods} endpoints). Every call goes through
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
'''

API_CLASS = '''

class BoondManagerAPI:
    """Namespaced access to every endpoint of the BoondManager API.

    Usage::

        doc = await client.api.times_reports.get("1652")
        doc = await client.api.projects.search(params={"keywords": "AZTech"})
    """

    def __init__(self, client) -> None:
{assignments}
'''


def path_params(path: str) -> list[str]:
    return [snake(m) for m in re.findall(r"\{(\w+)\}", path)]


def fstring_path(path: str) -> str:
    concrete = re.sub(r"\{(\w+)\}", lambda m: "{" + snake(m.group(1)) + "}", path)
    return ('f"' if "{" in concrete else '"') + concrete + '"'


def preferred_name(verb: str, remainder: list[str]) -> str:
    """Method name inside a group, from the path segments after the group."""
    parts: list[str] = []
    for i, seg in enumerate(remainder):
        if seg.startswith("{"):
            if i > 0:
                parts.append("by_" + snake(seg[1:-1]))
        else:
            parts.append(snake(seg))
    stem = "_".join(parts)

    if not remainder:
        return {"get": "search", "post": "create", "put": "update_many", "delete": "delete_many"}[verb]
    if not stem:  # canonical /{id}
        return {"get": "get", "put": "update", "delete": "delete", "post": "create"}[verb]
    if verb == "put":
        return "update_" + stem
    if verb == "delete":
        return "delete_" + stem
    return stem  # get subresources and post actions read naturally bare


def describe_param(p: dict) -> str:
    bits = [p.get("type", "string")]
    if p.get("required"):
        bits.append("REQUIRED")
    if p.get("repeat"):
        bits.append("repeatable")
    if "enum" in p:
        bits.append("one of: " + " | ".join(str(v) for v in p["enum"]))
    if "default" in p:
        bits.append(f"default {p['default']}")
    line = f"{p['name']} ({', '.join(bits)})"
    if p.get("description"):
        line += f": {p['description']}"
    return line


def gen_method(verb: str, path: str, info: dict, name: str) -> str:
    params = path_params(path)
    args = ["self"] + params
    has_body = verb in ("post", "put")
    if has_body:
        # body is required when the spec declares a schema for it
        args.append("body: Any" if info["body_schema"] else "body: Any = None")
    sig = ", ".join(args) + ", *, params: dict | None = None, validate: bool = True"

    desc = (info.get("description") or "").strip()
    doc_lines = [f"{verb.upper()} {path}"]
    if desc and desc != doc_lines[0]:
        doc_lines += [""] + desc.splitlines()
    if info.get("params"):
        doc_lines += ["", "Query params:"]
        doc_lines += [f"  {describe_param(p)}" for p in info["params"]]
    if info["body_schema"]:
        doc_lines += ["", f"Request body schema: {info['body_schema']}"]
    doc = "\n        ".join(line.rstrip() for line in doc_lines)

    call_args = [f'"{verb.upper()}"', fstring_path(path)]
    if has_body:
        call_args.append("json=body")
    call_args += ["params=params", "validate=validate"]

    return (
        f"    async def {name}({sig}) -> Document:\n"
        f'        """{doc}\n        """\n'
        f"        return Document(await self._client.request({', '.join(call_args)}))\n"
    )


def class_name(group: str) -> str:
    return "".join(w.capitalize() for w in snake(group).split("_")) + "API"


def main() -> None:
    bundle = json.loads(
        gzip.decompress((ROOT / "boondmanager" / "_spec" / "spec.json.gz").read_bytes())
    )

    # group -> list of (verb, path, info)
    groups: dict[str, list[tuple[str, str, dict]]] = {}
    for endpoint in bundle["endpoints"]:
        group = endpoint["path"].strip("/").split("/")[0]
        for verb, info in endpoint["methods"].items():
            groups.setdefault(group, []).append((verb, endpoint["path"], info))

    n_methods = sum(len(v) for v in groups.values())
    out = HEADER.replace("{version}", str(bundle.get("api_version", "?"))).replace(
        "{n_methods}", str(n_methods)
    )
    index: dict[str, list[str]] = {}
    fallbacks: list[str] = []
    docs = [DOCS_HEADER]

    for group in sorted(groups):
        attr = snake(group)
        out += f"\n\nclass {class_name(group)}:\n"
        out += f'    """Endpoints under /{group}."""\n\n'
        out += "    def __init__(self, client) -> None:\n        self._client = client\n\n"
        docs.append(f"\n## client.api.{attr} (/{group})\n")
        taken: set[str] = set()
        for verb, path, info in sorted(groups[group], key=lambda t: (t[1], t[0])):
            remainder = path.strip("/").split("/")[1:]
            name = preferred_name(verb, remainder)
            if name in taken:
                name = f"{verb}_{name}"
                fallbacks.append(f"{verb.upper()} {path} -> {attr}.{name}")
            if name in taken:
                raise SystemExit(f"unresolvable name collision: {verb} {path}")
            taken.add(name)
            out += gen_method(verb, path, info, name) + "\n"
            docs.append(docs_line(name, verb, path, info))
            index.setdefault(attr, []).append(
                f'    ("{verb.upper()}", "{path}"): ("{attr}", "{name}"),'
            )

    assignments = "\n".join(
        f"        self.{snake(g)} = {class_name(g)}(client)" for g in sorted(groups)
    )
    out += API_CLASS.replace("{assignments}", assignments)

    out += "\n\nENDPOINT_INDEX: dict[tuple[str, str], tuple[str, str]] = {\n"
    for attr in sorted(index):
        out += "\n".join(index[attr]) + "\n"
    out += "}\n"

    OUT.write_text(out)
    DOCS_OUT.parent.mkdir(exist_ok=True)
    DOCS_OUT.write_text("\n".join(docs) + "\n")
    n = sum(len(v) for v in groups.values())
    print(f"wrote {OUT}: {len(groups)} groups, {n} methods, {len(OUT.read_text())//1024}KB")
    print(f"wrote {DOCS_OUT}: {len(DOCS_OUT.read_text())//1024}KB")
    if fallbacks:
        print("verb-prefixed fallback names:")
        for f in fallbacks:
            print("  ", f)


if __name__ == "__main__":
    main()
