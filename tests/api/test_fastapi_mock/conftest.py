import allure
import pytest
import responses

from src.album.schemas import AlbumRequest
from src.comments.schemas import CommentRequest

from tests.api.generators.random_data_generator import get_random_str, get_random_int, get_random_email_str

from utils.logger.logger import file_logger


log = file_logger(__name__)


@allure.title("Инициализация моков")
@pytest.fixture(scope="function")
def mock_server(env_config):
    host = env_config["LOCALHOST"]

    responses.add(
        method=responses.GET,
        url=f"{host}/albums/",
        status=404,
    )
    responses.add(
        method=responses.POST,
        url=f"{host}/comments/",
        status=403,
    )
    responses.add(
        method=responses.DELETE,
        url=f"{host}/comments/1",
        status=500,
    )


@allure.title("Инициализация тестовых данных comment")
@pytest.fixture(scope="function")
def comment():
    try:
        comment = CommentRequest(
            post_id=get_random_int(),
            name=get_random_str(),
            email=get_random_email_str(),
            body=get_random_str(30),
        )
        return comment.model_dump(by_alias=True)
    except Exception as e:
        log.error(e, exc_info=True)


@allure.title("Инициализация тестовых данных album")
@pytest.fixture(scope="function")
def album():
    try:
        album = AlbumRequest(
            user_id=get_random_int(),
            title=get_random_str(),
        )
        return album.model_dump(by_alias=True)
    except Exception as e:
        log.error(e, exc_info=True)
