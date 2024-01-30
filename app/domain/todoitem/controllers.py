from __future__ import annotations

from typing import Annotated

from litestar import Controller, get, post, patch, delete
from litestar.di import Provide
from litestar.dto import DTOData
from litestar.params import Dependency, Parameter
from litestar.pagination import OffsetPagination

from app.domain.todoitem.dependencies import provide_todo_item_service
from app.domain.todoitem.dtos import TodoItemDTO, TodoItemCreateDTO, TodoItemUpdateDTO
from app.domain.todoitem.services import TodoItemService
from app.domain.todoitem.models import TodoItem
from uuid import UUID

from advanced_alchemy.filters import FilterTypes

__all__ = ["TodoItemController"]


class TodoItemController(Controller):
    """To handle TodoItem object."""

    dependencies = {"todo_item_service": Provide(provide_todo_item_service)}
    signature_namespace = {
        "Dependency": Dependency,
        "Parameter": Parameter,
    }
    return_dto = TodoItemDTO
    tags = ["TodoItem"]

    @get(path="/items",
         operation_id="ListTodoItems",
         name="TodoItem:list",
         summary="To retrieve a list of the items.", )
    async def list_items(self,
                         todo_item_service: TodoItemService,
                         filters: Annotated[list[FilterTypes], Dependency(skip_validation=True)],
                         ) -> OffsetPagination[TodoItem]:
        """List the items."""

        print(*filters)

        db_obj, count = await todo_item_service.list_and_count(*filters)
        return todo_item_service.to_dto(db_obj, count, *filters)

    @get(path="/items/{item_id:uuid}",
         operation_id="GetTodoItem",
         name="TodoItem:get",
         summary="To retrieve the details of the item.")
    async def get_item(self,
                       todo_item_service: TodoItemService,
                       item_id: Annotated[
                           UUID,
                           Parameter(
                               title="item_id",
                               description="The item to retrieve."
                           )
                       ]
                       ) -> TodoItem:
        """Get the item details."""

        db_obj = await todo_item_service.get(item_id)
        return todo_item_service.to_dto(db_obj)

    @post(path="/items",
          operation_id="CreateTodoItem",
          name="TodoItem:create",
          summary="To create an item.",
          dto=TodoItemCreateDTO)
    async def create_item(self,
                          todo_item_service: TodoItemService,
                          data: DTOData[TodoItem],
                          ) -> TodoItem:
        """Create an item."""

        db_obj = await todo_item_service.create(data.create_instance())
        return todo_item_service.to_dto(db_obj)

    @patch(path="/items/{item_id:uuid}",
           operation_id="UpdateTodoItem",
           name="TodoItem:update",
           summary="To update an item.",
           dto=TodoItemUpdateDTO)
    async def update_item(self,
                          todo_item_service: TodoItemService,
                          data: DTOData[TodoItem],
                          item_id: Annotated[
                              UUID,
                              Parameter(
                                  title="item_id",
                                  description="The item to update."
                              )
                          ],
                          ) -> TodoItem:
        """Update the item."""

        db_obj = await todo_item_service.update(item_id=item_id, data=data.create_instance())
        return todo_item_service.to_dto(db_obj)

    @delete(path="/items/{item_id:uuid}",
            operation_id="DeleteTodoItem",
            name="TodoItem:delete",
            summary="To delete an item.")
    async def delete_item(self,
                          todo_item_service: TodoItemService,
                          item_id: Annotated[
                              UUID,
                              Parameter(
                                  title="item_id",
                                  description="The item to delete."
                              )
                          ]
                          ) -> None:
        """Delete the item."""
        _ = await todo_item_service.delete(item_id)
