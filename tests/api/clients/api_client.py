from httpx import get, post, put, delete, Response

from typing import Any

from tests.api.constants.log_constants import (
    GET_REQUEST_START,
    GET_REQUEST_END,
    GET_REQUEST_FAILED,
    GET_REQUEST_INFO,
    GET_BY_ID_REQUEST_START,
    GET_BY_ID_REQUEST_END,
    GET_BY_ID_REQUEST_FAILED,
    GET_BY_ID_REQUEST_INFO,
    POST_REQUEST_START,
    POST_REQUEST_END,
    POST_REQUEST_FAILED,
    POST_REQUEST_INFO,
    PUT_REQUEST_START,
    PUT_REQUEST_END,
    PUT_REQUEST_FAILED,
    PUT_REQUEST_INFO,
    DELETE_REQUEST_START,
    DELETE_REQUEST_END,
    DELETE_REQUEST_FAILED,
    DELETE_REQUEST_INFO,
    RESPONSE_DATA,
)

from utils.logger.logger import file_logger


log = file_logger(__name__)


class ApiClient:
    def __init__(self, host: str):
        self.host = host

    def get_resources(self, path: str, headers: dict[str, Any] | None = None) -> Response:
        url = f"{self.host}/{path}"
        try:
            log.info(GET_REQUEST_START, path)
            log.debug(GET_REQUEST_INFO, headers)

            response = get(url=url, headers=headers)

            log.info(GET_REQUEST_END, path, response.status_code)

            return response
        except Exception as e:
            log.error(GET_REQUEST_FAILED, path, e, exc_info=True)

    def get_resource_by_id(self, path: str, resource_id: int, headers: dict[str, Any] | None = None) -> Response:
        url = f"{self.host}/{path}/{resource_id}"
        try:
            log.info(GET_BY_ID_REQUEST_START, path, resource_id)
            log.debug(GET_BY_ID_REQUEST_INFO, headers)

            response = get(url=url, headers=headers)

            log.info(GET_BY_ID_REQUEST_END, path, resource_id, response.status_code)
            self._log_response(response)

            return response
        except Exception as e:
            log.error(GET_BY_ID_REQUEST_FAILED, path, resource_id, e, exc_info=True)

    def create_resource(self, path: str, data: dict[str, Any], headers: dict[str, Any] | None = None) -> Response:
        url = f"{self.host}/{path}"
        try:
            log.info(POST_REQUEST_START, path)
            log.debug(POST_REQUEST_INFO, headers, data)

            response = post(url=url, json=data, headers=headers)

            log.info(POST_REQUEST_END, path, response.status_code)
            self._log_response(response)

            return response
        except Exception as e:
            log.error(POST_REQUEST_FAILED, path, e, exc_info=True)

    def update_resource_by_id(
        self, path: str, resource_id: int, data: dict[str, Any], headers: dict[str, Any] | None = None
    ) -> Response:
        url = f"{self.host}/{path}/{resource_id}"
        try:
            log.info(PUT_REQUEST_START, path, resource_id)
            log.debug(PUT_REQUEST_INFO, headers, data)

            response = put(url=url, json=data, headers=headers)

            log.info(PUT_REQUEST_END, path, resource_id, response.status_code)
            self._log_response(response)

            return response
        except Exception as e:
            log.error(PUT_REQUEST_FAILED, path, resource_id, e, exc_info=True)

    def delete_resource_by_id(self, path: str, resource_id: int, headers: dict[str, Any] | None = None) -> Response:
        url = f"{self.host}/{path}/{resource_id}"
        try:
            log.info(DELETE_REQUEST_START, path, resource_id)
            log.debug(DELETE_REQUEST_INFO, headers)

            response = delete(url=url, headers=headers)

            log.info(DELETE_REQUEST_END, path, resource_id, response.status_code)
            self._log_response(response)

            return response
        except Exception as e:
            log.error(DELETE_REQUEST_FAILED, path, resource_id, e, exc_info=True)

    def _log_response(self, response: Response) -> None:
        if response.is_success:
            log.debug(RESPONSE_DATA, response.json())
