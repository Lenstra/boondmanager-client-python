"""Fetch the BoondManager RAML spec and vendor it into the package.

Downloads the public RAML build from doc.boondmanager.com, expands the full
endpoint tree, and writes a single gzipped bundle:

- boondmanager/_spec/spec.json.gz — {"endpoints": [...], "schemas": {name: schema}}

endpoints[*]: path, methods {get/post/put/delete: {description, body_schema,
params}} where params documents the query parameters (own + inherited from
RAML traits such as pagination). schemas: request-body JSON schemas
(Body-put/Body-post) used for pre-send validation.

Run from the package root:

    uv run --with pyyaml python scripts/fetch_spec.py

Then regenerate the API surface with scripts/generate_api.py.
"""

from __future__ import annotations

import gzip
import json
import pathlib
import posixpath
import re
from concurrent.futures import ThreadPoolExecutor

import httpx
import yaml

BASE = "https://doc.boondmanager.com/api-externe/raml-build/"
ROOT = pathlib.Path(__file__).resolve().parent.parent
SPEC_DIR = ROOT / "boondmanager" / "_spec"

_http = httpx.Client(timeout=30.0)

METHODS = ("get", "post", "put", "delete")

# Schemas referenced by resource files but absent from the root `schemas:`
# mapping (spec bug on BoondManager's side). The ones whose file we could
# locate by convention are listed here; the rest have no published schema
# and their endpoints are callable without pre-send validation.
EXTRA_SCHEMA_FILES = {
    "validationsBody-put": "schemas/validations/bodyPut.json",
}

# resourceType -> {method: body schema suffix} (from resourceTypes/*.raml).
# Only write methods carry request bodies.
RESOURCE_TYPE_BODIES = {
    "profile": {"put": "{type}Body-put"},
    "search": {"post": "{type}Body-post", "put": "{type}Body-put"},
    "rights": {},
    "download": {},
    "base": {},
}


class Include:
    def __init__(self, target: str) -> None:
        self.target = target

    def __repr__(self) -> str:
        return f"Include({self.target})"


def _include_constructor(loader, node):
    return Include(loader.construct_scalar(node))


yaml.SafeLoader.add_constructor("!include", _include_constructor)


def fetch(rel_path: str) -> str:
    url = BASE + rel_path
    resp = _http.get(url)
    resp.raise_for_status()
    return resp.text


def parse_raml(rel_path: str) -> dict:
    return yaml.safe_load(fetch(rel_path)) or {}


def _resource_type(node: dict) -> tuple[str, str | None]:
    """Return (resourceType name, type parameter) for a resource node."""
    t = node.get("type")
    if isinstance(t, str):
        return t, None
    if isinstance(t, dict):
        (rt_name, params), = t.items()
        param = (params or {}).get("type") if isinstance(params, dict) else None
        return rt_name, param
    return "base", None


_TRAITS: dict[str, dict] = {}  # trait name -> queryParameters, from traits/*.raml
_MD_LINK = re.compile(r"\[([^\]]*)\]\([^)]*\)")


def _clean_desc(text: str) -> str:
    """First meaningful line, markdown links unwrapped."""
    for line in (text or "").splitlines():
        line = _MD_LINK.sub(r"\1", line).strip().rstrip(":")
        if line:
            return line
    return ""


def _param_summary(name: str, definition: dict) -> dict:
    d = definition or {}
    out: dict = {"name": name, "type": d.get("type", "string")}
    if d.get("required"):
        out["required"] = True
    if d.get("repeat"):
        out["repeat"] = True
    if "enum" in d:
        out["enum"] = d["enum"]
    if "default" in d:
        out["default"] = d["default"]
    desc = _clean_desc(str(d.get("description", "")))
    if desc:
        out["description"] = desc
    return out


def _method_params(node: dict, method_node) -> list[dict]:
    """Query parameters for one method: its own + those of applied traits."""
    params: dict[str, dict] = {}

    def apply_traits(is_clause) -> None:
        for trait in is_clause or []:
            if isinstance(trait, dict):
                (trait_name, args), = trait.items()
            else:
                trait_name, args = trait, {}
            for pname, pdef in _TRAITS.get(trait_name, {}).items():
                pdef = dict(pdef or {})
                desc = str(pdef.get("description", ""))
                for k, v in (args or {}).items():
                    desc = desc.replace(f"<<{k}>>", str(v))
                pdef["description"] = desc
                params.setdefault(pname, pdef)

    own = method_node.get("queryParameters") if isinstance(method_node, dict) else None
    for pname, pdef in (own or {}).items():
        params[pname] = pdef or {}
    if isinstance(method_node, dict):
        apply_traits(method_node.get("is"))
    apply_traits(node.get("is"))

    # required params first, then endpoint-specific, then trait boilerplate
    summaries = [_param_summary(n, d) for n, d in params.items()]
    return sorted(summaries, key=lambda p: not p.get("required", False))


