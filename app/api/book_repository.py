from typing import List, Optional
from sqlmodel import Session, select
from app.models.book import Book, BookCreate, BookUpdate


class BookRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_book(self, book_create: BookCreate) -> Book:
        db_book = Book.from_orm(book_create)
        self.session.add(db_book)
        self.session.commit()
        self.session.refresh(db_book)
        return db_book

    def get_book_by_id(self, book_id: int) -> Optional[Book]:
        statement = select(Book).where(Book.id == book_id)
        return self.session.exec(statement).first()

    def get_books(self) -> List[Book]:
        statement = select(Book)
        return self.session.exec(statement).all()

    def get_books_with_filters(self, title: Optional[str] = None, author: Optional[str] = None, published_year: Optional[int] = None) -> List[Book]:
        statement = select(Book)
        
        if title:
            statement = statement.where(Book.title.contains(title))
        if author:
            statement = statement.where(Book.author.contains(author))
        if published_year:
            statement = statement.where(Book.published_year == published_year)
            
        return self.session.exec(statement).all()

    def update_book(self, book_id: int, book_update: BookUpdate) -> Optional[Book]:
        db_book = self.get_book_by_id(book_id)
        if not db_book:
            return None
            
        # Update only the fields that were provided
        if book_update.title is not None:
            db_book.title = book_update.title
        if book_update.author is not None:
            db_book.author = book_update.author
        if book_update.published_year is not None:
            db_book.published_year = book_update.published_year
            
        self.session.add(db_book)
        self.session.commit()
        self.session.refresh(db_book)
        return db_book

    def delete_book(self, book_id: int) -> bool:
        db_book = self.get_book_by_id(book_id)
        if not db_book:
            return False
            
        self.session.delete(db_book)
        self.session.commit()
        return True