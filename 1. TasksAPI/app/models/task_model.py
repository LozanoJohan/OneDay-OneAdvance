from pydantic import BaseModel
from typing import Union

class Task(BaseModel):
    id: int
    name: str
    description: str
    completion_status: bool
    priority: Union[int, None] = None
