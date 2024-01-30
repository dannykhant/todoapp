from advanced_alchemy.extensions.litestar.dto import SQLAlchemyDTO

from app.lib import dto

from app.domain.todoitem.models import TodoItem

__all__ = ["TodoItemDTO", "TodoItemCreateDTO", "TodoItemUpdateDTO"]


class TodoItemDTO(SQLAlchemyDTO[TodoItem]):
    config = dto.config(max_nested_depth=0)


class TodoItemCreateDTO(SQLAlchemyDTO[TodoItem]):
    config = dto.config(max_nested_depth=0, exclude={"id", "created_at", "updated_at"})


class TodoItemUpdateDTO(SQLAlchemyDTO[TodoItem]):
    config = dto.config(max_nested_depth=0, exclude={"id", "created_at", "updated_at"}, partial=True)
