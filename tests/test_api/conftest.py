import pytest

from tests.clients.api.api_client import ApiClient

from utils.logger.logger import file_logger


log = file_logger(__name__)


@pytest.fixture(scope="session")
def api_client(env_config):
    try:
        return ApiClient(host=env_config["HOST"])
    except Exception as e:
        log.error(e)
