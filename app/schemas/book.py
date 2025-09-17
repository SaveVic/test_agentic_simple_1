from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class BookBase(BaseModel):
    title: str
    author: str
    published_year: Optional[int] = None


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    pass


class BookResponse(BookBase):
    id: int

    class Config:
        from_attributes = True


class APIResponse(BaseModel):
    success: bool
    message: str
    data: Optional[dict | list] = None
    error: Optional[dict] = None