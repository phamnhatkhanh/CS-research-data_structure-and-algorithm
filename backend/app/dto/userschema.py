from datetime import date, datetime
from pydantic import BaseModel
from typing import Optional


class RegisterUser(BaseModel):
    name: str
    email: str
    password: str
    date_of_birth: Optional[date]
    verify_at: Optional[datetime]
    verify: Optional[bool]
