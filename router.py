from fastapi import APIRouter, Depends
from typing import Annotated
from schemas import STaskAdd, STask, STaskId
from repository import TaskRepository

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)

@router.post("")
async def add_task(task: Annotated[STaskAdd, Depends()]) -> STaskId:

    task_id = await TaskRepository.add_one(task)
    return {"message": "Task added successfully", "task_id": task_id}

@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks