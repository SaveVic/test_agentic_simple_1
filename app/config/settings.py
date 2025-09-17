from pydantic_settings import BaseSettings
from pydantic import ConfigDict
from typing import Literal


class Settings(BaseSettings):
    model_config = ConfigDict(env_file=".env")
    
    ENVIRONMENT: Literal["dev", "test", "prod"] = "dev"
    DATABASE_URL: str = "sqlite:///./books.db"


settings = Settings()