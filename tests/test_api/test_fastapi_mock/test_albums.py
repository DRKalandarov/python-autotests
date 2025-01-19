import pytest
import responses

from tests.clients.api.api_client import ApiClient
from tests.enums.http_code_enum import HttpCodeEnum


class TestAlbums:
    base_path = "albums"

    @responses.activate
    @pytest.mark.test_case_id("UT-T300")
    def test_get_albums_list(self, api_client: ApiClient) -> None:
        response = api_client.get_resources(path=self.base_path)
        assert response.status_code == HttpCodeEnum.NOT_FOUND.value
