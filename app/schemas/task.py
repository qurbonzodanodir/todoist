from pydantic import BaseModel
import typing as t
from datetime import datetime





class TaskRequest(BaseModel):
    name:str
    description: t.Optional[str] = None
    select_date: t.Optional[datetime] = None
    priority: t.Optional[str] = None


class TaskUpdateRequest(BaseModel):
    name: t.Optional[str] = None
    description: t.Optional[str] = None
    select_date: t.Optional[datetime] = None
    priority: t.Optional[str] = None



class TaskResponse(BaseModel):
    name: t.Optional[str] = None
    description: t.Optional[str] = None
    select_date: t.Optional[datetime] = None
    priority: t.Optional[str] = None


