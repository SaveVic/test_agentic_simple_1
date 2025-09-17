from typing import List, Optional
from fastapi import Depends
from sqlmodel import Session
from app.config.database import get_session
from app.models import Book
from app.repositories import BookRepository
from app.schemas import BookCreate, BookUpdate


class BookService:
    def __init__(self, session: Session = Depends(get_session)):
        self.repo = BookRepository(session)

    def create_book(self, book_create: BookCreate) -> Book:
        book = Book.model_validate(book_create)
        return self.repo.create_book(book)

    def get_all_books(
        self,
        title: Optional[str] = None,
        author: Optional[str] = None,
        published_year: Optional[int] = None,
    ) -> List[Book]:
        return self.repo.get_all_books(title, author, published_year)

    def get_book_by_id(self, book_id: int) -> Optional[Book]:
        return self.repo.get_book_by_id(book_id)

    def update_book(self, book_id: int, book_update: BookUpdate) -> Optional[Book]:
        book = self.repo.get_book_by_id(book_id)
        if book:
            update_data = book_update.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(book, key, value)
            return self.repo.update_book(book)
        return None

    def delete_book(self, book_id: int) -> bool:
        book = self.repo.get_book_by_id(book_id)
        if book:
            self.repo.delete_book(book)
            return True
        return False