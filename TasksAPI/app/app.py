from fastapi import FastAPI

from app.routers.tasks_router import router as tasks_router
from app.routers.users_router import router as users_router


app = FastAPI()
app.include_router(tasks_router)
app.include_router(users_router)