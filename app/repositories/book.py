from sqlmodel import Session, select
from app.models.book import Book
from typing import Optional, List


class BookRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_book(self, book: Book) -> Book:
        self.session.add(book)
        self.session.commit()
        self.session.refresh(book)
        return book

    def get_book_by_id(self, book_id: int) -> Optional[Book]:
        return self.session.get(Book, book_id)

    def get_all_books(self) -> List[Book]:
        statement = select(Book)
        return self.session.exec(statement).all()

    def get_books_by_filters(self, title: Optional[str] = None, author: Optional[str] = None, published_year: Optional[int] = None) -> List[Book]:
        statement = select(Book)
        
        if title:
            statement = statement.where(Book.title.contains(title))
        if author:
            statement = statement.where(Book.author.contains(author))
        if published_year:
            statement = statement.where(Book.published_year == published_year)
            
        return self.session.exec(statement).all()

    def update_book(self, book_id: int, book_data: dict) -> Optional[Book]:
        db_book = self.session.get(Book, book_id)
        if not db_book:
            return None
            
        for key, value in book_data.items():
            if value is not None:
                setattr(db_book, key, value)
                
        db_book.updated_at = db_book.__class__.updated_at.default.func()
        self.session.add(db_book)
        self.session.commit()
        self.session.refresh(db_book)
        return db_book

    def delete_book(self, book_id: int) -> bool:
        book = self.session.get(Book, book_id)
        if not book:
            return False
            
        self.session.delete(book)
        self.session.commit()
        return True