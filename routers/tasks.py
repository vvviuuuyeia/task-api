from fastapi import APIRouter, HTTPException, status
import data
from models import TaskCreate, TaskUpdate

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("")
def list_tasks(completed: bool | None = None):
    if completed is None:
        return data.tasks
    return [t for t in data.tasks if t["completed"] == completed]

@router.get("/{task_id}")
def get_one(task_id: int):
    task = data.find_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="任务不存在")
    return task

@router.post("", status_code=status.HTTP_201_CREATED)
def create(payload: TaskCreate):
    return data.create_task(payload)

@router.patch("/{task_id}")
def update(task_id: int, payload: TaskUpdate):
    task = data.update_task(task_id, payload)
    if task is None:
        raise HTTPException(status_code=404, detail="任务不存在")
    return task

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove(task_id: int):
    if not data.delete_task(task_id):
        raise HTTPException(status_code=404, detail="任务不存在")