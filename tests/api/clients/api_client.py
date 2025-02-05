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
    RESPONSE_INFO,
)
from utils.logger.logger import file_logger


log = file_logger(__name__)


class ApiClient:
    def __init__(self, host: str):
        self.host = host

    def get_resources(
        self, path: str, query_params: dict[str, Any] | None = None, headers: dict[str, Any] | None = None
    ) -> Response:
        log.info(GET_REQUEST_START, path)
        log.debug(GET_REQUEST_INFO, query_params, headers)

        try:
            response = get(url=f"{self.host}/{path}", params=query_params, headers=headers)

            log.info(GET_REQUEST_END, path, response.status_code)
            return response
        except Exception as e:
            log.error(GET_REQUEST_FAILED, path, e, exc_info=True)

    def get_resource_by_id(
        self,
        path: str,
        resource_id: int,
        query_params: dict[str, Any] | None = None,
        headers: dict[str, Any] | None = None,
    ) -> Response:
        log.info(GET_BY_ID_REQUEST_START, path, resource_id)
        log.debug(GET_BY_ID_REQUEST_INFO, query_params, headers)

        try:
            response = get(url=f"{self.host}/{path}/{resource_id}", params=query_params, headers=headers)

            log.info(GET_BY_ID_REQUEST_END, path, resource_id, response.status_code)
            log.debug(RESPONSE_INFO, response.json())

            return response
        except Exception as e:
            log.error(GET_BY_ID_REQUEST_FAILED, path, resource_id, e, exc_info=True)

    def create_resource(self, path: str, data: dict[str, Any], headers: dict[str, Any] | None = None) -> Response:
        log.info(POST_REQUEST_START, path)
        log.debug(POST_REQUEST_INFO, headers, data)

        try:
            response = post(url=f"{self.host}/{path}", json=data, headers=headers)

            log.info(POST_REQUEST_END, path, response.status_code)
            log.debug(RESPONSE_INFO, response.json())

            return response
        except Exception as e:
            log.error(POST_REQUEST_FAILED, path, e, exc_info=True)

    def update_resource_by_id(
        self, path: str, resources_id: int, data: dict[str, Any], headers: dict[str, Any] | None = None
    ) -> Response:
        log.info(PUT_REQUEST_START, path, resources_id)
        log.debug(PUT_REQUEST_INFO, headers, data)

        try:
            response = put(url=f"{self.host}/{path}/{resources_id}", json=data, headers=headers)

            log.info(PUT_REQUEST_END, path, resources_id, response.status_code)
            log.debug(RESPONSE_INFO, response.json())

            return response
        except Exception as e:
            log.error(PUT_REQUEST_FAILED, path, resources_id, e, exc_info=True)

    def delete_resource_by_id(self, path: str, resources_id: int, headers: dict[str, Any] | None = None) -> Response:
        log.info(DELETE_REQUEST_START, path, resources_id)
        log.debug(DELETE_REQUEST_INFO, headers)

        try:
            response = delete(url=f"{self.host}/{path}/{resources_id}", headers=headers)

            log.info(DELETE_REQUEST_END, path, resources_id, response.status_code)
            log.debug(RESPONSE_INFO, response.json())

            return response
        except Exception as e:
            log.error(DELETE_REQUEST_FAILED, path, resources_id, e, exc_info=True)
