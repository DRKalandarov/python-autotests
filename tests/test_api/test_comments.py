import pytest

from typing import Any

from schemas.api.comment.response.comment_response import CommentResponse

from tests.clients.api.api_client import ApiClient

from tests.enums.http_code_enum import HttpCodeEnum

from utils.compare.compare import is_eql


class TestComments:
    base_path = "comments"

    def test_get_comments_list(self, api_client: ApiClient) -> None:
        """
        Получение списка всех комментариев
        """
        expected_response_data_len = 500

        response = api_client.get_resources(path=self.base_path)
        response_data = response.json()

        assert response.status_code == HttpCodeEnum.OK.value
        assert CommentResponse(**response_data[0])
        assert len(response_data) == expected_response_data_len

    @pytest.mark.parametrize("post_id", [1, 10, 100])
    def test_get_comment_by_id(self, api_client: ApiClient, post_id: int) -> None:
        """
        Получение комментария по id
        """
        response = api_client.get_resource_by_id(path=self.base_path, id=post_id)
        response_data = response.json()

        assert response.status_code == HttpCodeEnum.OK.value
        assert CommentResponse(**response_data)

    def test_create_comment(self, api_client: ApiClient, comment: dict[str, Any]) -> None:
        """
        Создание комментария
        """
        response = api_client.create_resource(path=self.base_path, data=comment)
        response_data = response.json()

        assert response.status_code == HttpCodeEnum.CREATED.value
        assert CommentResponse(**response_data)

        comment["id"] = response_data["id"]
        assert is_eql(response_data, comment)

    def test_update_comment_by_id(self, api_client: ApiClient, comment: dict[str, Any]) -> None:
        """
        Обновление комментария по id
        """
        resource_id = 10

        response = api_client.update_resource_by_id(path=self.base_path, id=resource_id, data=comment)
        response_data = response.json()

        assert response.status_code == HttpCodeEnum.OK.value
        assert CommentResponse(**response_data)

        comment["id"] = resource_id
        assert is_eql(response_data, comment)

    def test_delete_comment_by_id(self, api_client: ApiClient) -> None:
        """
        Удаление комментария по id
        """
        resource_id = 100

        response = api_client.delete_resource_by_id(path=self.base_path, id=resource_id)
        response_data = response.json()

        assert response.status_code == HttpCodeEnum.OK.value
        assert not response_data
