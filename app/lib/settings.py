"""App wide settings."""

from __future__ import annotations

import os
from functools import lru_cache
from pathlib import Path
from typing import Any, Literal

from dotenv import load_dotenv
from pydantic import ValidationError
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)

__all__ = ["db"]


class DatabaseSettings(BaseSettings):
    """Configures the database for the application."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="DB_",
        case_sensitive=False,
    )

    ECHO: bool = False
    """Enable SQLAlchemy engine logs."""
    ECHO_POOL: bool | Literal["debug"] = False
    """Enable SQLAlchemy connection pool logs."""
    POOL_DISABLE: bool = False
    """Disable SQLAlchemy pooling, same as setting pool to.

    [`NullPool`][sqlalchemy.pool.NullPool].
    """
    POOL_MAX_OVERFLOW: int = 10
    """See [`max_overflow`][sqlalchemy.pool.QueuePool]."""
    POOL_SIZE: int = 5
    """See [`pool_size`][sqlalchemy.pool.QueuePool]."""
    POOL_TIMEOUT: int = 30
    """See [`timeout`][sqlalchemy.pool.QueuePool]."""
    POOL_RECYCLE: int = 300
    POOL_PRE_PING: bool = False
    CONNECT_ARGS: dict[str, Any] = {}
    URL: str = f"postgresql+asyncpg://default:default@localhost:5432/todoapp"
    ENGINE: str | None = None
    USER: str | None = None
    PASSWORD: str | None = None
    HOST: str | None = None
    PORT: int | None = None
    NAME: str | None = None


@lru_cache
def load_settings() -> DatabaseSettings:
    env_file = Path(f"{os.curdir}/.env")
    if env_file.is_file():
        load_dotenv(env_file)

    try:
        """Override Application reload dir."""
        database: DatabaseSettings = DatabaseSettings()
    except ValidationError as e:
        print("Could not load settings.", e)  # noqa: T201
        raise

    return database


db = load_settings()
