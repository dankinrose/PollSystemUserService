from datetime import date
from typing import Optional

from pydantic import BaseModel


class UserCreateRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    age: int
    address: Optional[str] = None
    join_date: date
