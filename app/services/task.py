from sqlalchemy.orm import Session
from app.repositories.task import TaskPepository
from app.schemas.task import TaskRequest,TaskUpdateRequest



class TaskService:
    def __init__(self,db:Session):
        self.repo = TaskPepository(db)

    def list_tasks(self):
        return self.repo.get_all()
    
    def get_task(self,task_id: int):
        return self.repo.get_by_id(task_id)
    
    def create_task(self, data: TaskRequest):
        return self.repo.create(data)
    
    def update(self,task_id: int, data: TaskUpdateRequest):
        return self.repo.update(task_id,data)
    
    def delete(self,task_id: int):
        return self.repo.delete(task_id)