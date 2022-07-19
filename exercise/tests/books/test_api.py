from datetime import datetime
from unittest import mock

import pytest
from django.urls import reverse
from factories import ReviewFactory


@mock.patch("books.client.GutendexClient.search")
def test_gutendex_search_book_by_title_should_retrieve_list_of_books(
    client_search_mock, client_api, gutendex_search_data
):
    client_search_mock.return_value = gutendex_search_data

    url = "{}?{}".format(reverse("books:book-list"), "search=foo")
    response = client_api.get(url, format="json")
    assert response.status_code == 200
    assert len(response.data) == 2


@mock.patch("books.client.GutendexClient.search")
def test_gutendex_search_book_should_retrieve_empty_list_books(
    client_search_mock, client_api, gutendex_search_data
):
    gutendex_search_data["results"] = []
    client_search_mock.return_value = gutendex_search_data

    url = "{}?{}".format(reverse("books:book-list"), "search=foo")
    response = client_api.get(url, format="json")
    assert response.status_code == 200
    assert len(response.data) == 0
    client_search_mock.assert_called()


@mock.patch("books.client.GutendexClient.search")
def test_gutendex_create_book_should_return_status_code_405(
    client_search_mock, client_api, gutendex_search_data
):
    gutendex_search_data["results"] = []
    client_search_mock.return_value = gutendex_search_data

    url = reverse("books:book-list")
    response = client_api.post(url, {"title": "example 1"}, format="json")
    assert response.status_code == 405
    client_search_mock.assert_not_called()


@mock.patch("books.client.GutendexClient.retrieve")
def test_gutendex_update_book_should_return_status_code_405(
    client_search_mock, client_api, gutendex_search_data
):

    gutendex_search_data["results"] = []
    client_search_mock.return_value = gutendex_search_data

    url = reverse("books:book-detail", args=["1234"])
    response = client_api.patch(url, {"title": "example 1"}, format="json")
    assert response.status_code == 405
    client_search_mock.assert_not_called()


@mock.patch("books.client.GutendexClient.retrieve")
def test_gutendex_retrieve_book_by_id_should_return_book_detail_without_rating(
    client_search_mock, client_api, gutendex_example_1, db
):

    client_search_mock.return_value = gutendex_example_1

    url = reverse("books:book-detail", args=["291"])
    response = client_api.get(url, {"title": "example 1"}, format="json")
    assert response.status_code == 200
    client_search_mock.assert_called()
    assert "291" in client_search_mock.call_args.args
    response.data["rating"] is None


@mock.patch("books.client.GutendexClient.retrieve")
def test_gutendex_retrieve_book_by_id_should_return_book_detail_with_previous_rating(
    client_search_mock, client_api, gutendex_example_1, db
):
    review_1 = ReviewFactory(book_id="291")
    review_2 = ReviewFactory(book_id="291")

    client_search_mock.return_value = gutendex_example_1

    url = reverse("books:book-detail", args=["291"])
    response = client_api.get(url, {"title": "example 1"}, format="json")
    assert response.status_code == 200
    client_search_mock.assert_called()
    assert "291" in client_search_mock.call_args.args
    assert response.data["rating"] == str((review_1.rate + review_2.rate) / 2)
    assert str(review_1.review) in response.data["reviews"]
    assert str(review_2.review) in response.data["reviews"]


def test_create_review_should_return_status_code_201(client_api, db):

    book_review_payload = {
        "book_id": 15661,
        "review": "My review made to book 15661",
        "rate": 5,
    }

    url = reverse("books:review-list")
    response = client_api.post(url, book_review_payload, format="json")
    assert response.status_code == 201


@pytest.mark.parametrize(
    "book_review_invalid_payload",
    [
        {},
        {"review": "My review made to book 15661", "rate": 5},
        {"book_id": None, "review": "My review made to book 15661", "rate": 5},
        {"book_id": "", "review": "My review made to book 15661", "rate": 5},
        {"book_id": "test", "review": "My review made to book 15661", "rate": 5},
        {"book_id": "15661", "review": "", "rate": 5},
        {"book_id": "15661", "review": None, "rate": 5},
        {"book_id": "test", "rate": 5},
        {"book_id": "15661", "review": "My review made to book 15661", "rate": -1},
        {"book_id": "15661", "review": "My review made to book 15661", "rate": 6},
        {
            "book_id": "15661",
            "review": "My review made to book 15661",
        },
    ],
)
def test_create_review_with_invalid_data_should_return_status_code_400(
    book_review_invalid_payload, client_api, db
):

    url = reverse("books:review-list")
    response = client_api.post(url, book_review_invalid_payload, format="json")
    assert response.status_code == 400


def test_update_review_should_return_status_code_405(client_api, db):

    book_review_payload = {
        "book_id": 15661,
        "review": "My review made to book 15661",
        "rate": 5,
    }

    url = reverse("books:review-list")
    response = client_api.put(url, book_review_payload, format="json")
    assert response.status_code == 405


def test_list_review_should_return_status_code_405(client_api, db):

    url = reverse("books:review-list")
    response = client_api.get(url, format="json")
    assert response.status_code == 405
