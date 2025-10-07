from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskRequest,TaskUpdateRequest



class TaskPepository:
    def __init__(self,db:Session):
        self.db = db

    
    def get_all(self):
        return self.db.query(Task).all()
    
    def get_by_id(self,task_id:int):
        return self.db.query(Task).filter(Task.id == task_id).first()
    

    def create(self, task_data: TaskRequest):
        task = Task(**task_data.dict())
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task
    

    def update(self, task_id:int, task_data:TaskUpdateRequest):
        task = self.get_by_id(task_id)
        if not task:
            return None
        
        for field,value in task_data.dict(exclude_unset=True).items():
            setattr(task, field, value)
        self.db.commit()
        self.db.refresh(task)
        return task
    
    def delete(self, task_id:int):
        task = self.get_by_id(task_id)
        if task:
            self.db.delete(task)
            self.db.commit()
        return task
