from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.api.book_routes import router as book_router
from app.database.database import create_db_and_tables
from app.schemas.book import ErrorResponse

app = FastAPI(title="Books API", version="1.0.0")

# Create database and tables on startup
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Include routers
app.include_router(book_router)

# Exception handler for validation errors
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
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