import allure
import pytest

from typing import Any

from tests.api.clients.api_client import ApiClient

from utils.helpers import (
    assert_get_albums_list_is_ok,
    assert_get_album_by_id_is_ok,
    assert_album_is_created,
    assert_album_is_updated,
    assert_album_is_deleted,
)


@allure.epic("Сущность albums")
class TestAlbums:
    base_path = "albums"

    @allure.feature("Список всех сущностей")
    @pytest.mark.test_case_id("UT-T100")
    def test_get_albums_list(self, api_client: ApiClient) -> None:
        """
        Получение списка всех альбомов
        """
        expected_response_data_len = 100

        response = api_client.get_resources(self.base_path)
        assert_get_albums_list_is_ok(response, expected_response_data_len)

    @allure.feature("Получение сущности по id")
    @pytest.mark.parametrize("resource_id", [1, 10, 100])
    @pytest.mark.test_case_id("UT-T101")
    def test_get_album_by_id(self, api_client: ApiClient, resource_id: int) -> None:
        """
        Получение альбома по id
        """
        response = api_client.get_resource_by_id(self.base_path, resource_id)
        assert_get_album_by_id_is_ok(response)

    @allure.feature("Создание сущности")
    @pytest.mark.test_case_id("UT-T102")
    def test_create_album(self, api_client: ApiClient, album: dict[str, Any]) -> None:
        """
        Создание альбома
        """
        response = api_client.create_resource(self.base_path, album)
        assert_album_is_created(response, album)

    @allure.feature("Обновление сущности по id")
    @pytest.mark.test_case_id("UT-T103")
    def test_update_album_by_id(self, api_client: ApiClient, album: dict[str, Any]) -> None:
        """
        Обновление альбома по id
        """
        resource_id = 10

        response = api_client.update_resource_by_id(self.base_path, resource_id, album)
        assert_album_is_updated(response, album)

    @allure.feature("Удаление сущности по id")
    @pytest.mark.test_case_id("UT-T104")
    def test_delete_album_by_id(self, api_client: ApiClient) -> None:
        """
        Удаление альбома по id
        """
        resource_id = 100

        response = api_client.delete_resource_by_id(self.base_path, resource_id)
        assert_album_is_deleted(response)
