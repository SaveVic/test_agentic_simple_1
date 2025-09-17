# Books API

A simple RESTful API service to manage a collection of books built with Python, FastAPI, and SQLModel.

## Features

- Create, read, update, and delete books
- Filter books by title, author, or published year
- SQLite database for data persistence
- Docker support for easy deployment
- Comprehensive test suite

## Project Structure

```
books/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application entry point
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py      # Configuration settings
│   ├── database/
│   │   ├── __init__.py
│   │   └── database.py      # Database setup
│   ├── models/
│   │   ├── __init__.py
│   │   └── book.py          # Book model definition
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── book.py          # Pydantic schemas
│   └── api/
│       ├── __init__.py
│       ├── book_repository.py  # Data access layer
│       ├── book_service.py     # Business logic layer
│       └── book_routes.py      # API endpoints
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # Test configuration
│   ├── test_books.py        # Book API tests
│   └── test_config.py       # Configuration tests
├── Dockerfile               # Docker configuration
├── requirements.txt         # Python dependencies
└── README.md                # This file
```

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd books
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

### Using Python

1. Start the server:
   ```bash
   uvicorn app.main:app --reload
   ```

2. The API will be available at `http://localhost:8000`

### Using Docker

1. Build the Docker image:
   ```bash
   docker build -t books-api .
   ```

2. Run the container:
   ```bash
   docker run -p 8000:8000 books-api
   ```

3. The API will be available at `http://localhost:8000`

## API Endpoints

- `POST /books` - Create a new book
- `GET /books` - Retrieve all books (with optional filtering)
- `GET /books/{book_id}` - Retrieve a specific book by ID
- `PUT /books/{book_id}` - Update a specific book by ID
- `DELETE /books/{book_id}` - Delete a specific book by ID

### Filtering

The `GET /books` endpoint supports filtering by:
- `title` - Filter by title keyword
- `author` - Filter by author keyword
- `published_year` - Filter by published year

Example: `GET /books?title=Python&author=Guido`

## Testing

Run the test suite with pytest:
```bash
pytest
```

## Configuration

The application can be configured using environment variables:
- `ENVIRONMENT` - Set to "dev", "test", or "prod" (default: "dev")
- `DATABASE_URL` - Database connection string (default: "sqlite:///./books.db")

## Dependencies

- Python 3.11+
- FastAPI
- SQLModel
- Uvicorn
- Pydantic