from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.api.book_routes import router as book_router
from app.database.database import create_db_and_tables
from app.schemas.book import ErrorResponse


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create database and tables on startup
    create_db_and_tables()
    yield
    # Cleanup on shutdown (if needed)


app = FastAPI(title="Books API", version="1.0.0", lifespan=lifespan)

# Include routers
app.include_router(book_router)

# Exception handler for validation errors
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,  # Fixed deprecation warning
        content={
            "success": False,
            "message": "Validation error",
            "data": None,
            "error": {"detail": exc.errors()}
        }
    )

@app.get("/")
def read_root():
    return {"message": "Welcome to the Books API"}