import uuid
from datetime import UTC, datetime

from fastapi import APIRouter
from app.schemas.todo import TodoCreate, TodoRead, TodoUpdate
from app.core import exceptions

router = APIRouter()


todos: list[TodoRead] = []


class TodoRepository:
    @staticmethod
    @router.post("/todos", response_model=TodoRead)
    async def create_todo(todo_in: TodoCreate):
        todo = TodoRead(**todo_in.model_dump())
        todos.append(todo)
        return todo

    @staticmethod
    @router.get("/todos", response_model=list[TodoRead])
    async def list_todos():
        return todos

    @staticmethod
    @router.patch("/todos/{todo_id}", response_model=TodoRead)
    async def update_todo(todo_id: uuid.UUID, todo_in: TodoUpdate):
        for todo in todos:
            if todo.id == todo_id:
                update_data = todo_in.model_dump(exclude_unset=True)
                for key, value in update_data.items():
                    setattr(todo, key, value)
                # actualizar solo el modified_at
                todo.modified_at = datetime.now(UTC)
                return todo
        raise exceptions.TODO_404_NOT_FOUND

    @staticmethod
    @router.delete("/todos/{todo_id}", status_code=204)
    async def delete_todo(todo_id: uuid.UUID):
        for idx, todo in enumerate(todos):
            if todo.id == todo_id:
                todos.pop(idx)
                return
        raise exceptions.TODO_404_NOT_FOUND
