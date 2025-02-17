import allure
import pytest
import responses
import requests

from utils.helpers.helpers import assert_http_code_is_not_found


@allure.epic("Сущность albums")
class TestAlbums:
    base_url = "http://localhost:8000"

    @allure.feature("Мок списка всех сущностей")
    @responses.activate
    @pytest.mark.test_case_id("UT-T300")
    def test_get_albums_list(self, mock_server) -> None:
        response = requests.get(f"{self.base_url}/albums/")

        http_code = response.status_code
        assert_http_code_is_not_found(http_code)
