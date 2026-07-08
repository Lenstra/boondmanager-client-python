"""Light JSON:API wrappers for BoondManager responses.

The API returns JSON:API-ish documents::

    {"data": {...}, "included": [...], "meta": {...}}

``Document`` and ``Entity`` make them pleasant to navigate without hiding the
underlying dicts — both stay dict-compatible (``doc["data"]``, ``entity.raw``)
so nothing breaks when you need the raw payload.

Example::

    doc = await client.api.times_reports.get("1652")
    report = doc.one
    report["term"]                      # attribute access -> "2026-06"
    for project in doc.included("project"):
        deliveries = doc.related(project, "deliveries")
"""

from __future__ import annotations

from typing import Any, Iterator


class Entity:
    """One JSON:API resource object: {"id", "type", "attributes", "relationships"}."""

    __slots__ = ("raw",)

    def __init__(self, raw: dict) -> None:
        self.raw = raw

    @property
    def id(self) -> str:
        return str(self.raw.get("id", ""))

    @property
    def type(self) -> str:
        return self.raw.get("type", "")

    @property
    def attributes(self) -> dict:
        return self.raw.get("attributes") or {}

    @property
    def relationships(self) -> dict:
        return self.raw.get("relationships") or {}

    def __getitem__(self, key: str) -> Any:
        """Attribute access: entity["term"] -> attributes["term"]."""
        return self.attributes[key]

    def get(self, key: str, default: Any = None) -> Any:
        return self.attributes.get(key, default)

    def __contains__(self, key: str) -> bool:
        return key in self.attributes

    def rel(self, name: str) -> list[dict]:
        """Relationship refs as a list of {"id", "type"} dicts (possibly empty).

        Normalizes JSON:API's to-one (dict or null) and to-many (list) forms.
        """
        data = (self.relationships.get(name) or {}).get("data")
        if data is None:
            return []
        return data if isinstance(data, list) else [data]

    def __repr__(self) -> str:
        return f"<Entity {self.type}:{self.id}>"


class Document:
    """A full JSON:API response with helpers to navigate ``included``."""

    __slots__ = ("raw", "_index")

    def __init__(self, raw: dict) -> None:
        self.raw = raw
        self._index: dict[tuple[str, str], Entity] | None = None

    # -- dict compatibility -------------------------------------------------

    def __getitem__(self, key: str) -> Any:
        return self.raw[key]

    def get(self, key: str, default: Any = None) -> Any:
        return self.raw.get(key, default)

    def __contains__(self, key: str) -> bool:
        return key in self.raw

    # -- data ----------------------------------------------------------------

    @property
    def meta(self) -> dict:
        return self.raw.get("meta") or {}

    @property
    def one(self) -> Entity:
        """The single resource in ``data`` (profile/create/update responses)."""
        data = self.raw.get("data")
        if not isinstance(data, dict):
            raise ValueError(f"document data is not a single resource: {type(data)}")
        return Entity(data)

    @property
    def many(self) -> list[Entity]:
        """The resources in ``data`` normalized to a list (search responses)."""
        data = self.raw.get("data")
        if data is None:
            return []
        if isinstance(data, dict):
            return [Entity(data)]
        return [Entity(d) for d in data]

    def __iter__(self) -> Iterator[Entity]:
        return iter(self.many)

    def __len__(self) -> int:
        return len(self.many)

    # -- included ------------------------------------------------------------

    def included(self, resource_type: str | None = None) -> list[Entity]:
        items = [Entity(i) for i in self.raw.get("included") or []]
        return [i for i in items if i.type == resource_type] if resource_type else items

    def find(self, type: str, id: str | int) -> Entity | None:
        """Look up one included (or primary) entity by type and id."""
        if self._index is None:
            self._index = {(e.type, e.id): e for e in [*self.many, *self.included()]}
        return self._index.get((type, str(id)))

    def related(self, entity: Entity, relationship: str) -> list[Entity]:
        """Resolve a relationship of ``entity`` against ``included``.

        Refs that are not present in ``included`` are returned as bare
        Entities (id/type only) rather than dropped.
        """
        out = []
        for ref in entity.rel(relationship):
            resolved = self.find(ref.get("type", ""), ref.get("id", ""))
            out.append(resolved if resolved is not None else Entity(ref))
        return out

    def __repr__(self) -> str:
        data = self.raw.get("data")
        shape = f"list[{len(data)}]" if isinstance(data, list) else (data or {}).get("type", "empty")
        return f"<Document {shape}, included={len(self.raw.get('included') or [])}>"
