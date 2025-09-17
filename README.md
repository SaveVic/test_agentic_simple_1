# Books API

A simple RESTful API service to manage a collection of books.

## Project Structure
```
books-api/
├── app/
│   ├── config/          # Configuration files
│   ├── models/          # Database models
│   ├── schemas/         # Pydantic schemas for validation
│   ├── repositories/     # Database operations
│   ├── services/         # Business logic
│   ├── routes/          # API endpoints
│   └── main.py          # Main application file
├── tests/               # Test files
├── main.py              # Application entry point
├── requirements.txt     # Project dependencies
├── Dockerfile           # Docker configuration
└── README.md            # This file
```

## Quick Start

### Prerequisites
- Python 3.11+
- pip (Python package installer)

### Installation
1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
```bash
python main.py
```
The API will be available at `http://localhost:8000`

### Testing
Run the test suite:
```bash
python -m pytest tests/
```

## API Endpoints

### Create a Book
- **URL**: `POST /books/`
- **Request Body**:
  ```json
  {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "published_year": 1925
  }
  ```
- **Response**:
  ```json
  {
    "success": true,
    "message": "Book created successfully",
    "data": {
      "id": 1,
      "title": "The Great Gatsby",
      "author": "F. Scott Fitzgerald",
      "published_year": 1925
    }
  }
  ```

### Get All Books
- **URL**: `GET /books/`
- **Response**:
  ```json
  {
    "success": true,
    "message": "Books retrieved successfully",
    "data": [
      {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "published_year": 1925
      }
    ]
  }
  ```

### Get Books with Filters
- **URL**: `GET /books/?title=Gatsby&author=F.%20Scott&published_year=1925`
- **Parameters**:
  - `title`: Filter by title keywords
  - `author`: Filter by author keywords
  - `published_year`: Filter by publication year
- **Response**:
  ```json
  {
    "success": true,
    "message": "Books retrieved successfully",
    "data": [...]
  }
  ```

### Get a Specific Book
- **URL**: `GET /books/{id}`
- **Response**:
  ```json
  {
    "success": true,
    "message": "Book retrieved successfully",
    "data": {
      "id": 1,
      "title": "The Great Gatsby",
      "author": "F. Scott Fitzgerald",
      "published_year": 1925
    }
  }
  ```

### Update a Book
- **URL**: `PUT /books/{id}`
- **Request Body**:
  ```json
  {
    "title": "Updated Title",
    "author": "Updated Author",
    "published_year": 1926
  }
  ```
- **Response**:
  ```json
  {
    "success": true,
    "message": "Book updated successfully",
    "data": {
      "id": 1,
      "title": "Updated Title",
      "author": "Updated Author",
      "published_year": 1926
    }
  }
  ```

### Delete a Book
- **URL**: `DELETE /books/{id}`
- **Response**:
  ```json
  {
    "success": true,
    "message": "Book deleted successfully"
  }
  ```

## Docker Support

### Build the Image
```bash
docker build -t books-api .
```

### Run the Container
```bash
docker run -p 8000:8000 books-api
```

## Testing with curl

### Create a book
```bash
curl -X POST "http://localhost:8000/books/" \
     -H "Content-Type: application/json" \
     -d '{"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "published_year": 1925}'
```

### Get all books
```bash
curl -X GET "http://localhost:8000/books/"
```

### Get a specific book
```bash
curl -X GET "http://localhost:8000/books/1"
```

### Update a book
```bash
curl -X PUT "http://localhost:8000/books/1" \
     -H "Content-Type: application/json" \
     -d '{"title": "Updated Title"}'
```

### Delete a book
```bash
curl -X DELETE "http://localhost:8000/books/1"
```

## API Documentation

Visit `http://localhost:8000/docs` for interactive API documentation.