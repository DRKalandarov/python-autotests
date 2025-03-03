import allure
import pytest

from typing import Any

from tests.api.clients.api_client import ApiClient

from utils.helpers import (
    assert_get_comments_list_is_ok,
    assert_get_comment_by_id_is_ok,
    assert_comment_is_created,
    assert_comment_is_updated,
    assert_comment_is_deleted,
)


@allure.epic("Сущность comments")
class TestComments:
    base_path = "comments"

    @allure.feature("Список всех сущностей")
    @pytest.mark.test_case_id("UT-T200")
    def test_get_comments_list(self, api_client: ApiClient) -> None:
        """
        Получение списка всех комментариев
        """
        expected_response_data_len = 500

        response = api_client.get_resources(self.base_path)
        assert_get_comments_list_is_ok(response, expected_response_data_len)

    @allure.feature("Получение сущности по id")
    @pytest.mark.parametrize("post_id", [1, 10, 100])
    @pytest.mark.test_case_id("UT-T201")
    def test_get_comment_by_id(self, api_client: ApiClient, post_id: int) -> None:
        """
        Получение комментария по id
        """
        response = api_client.get_resource_by_id(self.base_path, post_id)
        assert_get_comment_by_id_is_ok(response)

    @allure.feature("Создание сущности")
    @pytest.mark.test_case_id("UT-T202")
    def test_create_comment(self, api_client: ApiClient, comment: dict[str, Any]) -> None:
        """
        Создание комментария
        """
        response = api_client.create_resource(self.base_path, comment)
        assert_comment_is_created(response, comment)

    @allure.feature("Обновление сущности по id")
    @pytest.mark.test_case_id("UT-T203")
    def test_update_comment_by_id(self, api_client: ApiClient, comment: dict[str, Any]) -> None:
        """
        Обновление комментария по id
        """
        resource_id = 10

        response = api_client.update_resource_by_id(self.base_path, resource_id, comment)
        assert_comment_is_updated(response, comment)

    @allure.feature("Удаление сущности по id")
    @pytest.mark.test_case_id("UT-T204")
    def test_delete_comment_by_id(self, api_client: ApiClient) -> None:
        """
        Удаление комментария по id
        """
        resource_id = 100

        response = api_client.delete_resource_by_id(self.base_path, resource_id)
        assert_comment_is_deleted(response)