def _explicit_body_schema(method_node) -> str | None:
    """Schema declared inline on the method (overrides the resourceType default)."""
    if not isinstance(method_node, dict):
        return None
    body = method_node.get("body")
    if not isinstance(body, dict):
        return None
    app_json = body.get("application/json")
    if not isinstance(app_json, dict):
        return None
    schema = app_json.get("schema")
    return schema if isinstance(schema, str) else None


def _process_node(
    node: dict, url_path: str, base_dir: str, endpoints: list[dict]
) -> None:
    """Process an already-parsed RAML resource node and recurse into children."""
    rt_name, type_param = _resource_type(node)
    body_map = RESOURCE_TYPE_BODIES.get(rt_name, {})

    entry: dict = {"path": url_path, "methods": {}}
    for method in METHODS:
        if method not in node:
            continue
        method_node = node.get(method)
        schema = _explicit_body_schema(method_node)
        if schema is None and type_param:
            template = body_map.get(method)
            if template:
                schema = template.format(type=type_param)
        desc = ""
        if isinstance(method_node, dict):
            desc = (method_node.get("description") or "").strip()
        if not desc and isinstance(node.get("description"), str):
            desc = node["description"].strip()
        entry["methods"][method] = {
            "description": desc,
            "body_schema": schema,
            "params": _method_params(node, method_node),
        }
    if entry["methods"]:
        endpoints.append(entry)

    for key, value in node.items():
        if not (isinstance(key, str) and key.startswith("/")):
            continue
        child_path = url_path + key
        if isinstance(value, Include):
            walk_resource(
                posixpath.normpath(posixpath.join(base_dir, value.target)),
                child_path,
                endpoints,
            )
        elif isinstance(value, dict):
            _process_node(value, child_path, base_dir, endpoints)


def walk_resource(rel_path: str, url_path: str, endpoints: list[dict]) -> None:
    node = parse_raml(rel_path)
    _process_node(node, url_path, posixpath.dirname(rel_path), endpoints)


def main() -> None:
    root_text = fetch("api-externe.raml")
    root = yaml.safe_load(root_text)

    # name -> schema file path, from the root `schemas:` list
    schema_files: dict[str, str] = {}
    for item in root.get("schemas", []):
        for name, inc in item.items():
            if isinstance(inc, Include):
                schema_files[name] = inc.target
    schema_files.update(EXTRA_SCHEMA_FILES)

    # shared query-parameter traits (searchable, paginable, ...)
    for item in root.get("traits", []):
        for name, inc in item.items():
            if isinstance(inc, Include):
                _TRAITS[name] = parse_raml(inc.target).get("queryParameters") or {}
    print(f"loaded {len(_TRAITS)} traits")

    # top-level endpoints, in document order (yaml dict preserves it)
    endpoints: list[dict] = []
    top = [(k, v) for k, v in root.items() if isinstance(k, str) and k.startswith("/")]
    print(f"expanding {len(top)} top-level resources...")
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = [
            pool.submit(walk_resource, v.target, k, endpoints)
            for k, v in top
            if isinstance(v, Include)
        ]
        for f in futures:
            f.result()
    # inline top-level resources (defined as a dict directly in the root RAML)
    for k, v in top:
        if isinstance(v, dict):
            _process_node(v, k, "", endpoints)
    endpoints.sort(key=lambda e: e["path"])

    # download every referenced request-body schema
    needed = sorted(
        {
            m["body_schema"]
            for e in endpoints
            for m in e["methods"].values()
            if m["body_schema"]
        }
    )
    missing = [s for s in needed if s not in schema_files]
    if missing:
        print(f"WARNING: {len(missing)} schemas referenced but not in root mapping: {missing}")
    needed = [s for s in needed if s in schema_files]

    print(f"downloading {len(needed)} request-body schemas...")
    schemas: dict[str, dict] = {}

    def grab(name: str) -> None:
        schemas[name] = json.loads(fetch(schema_files[name]))

    with ThreadPoolExecutor(max_workers=8) as pool:
        for f in [pool.submit(grab, s) for s in needed]:
            f.result()

    bundle = {
        "source": BASE,
        "api_version": root.get("version"),
        "endpoints": endpoints,
        "schemas": schemas,
    }
    SPEC_DIR.mkdir(parents=True, exist_ok=True)
    raw = json.dumps(bundle, separators=(",", ":")).encode()
    # mtime=0 keeps the output byte-stable across regenerations
    with (SPEC_DIR / "spec.json.gz").open("wb") as fh:
        fh.write(gzip.compress(raw, mtime=0))
    n_methods = sum(len(e["methods"]) for e in endpoints)
    print(
        f"wrote {len(endpoints)} endpoints ({n_methods} methods), "
        f"{len(schemas)} schemas, {len(raw)//1024}KB raw"
    )


if __name__ == "__main__":
    main()
