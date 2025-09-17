from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from app.config.database import create_db_and_tables
from app.routes.book import router as book_router
from app.schemas.book import APIResponse


app = FastAPI(title="Books API", version="1.0.0", description="A simple API to manage books")


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=422,
        content=APIResponse(
            success=False,
            message="Validation error",
            error={"details": exc.errors()}
        ).model_dump()
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content=APIResponse(
            success=False,
            message=exc.detail,
            error={"details": exc.detail}
        ).model_dump()
    )


@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content=APIResponse(
            success=False,
            message="Internal server error",
            error={"details": str(exc)}
        ).model_dump()
    )


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.include_router(book_router)