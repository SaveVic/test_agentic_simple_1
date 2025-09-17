# Book Management Service

This is a simple RESTful API service to manage a collection of books, built with Python, FastAPI, and SQLModel.

## Features

- Create, Read, Update, and Delete books.
- Filter books by title, author, and published year.
- SQLite database for storage.
- Docker support for containerization.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```

2.  **Create a virtual environment and install dependencies:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

## Running the Application

-   **Using uvicorn:**
    ```bash
    uvicorn app.main:app --reload
    ```
    The application will be available at `http://127.0.0.1:8000`.

-   **Using Docker:**
    1.  **Build the Docker image:**
        ```bash
        docker build -t book-service .
        ```
    2.  **Run the Docker container:**
        ```bash
        docker run -p 8000:8000 book-service
        ```
    The application will be available at `http://localhost:8000`.

## API Endpoints

-   `POST /books`: Create a new book.
-   `GET /books`: Retrieve a list of all books.
-   `GET /books?title=<...>&author=<...>&published_year=<...>`: Filter books.
-   `GET /books/{book_id}`: Retrieve a single book by its ID.
-   `PUT /books/{book_id}`: Update an existing book's details.
-   `DELETE /books/{book_id}`: Delete a book by its ID.

## Testing

To run the tests, use pytest:

```bash
pytest
```