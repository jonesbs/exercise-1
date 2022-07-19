import requests
from django.conf import settings

from .exceptions import RequestFail


class GutendexClient:
    @staticmethod
    def get_url(*path_attributes):
        api_domain = settings.BOOKS_API
        path = "/".join(path_attributes)
        return f"{api_domain}{path}"

    @staticmethod
    def search(query_params: dict) -> dict:
        if not query_params:
            query_params = {}

        url = GutendexClient.get_url("/books")
        response = requests.get(url, params=query_params)

        if response.status_code != 200:
            raise RequestFail(response.status_code, response.json())

        content = response.json()
        return content

    @staticmethod
    def retrieve(book_id: int) -> dict:
        url = GutendexClient.get_url("/books", book_id)
        response = requests.get(url)

        if response.status_code != 200:
            raise RequestFail(response.status_code, response.json())

        content = response.json()
        return content
