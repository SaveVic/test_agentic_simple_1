from typing import Optional, TypeVar, Generic
from pydantic import BaseModel, Field

T = TypeVar("T")


class APIResponse(BaseModel, Generic[T]):
    success: bool = True
    message: str = "Success"
    data: Optional[T] = None
    error: Optional[dict] = None


class BookCreate(BaseModel):
    title: str
    author: str
    published_year: Optional[int] = None


class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    published_year: Optional[int] = None