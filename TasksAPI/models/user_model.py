from pydantic import BaseModel
from typing import Optional
from .task_model import Task

class User(BaseModel):
    id: int = None
    name: str
    email: str
    password: str
    site: Optional[str] = None
    tasks: Optional[list[Task]] = []