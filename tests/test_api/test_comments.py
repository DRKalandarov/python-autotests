from tests.clients.api.api_client import ApiClient

from tests.enums.http_code_enum import HttpCodeEnum


class TestComments:
    base_path = "comments"

    def test_get_comments_list(self, api_client: ApiClient) -> None:
        response = api_client.get_resources(self.base_path)
        assert response.status_code == HttpCodeEnum.OK.value
