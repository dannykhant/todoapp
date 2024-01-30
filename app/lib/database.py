"""Database configuration."""

from __future__ import annotations

from typing import TYPE_CHECKING

from advanced_alchemy.extensions.litestar.plugins.init.config import SQLAlchemyAsyncConfig
from advanced_alchemy.extensions.litestar.plugins.init.config.asyncio import autocommit_before_send_handler
from advanced_alchemy.extensions.litestar.plugins.init.plugin import SQLAlchemyInitPlugin
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.pool import NullPool

from app.lib import constants, settings

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

DB_USER = settings.db.USER
DB_PASSWORD = settings.db.PASSWORD
DB_HOST = settings.db.HOST
DB_PORT = settings.db.PORT
DB_NAME = settings.db.NAME

if DB_USER and DB_PASSWORD and DB_HOST and DB_PORT and DB_NAME:
    DB_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
else:
    DB_URL = settings.db.url

engine = create_async_engine(
    DB_URL,
    future=True,
    echo=settings.db.ECHO,
    echo_pool=True if settings.db.ECHO_POOL == "debug" else settings.db.ECHO_POOL,
    max_overflow=settings.db.POOL_MAX_OVERFLOW,
    pool_size=settings.db.POOL_SIZE,
    pool_timeout=settings.db.POOL_TIMEOUT,
    pool_recycle=settings.db.POOL_RECYCLE,
    pool_pre_ping=settings.db.POOL_PRE_PING,
    pool_use_lifo=True,  # use lifo to reduce the number of idle connections
    poolclass=NullPool if settings.db.POOL_DISABLE else None,
    connect_args=settings.db.CONNECT_ARGS,
)
async_session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(engine, expire_on_commit=False)
"""Database session factory.

See [`async_sessionmaker()`][sqlalchemy.ext.asyncio.async_sessionmaker].
"""

config = SQLAlchemyAsyncConfig(
    session_dependency_key=constants.DB_SESSION_DEPENDENCY_KEY,
    engine_instance=engine,
    session_maker=async_session_factory,
    before_send_handler=autocommit_before_send_handler,
)

plugin = SQLAlchemyInitPlugin(config=config)
