"""Application ORM configuration."""

from __future__ import annotations

from advanced_alchemy.base import AuditColumns, orm_registry
from advanced_alchemy.base import UUIDAuditBase as TimestampedDatabaseModel
from advanced_alchemy.base import UUIDBase as DatabaseModel

__all__ = ["DatabaseModel", "TimestampedDatabaseModel", "orm_registry", "AuditColumns"]
