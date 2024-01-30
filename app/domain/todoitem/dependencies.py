from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import select

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator
    from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.todoitem.services import TodoItemService
from app.domain.todoitem.models import TodoItem

__all__ = ["provide_todo_item_service"]


async def provide_todo_item_service(
        db_session: AsyncSession | None = None
) -> AsyncGenerator[TodoItemService, None]:
    """Provide TodoItem Service."""

    async with TodoItemService.new(session=db_session,
                                   statement=select(TodoItem)) as service:
        yield service
