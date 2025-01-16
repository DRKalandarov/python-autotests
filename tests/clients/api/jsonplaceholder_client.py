from httpx import get, post, put, delete

from utils.logger.logger import file_logger


log = file_logger(__name__)


class JsonplaceholderClient:
    def __init__(self, host):
        self.host = host

    def get_resources(self, path, query_params=None, headers=None):
        log.info("Отправка запроса GET /%s", path)
        log.debug("request_params: query_params=%s, headers=%s", query_params, headers)

        try:
            response = get(url=f"{self.host}/{path}", params=query_params, headers=headers)
            log.info("Запрос GET /%s завершен успешно: http_code=%s", path, response.status_code)

            return response
        except Exception as e:
            log.error("При выполнении запроса GET /%s возникла ошибка: exception=%s", path, e)

    def get_resource_by_id(self, path, id, query_params=None, headers=None):
        log.info("Отправка запроса GET /%s/%s", path, id)
        log.debug("request_params: query_params=%s, headers=%s", query_params, headers)

        try:
            response = get(url=f"{self.host}/{path}/{id}", params=query_params, headers=headers)
            log.info("Запрос GET /%s/%s завершен успешно: http_code=%s", path, id, response.status_code)
            log.debug("response_data=%s", response.json())

            return response
        except Exception as e:
            log.error("При выполнении запроса GET /%s/%s возникла ошибка: exception=%s", path, id, e)

    def create_resource(self, path, data, headers=None):
        log.info("Отправка запроса POST /%s", path)
        log.debug("request_params: headers=%s, data=%s", headers, data)

        try:
            response = post(url=f"{self.host}/{path}", json=data, headers=headers)
            log.info("Запрос POST /%s завершен успешно: http_code=%s", path, response.status_code)
            log.debug("response_data=%s", response.json())

            return response
        except Exception as e:
            log.error("При выполнении запроса POST /%s возникла ошибка: exception=%s", path, e)

    def update_resource_by_id(self, path, id, data, headers=None):
        log.info("Отправка запроса PUT /%s/%s", path, id)
        log.debug("request_params: headers=%s, data=%s", headers, data)

        try:
            response = put(url=f"{self.host}/{path}/{id}", json=data, headers=headers)
            log.info("Запрос PUT /%s/%s завершен успешно: http_code=%s", path, id, response.status_code)
            log.debug("response_data=%s", response.json())

            return response
        except Exception as e:
            log.error("При выполнении запроса PUT /%s/%s возникла ошибка: exception=%s", path, id, e)

    def delete_resource_by_id(self, path, id, headers=None):
        log.info("Отправка запроса DELETE /%s/%s", path, id)
        log.debug("request_params: headers=%s", headers)

        try:
            response = delete(url=f"{self.host}/{path}/{id}", headers=headers)
            log.info("Запрос DELETE /%s/%s завершен успешно: http_code=%s", path, id, response.status_code)
            log.debug("response_data=%s", response.json())

            return response
        except Exception as e:
            log.error("При выполнении запроса DELETE /%s/%s возникла ошибка: exception=%s", path, id, e)
