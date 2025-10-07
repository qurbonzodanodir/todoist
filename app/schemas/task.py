from pydantic import BaseModel
import typing as t
from datetime import datetime
from app._shared.constants import TaskStatus,TaskPriority




class TaskRequest(BaseModel):
    name:str
    description: t.Optional[str] = None
    select_date: t.Optional[datetime] = None
    priority: t.Optional[TaskPriority] = None
    status: t.Optional[TaskStatus] = None


class TaskUpdateRequest(BaseModel):
    name: t.Optional[str] = None
    description: t.Optional[str] = None
    select_date: t.Optional[datetime] = None
    priority: t.Optional[TaskPriority] = None
    status: t.Optional[TaskStatus] = None



class TaskResponse(BaseModel):
    id:int
    name: t.Optional[str] = None
    description: t.Optional[str] = None
    select_date: t.Optional[datetime] = None
    priority: t.Optional[TaskPriority] = None
    status: t.Optional[TaskStatus] = None


