import pytest
from rest_framework.test import APIClient


@pytest.fixture()
def client_api():
    client = APIClient()
    return client


@pytest.fixture
def gutendex_example_1():
    return {
        "id": 291,
        "title": "The Golden Age",
        "authors": [
            {"name": "Grahame, Kenneth", "birth_year": 1859, "death_year": 1932}
        ],
        "translators": [],
        "subjects": [
            "Bildungsromans",
            "Brothers and sisters -- Fiction",
            "Country life -- Fiction",
            "England -- Fiction",
            "Pastoral fiction",
        ],
        "bookshelves": [],
        "languages": ["en"],
        "copyright": False,
        "media_type": "Text",
        "formats": {
            "text/html; charset=utf-8": "https://www.gutenberg.org/files/291/291-h.zip",
            "application/epub+zip": "https://www.gutenberg.org/ebooks/291.epub.images",
            "application/rdf+xml": "https://www.gutenberg.org/ebooks/291.rdf",
            "application/x-mobipocket-ebook": "https://www.gutenberg.org/ebooks/291.kindle.images",
            "text/plain; charset=utf-8": "https://www.gutenberg.org/files/291/291-0.txt",
            "text/html": "https://www.gutenberg.org/ebooks/291.html.images",
            "image/jpeg": "https://www.gutenberg.org/cache/epub/291/pg291.cover.medium.jpg",
        },
        "download_count": 62,
    }


@pytest.fixture
def gutendex_example_2():
    return {
        "id": 15661,
        "title": "The Golden Goose Book",
        "authors": [
            {
                "name": "Brooke, L. Leslie (Leonard Leslie)",
                "birth_year": 1862,
                "death_year": 1940,
            }
        ],
        "translators": [],
        "subjects": ["Fairy tales"],
        "bookshelves": ["Children's Picture Books"],
        "languages": ["en"],
        "copyright": False,
        "media_type": "Text",
        "formats": {
            "image/jpeg": "https://www.gutenberg.org/cache/epub/15661/pg15661.cover.small.jpg",
            "application/zip": "https://www.gutenberg.org/files/15661/15661-h.zip",
            "text/html; charset=us-ascii": "https://www.gutenberg.org/files/15661/15661-h/15661-h.htm",
            "text/plain; charset=us-ascii": "https://www.gutenberg.org/files/15661/15661.txt",
            "text/html": "https://www.gutenberg.org/ebooks/15661.html.images",
            "application/x-mobipocket-ebook": "https://www.gutenberg.org/ebooks/15661.kindle.images",
            "application/rdf+xml": "https://www.gutenberg.org/ebooks/15661.rdf",
            "application/epub+zip": "https://www.gutenberg.org/ebooks/15661.epub.images",
            "text/plain": "https://www.gutenberg.org/ebooks/15661.txt.utf-8",
        },
        "download_count": 62,
    }


@pytest.fixture()
def gutendex_search_data(gutendex_example_1, gutendex_example_2):
    return {
        "count": 2,
        "next": None,
        "previous": None,
        "results": [gutendex_example_1, gutendex_example_2],
    }
