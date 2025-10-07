from fastapi import FastAPI
from app.routers.task import router as task_router
from app.routers.category import router as category_router

app = FastAPI()


app.include_router(task_router,prefix="/api")
app.include_router(category_router,prefix="/api")