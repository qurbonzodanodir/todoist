from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app._core.database import get_db
from app.models.category import *
from app.schemas.category import *
from app.services.category import CategoryService



router = APIRouter(prefix="/category",tags=["Categories"])


@router.get("/", response_model=list[CategoryResponse])
def get_categories(db: Session = Depends(get_db)):
    return CategoryService(db).list_categories()

@router.get("/{category_id}",response_model=CategoryResponse)
def get_category(category_id: int, db:Session = Depends(get_db)):
    category = CategoryService(db).get_category(category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.post("/",response_model=CategoryResponse)
def create_category(data:CategoryRequest, db:Session = Depends(get_db)):
    return CategoryService(db).create(data)


@router.put("/{category_id}",response_model=CategoryResponse)
def update_category(category_id:int, data:CategoryUpdateRequest, db:Session = Depends(get_db)):
    category = CategoryService(db).update(category_id,data)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.delete("/{category_id}")
def delete_category(category_id:int, db:Session = Depends(get_db)):
    category = CategoryService(db).delete(category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

