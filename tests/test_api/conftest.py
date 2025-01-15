import pytest

from tests.clients.api.api_client import ApiClient


@pytest.fixture(scope="session")
def api_client(env_config):
    try:
        return ApiClient(host=env_config["HOST"])
    except Exception:
        pass
