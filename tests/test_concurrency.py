"""Tests for BoondManagerClient's request concurrency cap (no network)."""

import asyncio

from boondmanager import BoondManagerClient


class _FakeResponse:
    def __init__(self, data: dict) -> None:
        self._data = data
        self.content = b"1"

    def raise_for_status(self) -> None:
        pass

    def json(self) -> dict:
        return self._data


def _install_tracking_transport(client: BoondManagerClient) -> dict:
    """Replace the underlying httpx call with one that records peak concurrency."""
    state = {"active": 0, "peak": 0}

    async def fake_http_request(method, url, headers=None, **kwargs):
        state["active"] += 1
        state["peak"] = max(state["peak"], state["active"])
        await asyncio.sleep(0.01)
        state["active"] -= 1
        return _FakeResponse({"data": {"id": "1", "type": "x", "attributes": {}}})

    client._http.request = fake_http_request
    return state


def _run_n_requests(client: BoondManagerClient, n: int) -> None:
    async def run():
        await asyncio.gather(*(client.request("GET", f"/x/{i}") for i in range(n)))

    asyncio.run(run())


def test_default_caps_concurrency_at_five():
    client = BoondManagerClient(client_token="t", client_key="k")
    state = _install_tracking_transport(client)
    _run_n_requests(client, 10)
    assert state["peak"] == 5


def test_max_concurrent_requests_is_configurable():
    client = BoondManagerClient(client_token="t", client_key="k", max_concurrent_requests=3)
    state = _install_tracking_transport(client)
    _run_n_requests(client, 10)
    assert state["peak"] == 3


def test_max_concurrent_requests_none_disables_cap():
    client = BoondManagerClient(client_token="t", client_key="k", max_concurrent_requests=None)
    state = _install_tracking_transport(client)
    _run_n_requests(client, 10)
    assert state["peak"] == 10


def test_explicit_semaphore_overrides_max_concurrent_requests():
    client = BoondManagerClient(
        client_token="t",
        client_key="k",
        max_concurrent_requests=5,
        semaphore=asyncio.Semaphore(2),
    )
    state = _install_tracking_transport(client)
    _run_n_requests(client, 10)
    assert state["peak"] == 2


def test_search_resources_by_email_respects_concurrency_cap():
    # The manager-resolution fan-out in search_resources_by_email must not
    # bypass the client's own concurrency cap.
    client = BoondManagerClient(client_token="t", client_key="k", max_concurrent_requests=2)
    state = _install_tracking_transport(client)

    async def run():
        page = {
            "data": [
                {
                    "id": str(i),
                    "type": "resource",
                    "attributes": {},
                    "relationships": {
                        "mainManager": {"data": {"id": f"m{i}", "type": "resource"}}
                    },
                }
                for i in range(6)
            ]
        }

        async def fake_http_request(method, url, headers=None, **kwargs):
            state["active"] += 1
            state["peak"] = max(state["peak"], state["active"])
            await asyncio.sleep(0.01)
            state["active"] -= 1
            path = url.removeprefix(client._base_url)
            if path == "/resources":
                return _FakeResponse(page)
            manager_id = path.split("/")[2]  # /resources/{id}[/information]
            return _FakeResponse(
                {"data": {"id": manager_id, "type": "resource", "attributes": {}}}
            )

        client._http.request = fake_http_request
        await client.search_resources_by_email("a@x.fr")

    asyncio.run(run())
    assert state["peak"] <= 2
