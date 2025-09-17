import os
from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    
    ENVIRONMENT: str = "dev"
    DATABASE_URL: str = "sqlite:///./books.db"


settings = Settings()