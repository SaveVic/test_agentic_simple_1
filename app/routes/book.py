from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session
from app.config.database import get_session
from app.services.book import BookService
from app.schemas.book import BookCreate, BookUpdate, BookResponse, APIResponse
from typing import List, Optional

router = APIRouter(prefix="/books", tags=["books"])


@router.post("/", response_model=APIResponse, status_code=201)
def create_book(
    book: BookCreate,
    session: Session = Depends(get_session)
):
    try:
        service = BookService(session)
        created_book = service.create_book(book)
        return APIResponse(
            success=True,
            message="Book created successfully",
            data=BookResponse.model_validate(created_book).model_dump()
        )
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))


@router.get("/", response_model=APIResponse)
def get_books(
    title: Optional[str] = Query(None, description="Filter by title keywords"),
    author: Optional[str] = Query(None, description="Filter by author keywords"),
    published_year: Optional[int] = Query(None, description="Filter by published year"),
    session: Session = Depends(get_session)
):
    service = BookService(session)
    books = service.get_books_by_filters(title, author, published_year)
    book_responses = [BookResponse.model_validate(book).model_dump() for book in books]
    return APIResponse(
        success=True,
        message="Books retrieved successfully",
        data=book_responses
    )


@router.get("/{book_id}", response_model=APIResponse)
def get_book(
    book_id: int,
    session: Session = Depends(get_session)
):
    service = BookService(session)
    book = service.get_book_by_id(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
        
    return APIResponse(
        success=True,
        message="Book retrieved successfully",
        data=BookResponse.model_validate(book).model_dump()
    )


@router.put("/{book_id}", response_model=APIResponse)
def update_book(
    book_id: int,
    book_update: BookUpdate,
    session: Session = Depends(get_session)
):
    service = BookService(session)
    updated_book = service.update_book(book_id, book_update)
    if not updated_book:
        raise HTTPException(status_code=404, detail="Book not found")
        
    return APIResponse(
        success=True,
        message="Book updated successfully",
        data=BookResponse.model_validate(updated_book).model_dump()
    )


@router.delete("/{book_id}", response_model=APIResponse)
def delete_book(
    book_id: int,
    session: Session = Depends(get_session)
):
    service = BookService(session)
    deleted = service.delete_book(book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")
        
    return APIResponse(
        success=True,
        message="Book deleted successfully"
    )