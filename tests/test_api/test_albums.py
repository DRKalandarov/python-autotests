import pytest

from typing import Any

from schemas.api.album.response.album_response import AlbumResponse

from tests.clients.api.api_client import ApiClient

from tests.enums.http_code_enum import HttpCodeEnum

from utils.compare.compare import is_eql


class TestAlbums:
    base_path = "albums"

    @pytest.mark.test_case_id("UT-T100")
    def test_get_albums_list(self, api_client: ApiClient) -> None:
        """
        Получение списка всех альбомов
        """
        expected_response_data_len = 100

        response = api_client.get_resources(path=self.base_path)
        response_data = response.json()

        assert response.status_code == HttpCodeEnum.OK.value
        assert AlbumResponse(**response_data[0])
        assert len(response_data) == expected_response_data_len

    @pytest.mark.parametrize("id", [1, 10, 100])
    @pytest.mark.test_case_id("UT-T101")
    def test_get_album_by_id(self, api_client: ApiClient, id: int) -> None:
        """
        Получение албома по id
        """
        response = api_client.get_resource_by_id(path=self.base_path, id=id)
        response_data = response.json()

        assert response.status_code == HttpCodeEnum.OK.value
        assert AlbumResponse(**response_data)

    @pytest.mark.test_case_id("UT-T102")
    def test_create_album(self, api_client: ApiClient, album: dict[str, Any]) -> None:
        """
        Создание альбома
        """
        response = api_client.create_resource(path=self.base_path, data=album)
        response_data = response.json()

        assert response.status_code == HttpCodeEnum.CREATED.value
        assert AlbumResponse(**response_data)

        album["id"] = response_data["id"]
        assert is_eql(response_data, album)

    @pytest.mark.test_case_id("UT-T103")
    def test_update_album_by_id(self, api_client: ApiClient, album: dict[str, Any]) -> None:
        """
        Обновление альбома по id
        """
        resource_id = 10

        response = api_client.update_resource_by_id(path=self.base_path, id=resource_id, data=album)
        response_data = response.json()

        assert response.status_code == HttpCodeEnum.OK.value
        assert AlbumResponse(**response_data)

        album["id"] = resource_id
        assert is_eql(response_data, album)

    @pytest.mark.test_case_id("UT-T104")
    def test_delete_album_by_id(self, api_client: ApiClient) -> None:
        """
        Удаление альбома по id
        """
        resource_id = 100

        response = api_client.delete_resource_by_id(path=self.base_path, id=resource_id)
        response_data = response.json()

        assert response.status_code == HttpCodeEnum.OK.value
        assert not response_data
