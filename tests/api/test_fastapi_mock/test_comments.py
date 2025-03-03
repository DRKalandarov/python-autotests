import allure
import pytest
import responses
import requests

from typing import Any

from utils.helpers import assert_http_code_is_403, assert_http_code_is_500


@allure.epic("Сущность comments")
class TestComments:
    base_url = "http://localhost:8000/comments"

    @allure.feature("Мок создания сущности")
    @responses.activate
    @pytest.mark.test_case_id("UT-T301")
    def test_create_comment(self, mock_server, comment: dict[str, Any]) -> None:
        response = requests.post(url=f"{self.base_url}/", json=comment)

        http_code = response.status_code
        assert_http_code_is_403(http_code)

    @allure.feature("Мок удаления сущности по id")
    @responses.activate
    @pytest.mark.test_case_id("UT-T302")
    def test_delete_comment_by_id(self, mock_server) -> None:
        resource_id = 1
        response = requests.delete(f"{self.base_url}/{resource_id}")

        http_code = response.status_code
        assert_http_code_is_500(http_code)
