import os
from typing import Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENVIRONMENT: str = "dev"
    DATABASE_URL: str = "sqlite:///./books.db"

    class Config:
        env_file = ".env"


settings = Settings()