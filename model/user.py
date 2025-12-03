from datetime import date
from typing import Optional

from pydantic import BaseModel

class User(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: str
    email: str
    age: int
    address: Optional[str] = None
    join_date: date
    is_registered: bool = False
