from sqlmodel import SQLModel, create_engine, Session
from app.config.settings import settings
# Import the Book model to ensure it's registered with SQLModel
from app.models.book import Book

# Create the database engine
engine = create_engine(settings.DATABASE_URL, echo=True)


def create_db_and_tables():
    """Create the database and tables."""
    SQLModel.metadata.create_all(engine)


def get_session():
    """Get a database session."""
    with Session(engine) as session:
        yield session