from sqlalchemy.orm import Session
from app.repositories.category import CategoryRepository
from app.schemas.category import CategoryRequest,CategoryUpdateRequest


class CategoryService:
    def __init__(self,db:Session):
        self.repo = CategoryRepository(db)

    def list_categories(self):
        return self.repo.get_all()
    
    def get_category(self, category_id:int):
        return self.repo.get_by_id(category_id)
    
    def create(self,data:CategoryRequest):
        return self.repo.create(data)
    
    def update(self,category_id:int,data:CategoryUpdateRequest):
        return self.repo.update(category_id,data)
    
    def delete(self,category_id):
        return self.repo.delete(category_id)