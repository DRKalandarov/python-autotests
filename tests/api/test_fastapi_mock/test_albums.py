import allure
import pytest
import responses
import requests

from tests.api.enums.http_code_enum import HttpCodeEnum


@allure.epic("Сущность albums")
class TestAlbums:
    base_url = "http://localhost:8000"

    @allure.feature("Мок списка всех сущностей")
    @responses.activate
    @pytest.mark.test_case_id("UT-T300")
    def test_get_albums_list(self, mock_server) -> None:
        response = requests.get(f"{self.base_url}/albums/")
        assert response.status_code == HttpCodeEnum.NOT_FOUND.value
