import allure

from deepdiff import DeepDiff

from httpx import Response

from typing import Any

from src.album.schemas import AlbumResponse
from src.comments.schemas import CommentResponse

from tests.api.enums.http_code_enum import HttpCodeEnum
from tests.api.constants.exclude_paths_constants import ALBUM_RESPONSE_EXCLUDE_PATHS, COMMENT_RESPONSE_EXCLUDE_PATHS

from utils.logger.logger import file_logger


log = file_logger(__name__)


def is_eql(actual: dict[str, Any], expected: dict[str, Any], exclude_paths: list[str] | None = None) -> bool:
    diff = DeepDiff(t1=actual, t2=expected, exclude_paths=exclude_paths)

    log.info("Начало сравнения фактического словаря и ожидаемого")
    if not diff:
        log.info("Словари одинаковые")
        return True
    else:
        log.error("Словари разные: %s", diff)
        return False


def assert_get_albums_list_is_ok(response: Response, expected_response_data_len: int) -> None:
    with allure.step("Проверить http-код ответа"):
        assert response.status_code == HttpCodeEnum.OK.value

    response_data = response.json()
    with allure.step("Проверить структуру данных ответа"):
        assert AlbumResponse(**response_data[0])
    with allure.step("Проверить кол-во элементов в ответе"):
        assert len(response_data) == expected_response_data_len


def assert_get_album_by_id_is_ok(response: Response) -> None:
    with allure.step("Проверить http-код ответа"):
        assert response.status_code == HttpCodeEnum.OK.value

    response_data = response.json()
    with allure.step("Проверить структуру данных ответа"):
        assert AlbumResponse(**response_data)


def assert_album_is_created(response: Response, album: dict[str, Any]) -> None:
    with allure.step("Проверить http-код ответа"):
        assert response.status_code == HttpCodeEnum.CREATED.value

    response_data = response.json()
    with allure.step("Проверить структуру данных ответа"):
        assert AlbumResponse(**response_data)
    with allure.step("Сравнить данные из тела ответа и из тела запроса"):
        assert is_eql(response_data, album, ALBUM_RESPONSE_EXCLUDE_PATHS)


def assert_album_is_updated(response: Response, album: dict[str, Any]) -> None:
    with allure.step("Проверить http-код ответа"):
        assert response.status_code == HttpCodeEnum.OK.value

    response_data = response.json()
    with allure.step("Проверить структуру данных ответа"):
        assert AlbumResponse(**response_data)
    with allure.step("Сравнить данные из тела ответа и из тела запроса"):
        assert is_eql(response_data, album, ALBUM_RESPONSE_EXCLUDE_PATHS)


def assert_album_is_deleted(response: Response) -> None:
    with allure.step("Проверить http-код ответа"):
        assert response.status_code == HttpCodeEnum.OK.value

    response_data = response.json()
    with allure.step("Проверить, что тело ответа отсутствует"):
        assert not response_data


def assert_get_comments_list_is_ok(response: Response, expected_response_data_len: int) -> None:
    with allure.step("Проверить http-код ответа"):
        assert response.status_code == HttpCodeEnum.OK.value

    response_data = response.json()
    with allure.step("Проверить структуру данных"):
        assert CommentResponse(**response_data[0])
    with allure.step("Проверить кол-во элементов в ответе"):
        assert len(response_data) == expected_response_data_len


def assert_get_comment_by_id_is_ok(response: Response) -> None:
    with allure.step("Проверить http-код ответа"):
        assert response.status_code == HttpCodeEnum.OK.value

    response_data = response.json()
    with allure.step("Проверить структуру данных ответа"):
        assert CommentResponse(**response_data)


def assert_comment_is_created(response: Response, comment: dict[str, Any]) -> None:
    with allure.step("Проверить http-код ответа"):
        assert response.status_code == HttpCodeEnum.CREATED.value

    response_data = response.json()
    with allure.step("Проверить структуру данных ответа"):
        assert CommentResponse(**response_data)
    with allure.step("Сравнить данные из тела ответа и из тела запроса"):
        assert is_eql(response_data, comment, COMMENT_RESPONSE_EXCLUDE_PATHS)


def assert_comment_is_updated(response: Response, comment: dict[str, Any]) -> None:
    with allure.step("Проверить http-код ответа"):
        assert response.status_code == HttpCodeEnum.OK.value

    response_data = response.json()
    with allure.step("Проверить структуру данных ответа"):
        assert CommentResponse(**response_data)
    with allure.step("Сравнить данные из тела ответа и из тела запроса"):
        assert is_eql(response_data, comment, COMMENT_RESPONSE_EXCLUDE_PATHS)


def assert_comment_is_deleted(response: Response) -> None:
    with allure.step("Проверить http-код ответа"):
        assert response.status_code == HttpCodeEnum.OK.value

    response_data = response.json()
    with allure.step("Проверить, что тело ответа отсутствует"):
        assert not response_data
