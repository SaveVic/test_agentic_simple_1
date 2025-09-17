from typing import Optional
from sqlmodel import Field, SQLModel


class BookBase(SQLModel):
    title: str
    author: str
    published_year: Optional[int] = None


class Book(BookBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class BookCreate(BookBase):
    pass


class BookUpdate(SQLModel):
    title: Optional[str] = None
    author: Optional[str] = None
    published_year: Optional[int] = None


class BookResponse(BookBase):
    id: int