import allure
import pytest
import responses
import requests

from utils.helpers import assert_http_code_is_404


@allure.epic("Сущность albums")
class TestAlbums:
    base_url = "http://localhost:8000/albums/"

    @allure.feature("Мок списка всех сущностей")
    @responses.activate
    @pytest.mark.test_case_id("UT-T300")
    def test_get_albums_list(self, mock_server) -> None:
        response = requests.get(self.base_url)

        http_code = response.status_code
        assert_http_code_is_404(http_code)
