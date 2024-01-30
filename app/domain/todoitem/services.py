from __future__ import annotations

from app.lib.repository import SQLAlchemyAsyncRepository
from app.lib.service import SQLAlchemyAsyncRepositoryService

from app.domain.todoitem.models import TodoItem

__all__ = ["TodoItemService", "TodoItemRepository"]


class TodoItemRepository(SQLAlchemyAsyncRepository[TodoItem]):
    """TodoItem repository."""

    model_type = TodoItem


class TodoItemService(SQLAlchemyAsyncRepositoryService[TodoItem]):
    """For the basic operations of TodoItem."""

    repository_type = TodoItemRepository
