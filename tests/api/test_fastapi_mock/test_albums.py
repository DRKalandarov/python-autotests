import pytest
import responses
import requests

from tests.api.enums.http_code_enum import HttpCodeEnum


class TestAlbums:
    base_url = "http://127.0.0.1:8000"

    @responses.activate
    @pytest.mark.test_case_id("UT-T300")
    def test_get_albums_list(self, mock_server) -> None:
        response = requests.get(f"{self.base_url}/albums")
        assert response.status_code == HttpCodeEnum.NOT_FOUND.value
