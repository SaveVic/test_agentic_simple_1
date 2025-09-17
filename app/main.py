from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.config.database import create_db_and_tables
from app.routes.books import router as books_router


app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.exception_handler(Exception)
async def validation_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=422,
        content={"success": False, "error": {"code": 422, "message": str(exc)}},
    )


app.include_router(books_router, prefix="/books", tags=["books"])