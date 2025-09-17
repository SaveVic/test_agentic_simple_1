from app.repositories.book import BookRepository
from app.models.book import Book
from app.schemas.book import BookCreate, BookUpdate
from typing import List, Optional
from sqlmodel import Session


class BookService:
    def __init__(self, session: Session):
        self.repository = BookRepository(session)

    def create_book(self, book_create: BookCreate) -> Book:
        book = Book(**book_create.model_dump())
        return self.repository.create_book(book)

    def get_book_by_id(self, book_id: int) -> Optional[Book]:
        return self.repository.get_book_by_id(book_id)

    def get_all_books(self) -> List[Book]:
        return self.repository.get_all_books()

    def get_books_by_filters(self, title: Optional[str] = None, author: Optional[str] = None, published_year: Optional[int] = None) -> List[Book]:
        return self.repository.get_books_by_filters(title, author, published_year)

    def update_book(self, book_id: int, book_update: BookUpdate) -> Optional[Book]:
        return self.repository.update_book(book_id, book_update.model_dump(exclude_unset=True))

    def delete_book(self, book_id: int) -> bool:
        return self.repository.delete_book(book_id)