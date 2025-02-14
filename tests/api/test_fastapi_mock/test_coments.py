import allure
import pytest
import responses
import requests

from src.comments.schemas import CommentRequest

from tests.api.enums.http_code_enum import HttpCodeEnum


@allure.epic("Сущность comments")
class TestComments:
    base_url = "http://localhost:8000"

    @allure.feature("Мок создания сущности")
    @responses.activate
    @pytest.mark.test_case_id("UT-T301")
    def test_create_comment(self, mock_server, comment: CommentRequest) -> None:
        response = requests.post(url=f"{self.base_url}/comments/", data=comment)
        assert response.status_code == HttpCodeEnum.FORBIDDEN.value

    @allure.feature("Мок удаления сущности по id")
    @responses.activate
    @pytest.mark.test_case_id("UT-T302")
    def test_delete_comment_by_id(self, mock_server) -> None:
        response = requests.delete(f"{self.base_url}/comments/1")
        assert response.status_code == HttpCodeEnum.INTERNAL_SERVER_ERROR.value
