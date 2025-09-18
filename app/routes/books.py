from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from app.models import Book
from app.schemas import APIResponse, BookCreate, BookUpdate
from app.services import BookService

router = APIRouter()


@router.post(
    "/",
    response_model=APIResponse[Book],
    status_code=status.HTTP_201_CREATED,
)
def create_book(
    book_create: BookCreate, service: BookService = Depends()
) -> APIResponse[Book]:
    book = service.create_book(book_create)
    return APIResponse(
        success=True,
        message="Book created successfully",
        data=book,
    )


@router.get(
    "/",
    response_model=APIResponse[List[Book]],
    status_code=status.HTTP_200_OK,
)
def get_all_books(
    title: Optional[str] = None,
    author: Optional[str] = None,
    published_year: Optional[int] = None,
    service: BookService = Depends(),
) -> APIResponse[List[Book]]:
    books = service.get_all_books(title, author, published_year)
    return APIResponse(
        success=True,
        message="Books retrieved successfully",
        data=books,
    )


@router.get(
    "/{book_id}",
    response_model=APIResponse[Book],
    status_code=status.HTTP_200_OK,
)
def get_book_by_id(book_id: int, service: BookService = Depends()) -> APIResponse[Book]:
    book = service.get_book_by_id(book_id)
    if book:
        return APIResponse(
            success=True,
            message="Book retrieved successfully",
            data=book,
        )
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=APIResponse(
            success=False,
            message="Book not found",
            error={"code": 404, "message": "Book not found"},
            data=None
        ).model_dump(exclude_none=True),
    )


@router.put(
    "/{book_id}",
    response_model=APIResponse[Book],
    status_code=status.HTTP_200_OK,
)
def update_book(
    book_id: int, book_update: BookUpdate, service: BookService = Depends()
) -> APIResponse[Book]:
    book = service.update_book(book_id, book_update)
    if book:
        return APIResponse(
            success=True,
            message="Book updated successfully",
            data=book,
        )
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=APIResponse(
            success=False,
            message="Book not found",
            error={"code": 404, "message": "Book not found"},
            data=None
        ).model_dump(exclude_none=True),
    )


@router.delete(
    "/{book_id}",
    response_model=APIResponse,
    status_code=status.HTTP_200_OK,
)
def delete_book(book_id: int, service: BookService = Depends()) -> APIResponse:
    if service.delete_book(book_id):
        return APIResponse(success=True, message="Book deleted successfully", data=None)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=APIResponse(
            success=False,
            message="Book not found",
            error={"code": 404, "message": "Book not found"},
            data=None
        ).model_dump(exclude_none=True),
    )