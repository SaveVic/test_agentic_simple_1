from sqlmodel import create_engine, Session
from app.config.settings import settings
from app.models.book import Book
from sqlmodel import SQLModel


engine = create_engine(settings.DATABASE_URL, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session