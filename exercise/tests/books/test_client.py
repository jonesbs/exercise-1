from datetime import datetime
from unittest import mock

import pytest
from books.client import GutendexClient
from books.exceptions import RequestFail
from django.conf import settings
from django.urls import reverse
from factories import ReviewFactory


@mock.patch("requests.get")
def test_gutendex_client_search_book_by_title_should_call_requests_with_valid_arguments(
    requests_mock, client_api
):

    requests_mock.return_value = mock.Mock(status_code=200)
    domain = settings.BOOKS_API
    query_params = {"search": "golden state", "page": 2}
    GutendexClient.search(query_params)
    requests_mock.assert_called_once_with(f"{domain}/books", params=query_params)


@mock.patch("requests.get")
def test_gutendex_client_search_book_by_title_should_call_requests_with_invalid_arguments(
    requests_mock, client_api
):

    requests_mock.return_value = mock.Mock(status_code=400)
    domain = settings.BOOKS_API
    query_params = {"search": "golden state", "page": "invalid"}

    with pytest.raises(RequestFail) as e:
        GutendexClient.search(query_params)

    requests_mock.assert_called_once_with(f"{domain}/books", params=query_params)


@mock.patch("requests.get")
def test_gutendex_client_retrieve_book_not_exist_should_raise_exception(
    requests_mock, client_api
):
    requests_mock.return_value = mock.Mock(status_code=400)
    book_id = "123456"
    domain = settings.BOOKS_API
    query_params = {"search": "golden state", "page": 2}

    with pytest.raises(RequestFail) as e:
        GutendexClient.retrieve(book_id)

    requests_mock.assert_called_once_with(f"{domain}/books/123456")


@mock.patch("requests.get")
def test_gutendex_client_retrieve_book_should_call_json_decode(
    requests_mock, client_api
):
    response_json = mock.Mock()
    response_json.status_code = 200
    response_json.json.return_value = "foo"

    requests_mock.return_value = response_json
    book_id = "123456"
    domain = settings.BOOKS_API
    query_params = {"search": "golden state", "page": 2}

    GutendexClient.retrieve(book_id)

    requests_mock.assert_called_once_with(f"{domain}/books/123456")
    response_json.json.assert_called()
