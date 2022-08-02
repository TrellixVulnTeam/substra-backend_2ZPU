from typing import Any

from substrapp.clients import organization as organization_client


class Algo:
    def __init__(self, channel: str, algo_asset: dict[str, Any]):
        self._channel = channel
        self._algo = algo_asset

    @property
    def _owner(self) -> str:
        return self._algo["owner"]

    @property
    def _storage_address(self) -> str:
        return self._algo["algorithm"]["storage_address"]

    @property
    def checksum(self) -> str:
        return self._algo["algorithm"]["checksum"]

    @property
    def key(self) -> str:
        return self._algo["key"]

    @property
    def container_image_tag(self) -> str:
        return f"algo-{self.checksum[:16]}"

    @property
    def __dict__(self) -> dict[str, Any]:
        return self._algo

    @property
    def archive(self) -> bytes:
        return organization_client.get(self._channel, self._owner, self._storage_address, self.checksum)

    @property
    def inputs(self) -> dict[str, dict]:
        return self._algo["inputs"]

    @property
    def outputs(self) -> dict[str, dict]:
        return self._algo["outputs"]
