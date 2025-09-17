import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_book():
    response = client.post(
        "/books/",
        json={"title": "Test Book", "author": "Test Author", "published_year": 2023},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["success"] == True
    assert data["message"] == "Book created successfully"
    assert "data" in data
    assert data["data"]["title"] == "Test Book"
    assert data["data"]["author"] == "Test Author"
    assert data["data"]["published_year"] == 2023
    assert "id" in data["data"]


def test_create_book_missing_title():
    response = client.post(
        "/books/", json={"author": "Test Author", "published_year": 2023}
    )  # Missing title
    assert response.status_code == 422
    data = response.json()
    assert data["success"] == False


def test_create_book_missing_author():
    response = client.post(
        "/books/", json={"title": "Test Book", "published_year": 2023}
    )  # Missing author
    assert response.status_code == 422
    data = response.json()
    assert data["success"] == False


def test_create_book_missing_year():
    response = client.post(
        "/books/", json={"title": "Test Book", "author": "Test Author"}
    )  # Missing year
    assert response.status_code == 201
    data = response.json()
    assert data["success"] == True


def test_get_books():
    # First create a book
    client.post(
        "/books/",
        json={
            "title": "Test Book 1",
            "author": "Test Author 1",
            "published_year": 2023,
        },
    )
    client.post(
        "/books/",
        json={
            "title": "Test Book 2",
            "author": "Test Author 2",
            "published_year": 2022,
        },
    )

    response = client.get("/books/")
    assert response.status_code == 200
    data = response.json()
    assert data["success"] == True
    assert data["message"] == "Books retrieved successfully"
    assert "data" in data
    assert len(data["data"]) >= 2


def test_get_book_by_id():
    # First create a book
    create_response = client.post(
        "/books/",
        json={"title": "Test Book", "author": "Test Author", "published_year": 2023},
    )
    book_id = create_response.json()["data"]["id"]

    response = client.get(f"/books/{book_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["success"] == True
    assert data["message"] == "Book retrieved successfully"
    assert "data" in data
    assert data["data"]["id"] == book_id
    assert data["data"]["title"] == "Test Book"


def test_get_book_by_id_not_found():
    response = client.get("/books/99999")
    assert response.status_code == 404
    data = response.json()
    assert data["success"] == False


def test_update_book():
    # First create a book
    create_response = client.post(
        "/books/",
        json={"title": "Test Book", "author": "Test Author", "published_year": 2023},
    )
    book_id = create_response.json()["data"]["id"]

    # Update the book
    response = client.put(
        f"/books/{book_id}",
        json={"title": "Updated Test Book", "author": "Updated Author"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["success"] == True
    assert data["message"] == "Book updated successfully"
    assert "data" in data
    assert data["data"]["title"] == "Updated Test Book"
    assert data["data"]["author"] == "Updated Author"
    assert data["data"]["published_year"] == 2023  # Should remain unchanged


def test_update_book_with_title_only():
    # First create a book
    create_response = client.post(
        "/books/",
        json={"title": "Test Book", "author": "Test Author", "published_year": 2023},
    )
    book_id = create_response.json()["data"]["id"]

    # Update the book
    response = client.put(
        f"/books/{book_id}",
        json={"title": "Updated Test Book"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["success"] == True
    assert data["message"] == "Book updated successfully"
    assert "data" in data
    assert data["data"]["title"] == "Updated Test Book"
    assert data["data"]["author"] == "Test Author"
    assert data["data"]["published_year"] == 2023  # Should remain unchanged


def test_update_book_with_author_only():
    # First create a book
    create_response = client.post(
        "/books/",
        json={"title": "Test Book", "author": "Test Author", "published_year": 2023},
    )
    book_id = create_response.json()["data"]["id"]

    # Update the book
    response = client.put(
        f"/books/{book_id}",
        json={"author": "Updated Author"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["success"] == True
    assert data["message"] == "Book updated successfully"
    assert "data" in data
    assert data["data"]["title"] == "Test Book"
    assert data["data"]["author"] == "Updated Author"
    assert data["data"]["published_year"] == 2023  # Should remain unchanged


def test_update_book_with_year_only():
    # First create a book
    create_response = client.post(
        "/books/",
        json={"title": "Test Book", "author": "Test Author", "published_year": 2023},
    )
    book_id = create_response.json()["data"]["id"]

    # Update the book
    response = client.put(
        f"/books/{book_id}",
        json={"published_year": "2099"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["success"] == True
    assert data["message"] == "Book updated successfully"
    assert "data" in data
    assert data["data"]["title"] == "Test Book"
    assert data["data"]["author"] == "Test Author"
    assert data["data"]["published_year"] == 2099  # Should remain unchanged


def test_update_book_not_found():
    response = client.put(
        "/books/99999", json={"title": "Updated Test Book", "author": "Updated Author"}
    )
    assert response.status_code == 404
    data = response.json()
    assert data["success"] == False


def test_delete_book():
    # First create a book
    create_response = client.post(
        "/books/",
        json={"title": "Test Book", "author": "Test Author", "published_year": 2023},
    )
    book_id = create_response.json()["data"]["id"]

    # Delete the book
    response = client.delete(f"/books/{book_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["success"] == True
    assert data["message"] == "Book deleted successfully"


def test_delete_book_not_found():
    response = client.delete("/books/99999")
    assert response.status_code == 404
    data = response.json()
    assert data["success"] == False


def test_get_books_with_filters():
    # First, delete all existing books to ensure a clean state
    response = client.get("/books/")
    if response.status_code == 200:
        data = response.json()
        for book in data.get("data", []):
            client.delete(f"/books/{book['id']}")

    # Create test books
    client.post(
        "/books/",
        json={
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "published_year": 1925,
        },
    )
    client.post(
        "/books/",
        json={
            "title": "To Kill a Mockingbird",
            "author": "Harper Lee",
            "published_year": 1960,
        },
    )
    client.post(
        "/books/",
        json={"title": "1984", "author": "George Orwell", "published_year": 1949},
    )

    # Filter by title
    response = client.get("/books/?title=Gatsby")
    assert response.status_code == 200
    data = response.json()
    assert len(data["data"]) == 1
    assert data["data"][0]["title"] == "The Great Gatsby"

    # Filter by author
    response = client.get("/books/?author=Orwell")
    assert response.status_code == 200
    data = response.json()
    assert len(data["data"]) == 1
    assert data["data"][0]["author"] == "George Orwell"

    # Filter by year
    response = client.get("/books/?published_year=1960")
    assert response.status_code == 200
    data = response.json()
    assert len(data["data"]) == 1
    assert data["data"][0]["published_year"] == 1960

    # Filter by multiple parameters
    response = client.get("/books/?title=1984&author=George")
    assert response.status_code == 200
    data = response.json()
    assert len(data["data"]) == 1
    assert data["data"][0]["title"] == "1984"
    assert data["data"][0]["author"] == "George Orwell"
