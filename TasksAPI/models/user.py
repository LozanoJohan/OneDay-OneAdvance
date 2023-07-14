from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: int = None
    name: str
    email: str
    password: str
    site: Optional[str] = None