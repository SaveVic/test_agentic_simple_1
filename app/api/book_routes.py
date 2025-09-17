from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlmodel import Session
from app.database.database import get_session
from app.api.book_service import BookService
from app.models.book import BookCreate, BookUpdate
from app.schemas.book import BookResponse, SuccessResponse, ErrorResponse, BookFilter

router = APIRouter(prefix="/books", tags=["books"])


@router.post("/", response_model=SuccessResponse, status_code=status.HTTP_201_CREATED)
def create_book(
    book_create: BookCreate,
    session: Session = Depends(get_session)
) -> SuccessResponse:
    service = BookService(session)
    book = service.create_book(book_create)
    return SuccessResponse(
        success=True,
        message="Book created successfully",
        data=BookResponse.model_validate(book)
    )


@router.get("/", response_model=SuccessResponse)
def get_books(
    title: Optional[str] = Query(None, description="Filter by title"),
    author: Optional[str] = Query(None, description="Filter by author"),
    published_year: Optional[int] = Query(None, description="Filter by published year"),
    session: Session = Depends(get_session)
) -> SuccessResponse:
    service = BookService(session)
    filters = BookFilter(title=title, author=author, published_year=published_year)
    books = service.get_books(filters)
    book_responses = [BookResponse.model_validate(book) for book in books]
    return SuccessResponse(
        success=True,
        message="Books retrieved successfully",
        data=book_responses
    )


@router.get("/{book_id}", response_model=SuccessResponse)
def get_book(
    book_id: int,
    session: Session = Depends(get_session)
) -> SuccessResponse:
    service = BookService(session)
    book = service.get_book_by_id(book_id)
    if not book:
        return ErrorResponse(
            success=False,
            message="Book not found",
            error={"detail": "Book not found"}
        )
    return SuccessResponse(
        success=True,
        message="Book retrieved successfully",
        data=BookResponse.model_validate(book)
    )


@router.put("/{book_id}", response_model=SuccessResponse)
def update_book(
    book_id: int,
    book_update: BookUpdate,
    session: Session = Depends(get_session)
) -> SuccessResponse:
    service = BookService(session)
    book = service.update_book(book_id, book_update)
    if not book:
        return ErrorResponse(
            success=False,
            message="Book not found",
            error={"detail": "Book not found"}
        )
    return SuccessResponse(
        success=True,
        message="Book updated successfully",
        data=BookResponse.model_validate(book)
    )


@router.delete("/{book_id}", response_model=SuccessResponse)
def delete_book(
    book_id: int,
    session: Session = Depends(get_session)
) -> SuccessResponse:
    service = BookService(session)
    deleted = service.delete_book(book_id)
    if not deleted:
        return ErrorResponse(
            success=False,
            message="Book not found",
            error={"detail": "Book not found"}
        )
    return SuccessResponse(
        success=True,
        message="Book deleted successfully",
        data=None
    )