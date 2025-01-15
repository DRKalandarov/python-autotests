import pytest

from dotenv import dotenv_values


@pytest.fixture(scope="session")
def env_config():
    env_path = ".env.local"
    try:
        return dotenv_values(env_path)
    except Exception:
        pass
