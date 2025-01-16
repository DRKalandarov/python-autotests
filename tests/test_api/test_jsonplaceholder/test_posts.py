import pytest

from typing import Any

from schemas.api.post.response.post_response import PostResponse

from tests.clients.api.jsonplaceholder_client import JsonplaceholderClient

from tests.enums.http_code_enum import HttpCodeEnum

from utils.compare.compare import is_eql


class TestPosts:
    base_path = "posts"

    @pytest.mark.test_case_id("UT-T300")
    def test_get_posts_list(self, jsonplaceholder_client: JsonplaceholderClient) -> None:
        """
        Получение списка всех постов
        """
        expected_response_data_len = 100

        response = jsonplaceholder_client.get_resources(path=self.base_path)
        response_data = response.json()

        assert response.status_code == HttpCodeEnum.OK.value
        assert PostResponse(**response_data[0])
        assert len(response_data) == expected_response_data_len

    @pytest.mark.parametrize("id", [1, 10, 100])
    @pytest.mark.test_case_id("UT-T301")
    def test_get_post_by_id(self, jsonplaceholder_client: JsonplaceholderClient, id: int) -> None:
        """
        Получение поста по id
        """
        response = jsonplaceholder_client.get_resource_by_id(path=self.base_path, id=id)
        response_data = response.json()

        assert response.status_code == HttpCodeEnum.OK.value
        assert PostResponse(**response_data)

    @pytest.mark.test_case_id("UT-T302")
    def test_create_post(self, jsonplaceholder_client: JsonplaceholderClient, post: dict[str, Any]) -> None:
        """
        Создание поста
        """
        response = jsonplaceholder_client.create_resource(path=self.base_path, data=post)
        response_data = response.json()

        assert response.status_code == HttpCodeEnum.CREATED.value
        assert PostResponse(**response_data)

        post["id"] = response_data["id"]
        assert is_eql(response_data, post)

    @pytest.mark.test_case_id("UT-T303")
    def test_update_post_by_id(self, jsonplaceholder_client: JsonplaceholderClient, post: dict[str, Any]) -> None:
        """
        Обновление поста по id
        """
        resource_id = 10

        response = jsonplaceholder_client.update_resource_by_id(path=self.base_path, id=resource_id, data=post)
        response_data = response.json()

        assert response.status_code == HttpCodeEnum.OK.value
        assert PostResponse(**response_data)

        post["id"] = resource_id
        assert is_eql(response_data, post)

    @pytest.mark.test_case_id("UT-T304")
    def test_delete_post_by_id(self, jsonplaceholder_client: JsonplaceholderClient) -> None:
        """
        Удаление поста по id
        """
        resource_id = 100

        response = jsonplaceholder_client.delete_resource_by_id(path=self.base_path, id=resource_id)
        response_data = response.json()

        assert response.status_code == HttpCodeEnum.OK.value
        assert not response_data
