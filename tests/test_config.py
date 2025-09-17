import pytest
from app.config.settings import settings


def test_settings():
    # Test that settings are loaded correctly
    assert settings.ENVIRONMENT in ["dev", "test", "prod"]
    assert settings.DATABASE_URL is not None


def test_dev_environment():
    # Test that default environment is dev
    assert settings.ENVIRONMENT == "dev"