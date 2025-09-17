from fastapi import FastAPI
from app.api.book_routes import router as book_router
from app.database.database import create_db_and_tables

app = FastAPI(title="Books API", version="1.0.0")

# Create database and tables on startup
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Include routers
app.include_router(book_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Books API"}