from litestar.types import ControllerRouterHandler

from app.domain import todoitem, system, plugins, openapi

routes: list[ControllerRouterHandler] = [
    todoitem.controllers.TodoItemController,
    system.controllers.SystemController
]

__all__ = [
    "todoitem",
    "system",
    "plugins",
    "openapi"
]
