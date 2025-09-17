from pydantic_settings import BaseSettings
from typing import Literal


class Settings(BaseSettings):
    ENVIRONMENT: Literal["dev", "test", "prod"] = "dev"
    DATABASE_URL: str = "sqlite:///./books.db"

    class Config:
        env_file = ".env"


settings = Settings()