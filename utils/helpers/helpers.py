import allure

from deepdiff import DeepDiff

from httpx import Response

from typing import Any

from src.album.schemas import AlbumResponse
from src.comments.schemas import CommentResponse

from tests.api.constants.assert_custom_message_constants import (
    HTTP_CODE_MSG_ERROR,
    RESPONSE_BODY_LIST_LENGTH_MSG_ERROR,
    RESPONSE_NOT_JSON_MSG_ERROR,
    RESPONSE_BODY_NOT_EMPTY_MSG_ERROR,
    RESPONSE_BODY_IS_EMPTY_MSG_ERROR,
)
from tests.api.constants.exclude_paths_constants import ALBUM_RESPONSE_EXCLUDE_PATHS, COMMENT_RESPONSE_EXCLUDE_PATHS
from tests.api.enums.http_code_enum import HttpCodeEnum

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


def assert_http_code_is_ok(actual_http_code: int) -> None:
    expected_http_code = HttpCodeEnum.OK.value
    with allure.step("Проверить, что http-код = 200"):
        assert actual_http_code == expected_http_code, HTTP_CODE_MSG_ERROR.format(actual_http_code, expected_http_code)


def assert_http_code_is_created(actual_http_code: int) -> None:
    expected_http_code = HttpCodeEnum.CREATED.value
    with allure.step("Проверить, что http-код = 201"):
        assert actual_http_code == expected_http_code, HTTP_CODE_MSG_ERROR.format(actual_http_code, expected_http_code)


def assert_http_code_is_forbidden(actual_http_code: int) -> None:
    expected_http_code = HttpCodeEnum.FORBIDDEN.value
    with allure.step("Проверить, что http-код = 403"):
        assert actual_http_code == expected_http_code, HTTP_CODE_MSG_ERROR.format(actual_http_code, expected_http_code)


def assert_http_code_is_not_found(actual_http_code: int) -> None:
    expected_http_code = HttpCodeEnum.NOT_FOUND.value
    with allure.step("Проверить, что http-код = 404"):
        assert actual_http_code == expected_http_code, HTTP_CODE_MSG_ERROR.format(actual_http_code, expected_http_code)


def assert_http_code_is_internal_server_error(actual_http_code: int) -> None:
    expected_http_code = HttpCodeEnum.INTERNAL_SERVER_ERROR.value
    with allure.step("Проверить, что http-код = 500"):
        assert actual_http_code == expected_http_code, HTTP_CODE_MSG_ERROR.format(actual_http_code, expected_http_code)


def assert_response_body_is_empty(response: Response) -> None:
    try:
        response_body = response.json()
        with allure.step("Проверить, что тело ответа отсутствует"):
            assert not response_body, RESPONSE_BODY_NOT_EMPTY_MSG_ERROR
    except ValueError:
        assert False, RESPONSE_NOT_JSON_MSG_ERROR


def assert_response_body_not_empty(response: Response) -> None:
    try:
        response_body = response.json()
        with allure.step("Проверить, что тело ответа не пустое"):
            assert response_body, RESPONSE_BODY_IS_EMPTY_MSG_ERROR
    except ValueError:
        assert False, RESPONSE_NOT_JSON_MSG_ERROR


def assert_response_body_list_length(actual_list_length: int, expected_list_length: int) -> None:
    with allure.step("Проверить кол-во элементов в ответе"):
        assert actual_list_length == expected_list_length, RESPONSE_BODY_LIST_LENGTH_MSG_ERROR.format(
            actual_list_length, expected_list_length
        )


def assert_get_albums_list_is_ok(response: Response, expected_response_body_length: int) -> None:
    http_code = response.status_code
    assert_http_code_is_ok(http_code)

    assert_response_body_not_empty(response)

    response_body = response.json()
    with allure.step("Проверить структуру данных ответа"):
        assert AlbumResponse(**response_body[0])

    response_body_length = len(response_body)
    assert_response_body_list_length(response_body_length, expected_response_body_length)


def assert_get_album_by_id_is_ok(response: Response) -> None:
    http_code = response.status_code
    assert_http_code_is_ok(http_code)

    assert_response_body_not_empty(response)

    response_body = response.json()
    with allure.step("Проверить структуру данных ответа"):
        assert AlbumResponse(**response_body)


def assert_album_is_created(response: Response, album: dict[str, Any]) -> None:
    http_code = response.status_code
    assert_http_code_is_created(http_code)

    assert_response_body_not_empty(response)

    response_body = response.json()
    with allure.step("Проверить структуру данных ответа"):
        assert AlbumResponse(**response_body)
    with allure.step("Сравнить данные из тела ответа и из тела запроса"):
        assert is_eql(response_body, album, ALBUM_RESPONSE_EXCLUDE_PATHS)


def assert_album_is_updated(response: Response, album: dict[str, Any]) -> None:
    http_code = response.status_code
    assert_http_code_is_ok(http_code)

    assert_response_body_not_empty(response)

    response_body = response.json()
    with allure.step("Проверить структуру данных ответа"):
        assert AlbumResponse(**response_body)
    with allure.step("Сравнить данные из тела ответа и из тела запроса"):
        assert is_eql(response_body, album, ALBUM_RESPONSE_EXCLUDE_PATHS)


def assert_album_is_deleted(response: Response) -> None:
    http_code = response.status_code
    assert_http_code_is_ok(http_code)

    assert_response_body_is_empty(response)


def assert_get_comments_list_is_ok(response: Response, expected_response_body_length: int) -> None:
    http_code = response.status_code
    assert_http_code_is_ok(http_code)

    assert_response_body_not_empty(response)

    response_body = response.json()
    with allure.step("Проверить структуру данных"):
        assert CommentResponse(**response_body[0])

    response_body_length = len(response_body)
    assert_response_body_list_length(response_body_length, expected_response_body_length)


def assert_get_comment_by_id_is_ok(response: Response) -> None:
    http_code = response.status_code
    assert_http_code_is_ok(http_code)

    assert_response_body_not_empty(response)

    response_body = response.json()
    with allure.step("Проверить структуру данных ответа"):
        assert CommentResponse(**response_body)


def assert_comment_is_created(response: Response, comment: dict[str, Any]) -> None:
    http_code = response.status_code
    assert_http_code_is_created(http_code)

    assert_response_body_not_empty(response)

    response_body = response.json()
    with allure.step("Проверить структуру данных ответа"):
        assert CommentResponse(**response_body)
    with allure.step("Сравнить данные из тела ответа и из тела запроса"):
        assert is_eql(response_body, comment, COMMENT_RESPONSE_EXCLUDE_PATHS)


def assert_comment_is_updated(response: Response, comment: dict[str, Any]) -> None:
    http_code = response.status_code
    assert_http_code_is_ok(http_code)

    assert_response_body_not_empty(response)

    response_body = response.json()
    with allure.step("Проверить структуру данных ответа"):
        assert CommentResponse(**response_body)
    with allure.step("Сравнить данные из тела ответа и из тела запроса"):
        assert is_eql(response_body, comment, COMMENT_RESPONSE_EXCLUDE_PATHS)


def assert_comment_is_deleted(response: Response) -> None:
    http_code = response.status_code
    assert_http_code_is_ok(http_code)

    assert_response_body_is_empty(response)
