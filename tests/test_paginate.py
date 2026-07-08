"""Tests for BoondManagerClient.paginate (no network)."""

import asyncio

from boondmanager import BoondManagerClient


def _page(ids) -> dict:
    return {"data": [{"id": str(i), "type": "resource", "attributes": {}} for i in ids]}


def make_client(pages: list[dict]) -> BoondManagerClient:
    client = BoondManagerClient(client_token="t", client_key="k")
    call_log: list[dict] = []
    page_iter = iter(pages)

    async def fake_request(method, endpoint, *, validate=True, params=None, **kwargs):
        call_log.append({"method": method, "endpoint": endpoint, "params": dict(params or {})})
        return next(page_iter)

    client.request = fake_request
    client._call_log = call_log
    return client


def collect(client, **kwargs) -> list:
    async def _run():
        return [page async for page in client.paginate("GET", "/resources", **kwargs)]
    return asyncio.run(_run())


def test_single_partial_page():
    client = make_client([_page([1, 2, 3])])
    pages = collect(client, page_size=30)
    assert len(pages) == 1
    assert [e.id for e in pages[0]] == ["1", "2", "3"]


def test_multiple_full_then_partial_page():
    client = make_client([_page(range(1, 6)), _page(range(6, 9))])
    pages = collect(client, page_size=5)
    assert len(pages) == 2
    assert len(pages[0]) == 5
    assert len(pages[1]) == 3


def test_stops_without_yielding_empty_sentinel_page():
    # When the last real page is exactly page_size, an extra empty page is
    # fetched as a sentinel. It must not be yielded.
    client = make_client([_page(range(1, 6)), _page(range(6, 11)), _page([])])
    pages = collect(client, page_size=5)
    assert len(pages) == 2
    assert len(client._call_log) == 3  # three fetches, two yields


def test_page_param_increments():
    client = make_client([_page(range(1, 6)), _page([])])
    collect(client, page_size=5)
    assert client._call_log[0]["params"]["page"] == 1
    assert client._call_log[1]["params"]["page"] == 2


def test_caller_params_are_forwarded_and_not_mutated():
    caller_params = {"keywords": "foo"}
    client = make_client([_page([1])])
    collect(client, params=caller_params, page_size=30)
    sent = client._call_log[0]["params"]
    assert sent["keywords"] == "foo"
    assert sent["page"] == 1
    assert sent["maxResults"] == 30
    # caller's dict must not be mutated
    assert caller_params == {"keywords": "foo"}


def test_page_size_passed_as_max_results():
    client = make_client([_page([1])])
    collect(client, page_size=10)
    assert client._call_log[0]["params"]["maxResults"] == 10
