import typing  as t
from pydantic import BaseModel

class CategoryRequest(BaseModel):
    name: str
    parent_id: t.Optional[int] = None


class CategoryUpdateRequest(BaseModel):
    name: t.Optional[str] = None
    parent_id: t.Optional[int] = None



class CategoryResponse(BaseModel):
    id: int
    name: t.Optional[str] = None
    parent_id: t.Optional[int] = None