import allure
import pytest
import responses
import requests

from src.comments.schemas import CommentRequest

from utils.helpers.helpers import assert_http_code_is_forbidden, assert_http_code_is_internal_server_error


@allure.epic("Сущность comments")
class TestComments:
    base_url = "http://localhost:8000"

    @allure.feature("Мок создания сущности")
    @responses.activate
    @pytest.mark.test_case_id("UT-T301")
    def test_create_comment(self, mock_server, comment: CommentRequest) -> None:
        response = requests.post(url=f"{self.base_url}/comments/", data=comment)
        http_code = response.status_code
        assert_http_code_is_forbidden(http_code)

    @allure.feature("Мок удаления сущности по id")
    @responses.activate
    @pytest.mark.test_case_id("UT-T302")
    def test_delete_comment_by_id(self, mock_server) -> None:
        response = requests.delete(f"{self.base_url}/comments/1")
        http_code = response.status_code
        assert_http_code_is_internal_server_error(http_code)
