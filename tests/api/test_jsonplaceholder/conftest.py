import pytest

from src.album.schemas import AlbumRequest
from src.comments.schemas import CommentRequest

from tests.api.clients.api_client import ApiClient
from tests.api.generators.random_data_generator import get_random_str, get_random_int, get_random_email_str

from utils.logger.logger import file_logger


log = file_logger(__name__)


@pytest.fixture(scope="session")
def api_client(env_config):
    try:
        return ApiClient(host=env_config["JSONPLACEHOLDER_HOST"])
    except Exception as e:
        log.error(e, exc_info=True)


@pytest.fixture(scope="function")
def comment():
    try:
        comment = CommentRequest(
            post_id=get_random_int(),
            name=get_random_str(10),
            email=get_random_email_str(),
            body=get_random_str(30),
        )
        return comment.model_dump(by_alias=True)
    except Exception as e:
        log.error(e, exc_info=True)


@pytest.fixture(scope="function")
def album():
    try:
        album = AlbumRequest(
            user_id=get_random_int(),
            title=get_random_str(10),
        )
        return album.model_dump(by_alias=True)
    except Exception as e:
        log.error(e, exc_info=True)
