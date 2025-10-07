from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app._core.database import get_db
from app.models.task import *
from app.schemas.task import *
from app.services.task import TaskService


router = APIRouter(prefix="/task", tags=["Taks"])


@router.get("/",response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    return TaskService(db).list_tasks()

@router.post("/",response_model=TaskResponse)
def create_task(task_data: TaskRequest, db : Session = Depends(get_db)):
    return TaskService(db).create_task(task_data)


@router.get("/{task_id}",response_model=TaskResponse)
def get_task(task_id:int, db: Session = Depends(get_db)):
    task = TaskService(db).get_task(task_id)
    if not task:
        raise HTTPException(status_code=404,detail="Task not found")
    return task


@router.put("/{task_id}",response_model=TaskResponse)
def update_task(task_id:int,task_data:TaskUpdateRequest,db: Session = Depends(get_db)):
    task = TaskService(db).update(task_id,task_data)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.delete("/{task_id}")
def delete_task(task_id: int,db: Session = Depends(get_db)):
    task = TaskService(db).delete(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return{"detail": "Task deleted"}



