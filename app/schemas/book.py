from typing import List, Optional, Union
from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    author: str
    published_year: Optional[int] = None


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    published_year: Optional[int] = None


class BookResponse(BookBase):
    id: int

    class Config:
        from_attributes = True


class BookFilter(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    published_year: Optional[int] = None


class SuccessResponse(BaseModel):
    success: bool
    message: str
    data: Optional[Union[BookResponse, List[BookResponse], dict]] = None
    error: Optional[dict] = None


class ErrorResponse(BaseModel):
    success: bool
    message: str
    data: Optional[dict] = None
    error: Optional[dict] = None