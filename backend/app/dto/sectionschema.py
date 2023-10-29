from datetime import date, datetime
from pydantic import BaseModel
from typing import List


class SectionId(BaseModel):
    list_id: List[int]
    time: int
    id_user: int
