import pytest
import responses
import requests

from tests.clients.api.api_client import ApiClient
from tests.enums.http_code_enum import HttpCodeEnum


class TestAlbums:
    base_url = "http://127.0.0.1:8000"

    @responses.activate
    @pytest.mark.test_case_id("UT-T300")
    def test_get_albums_list(self, mock_server, api_client: ApiClient) -> None:
        # response = api_client.get_resources(path=self.base_path)
        response = requests.get(f"{self.base_url}/albums")
        assert response.status_code == HttpCodeEnum.NOT_FOUND.value

    @responses.activate
    @pytest.mark.test_case_id("UT-T301")
    def test_create_comment(self, mock_server, api_client: ApiClient) -> None:
        # response = api_client.get_resources(path=self.base_path)
        response = requests.post(f"{self.base_url}/comments")
        assert response.status_code == HttpCodeEnum.FORBIDDEN.value

    @responses.activate
    @pytest.mark.test_case_id("UT-T302")
    def test_delete_comment_by_id(self, mock_server, api_client: ApiClient) -> None:
        # response = api_client.get_resources(path=self.base_path)
        response = requests.delete(f"{self.base_url}/comments/1")
        assert response.status_code == HttpCodeEnum.INTERNAL_SERVER_ERROR.value
