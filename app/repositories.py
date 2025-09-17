from typing import List, Optional
from sqlmodel import Session, select
from app.models import Book


class BookRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_book(self, book: Book) -> Book:
        self.session.add(book)
        self.session.commit()
        self.session.refresh(book)
        return book

    def get_all_books(
        self,
        title: Optional[str] = None,
        author: Optional[str] = None,
        published_year: Optional[int] = None,
    ) -> List[Book]:
        statement = select(Book)
        if title:
            statement = statement.where(Book.title.contains(title))
        if author:
            statement = statement.where(Book.author.contains(author))
        if published_year:
            statement = statement.where(Book.published_year == published_year)
        return self.session.exec(statement).all()

    def get_book_by_id(self, book_id: int) -> Optional[Book]:
        return self.session.get(Book, book_id)

    def update_book(self, book: Book) -> Book:
        self.session.add(book)
        self.session.commit()
        self.session.refresh(book)
        return book

    def delete_book(self, book: Book):
        self.session.delete(book)
        self.session.commit()