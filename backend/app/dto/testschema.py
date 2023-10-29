from datetime import date, datetime
from pydantic import BaseModel
from typing import Dict, List, Union


class TestValid(BaseModel):
    list_answer: List[Dict[str, Union[int, str]]]
