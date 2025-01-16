import asyncio
import httpx
import pytest

from tests.enums.http_code_enum import HttpCodeEnum


class TestAsyncRequestToMultipleEndpoints:
    urls = [
        "https://jsonplaceholder.typicode.com/albums",
        "https://jsonplaceholder.typicode.com/comments",
        "https://jsonplaceholder.typicode.com/posts",
    ]

    @pytest.mark.asyncio
    @pytest.mark.test_case_id("UT-T400")
    async def test_get_resources_list(self) -> None:
        """
        Асинхронная отправка GET запросов
        """
        async with httpx.AsyncClient() as client:
            tasks = [client.get(url) for url in self.urls]
            responses = await asyncio.gather(*tasks)
        for response in responses:
            assert response.status_code == HttpCodeEnum.OK.value
