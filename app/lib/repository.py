"""Repository pattern helpers."""

from __future__ import annotations

from typing import TYPE_CHECKING

from advanced_alchemy.repository import SQLAlchemyAsyncRepository
from litestar.repository.handlers import on_app_init as _on_app_init

if TYPE_CHECKING:
    from litestar.config.app import AppConfig
__all__ = ["SQLAlchemyAsyncRepository", "on_app_init"]


def on_app_init(app_config: "AppConfig") -> "AppConfig":
    """Executes on application init.  Injects signature namespaces."""
    app_config.signature_namespace.update(
        {
            "SQLAlchemyAsyncRepository": SQLAlchemyAsyncRepository,
        },
    )
    return _on_app_init(app_config)
