import pytest

from dotenv import dotenv_values

from utils.logger.logger import file_logger


log = file_logger(__name__)


@pytest.fixture(scope="session")
def env_config():
    env_path = ".env.local"
    try:
        return dotenv_values(env_path)
    except Exception as e:
        log.error(e)
