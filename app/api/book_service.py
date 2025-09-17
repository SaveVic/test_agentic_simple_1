from typing import List, Optional
from sqlmodel import Session
from app.api.book_repository import BookRepository
from app.models.book import Book, BookCreate, BookUpdate
from app.schemas.book import BookFilter


class BookService:
    def __init__(self, session: Session):
        self.repository = BookRepository(session)

    def create_book(self, book_create: BookCreate) -> Book:
        return self.repository.create_book(book_create)

    def get_book_by_id(self, book_id: int) -> Optional[Book]:
        return self.repository.get_book_by_id(book_id)

    def get_books(self, filters: Optional[BookFilter] = None) -> List[Book]:
        if filters:
            return self.repository.get_books_with_filters(
                title=filters.title,
                author=filters.author,
                published_year=filters.published_year
            )
        return self.repository.get_books()

    def update_book(self, book_id: int, book_update: BookUpdate) -> Optional[Book]:
        return self.repository.update_book(book_id, book_update)

    def delete_book(self, book_id: int) -> bool:
        return self.repository.delete_book(book_id)