from pydantic import BaseModel
from typing import List


class Donor(BaseModel):
    id: int
    name: str
    age: int
    blood_type: str
    health_conditions: List[str]
