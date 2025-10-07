from sqlalchemy.orm import Session
from app.schemas.category import CategoryRequest,CategoryUpdateRequest
from app.models.category import Category


class CategoryRepository:
    def __init__(self, db:Session):
        self.db = db
        

    def get_all(self):
        return self.db.query(Category).all()
    
    def get_by_id(self,category_id:int):
        return self.db.query(Category).filter(Category.id == category_id).first()
    

    def create(self, category_data: CategoryRequest):
        category = Category(**category_data.dict())
        self.db.add(category)
        self.db.commit()
        self.db.refresh(category)
        return category
    
    def update(self, category_id:int, category_data: CategoryUpdateRequest):
        category = self.get_by_id(category_id)
        if not category:
            return None
        
        for field,value in category_data.dict(exclude_unset=True).items():
            setattr(category, field, value)
        self.db.commit()
        self.db.refresh(category)
        return category
    

    def delete(self,category_id:int):
        category = self.get_by_id(category_id)
        if category:
            self.db.delete(category)
            self.db.commit()
        return category



