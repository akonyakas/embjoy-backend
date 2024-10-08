from pydantic import BaseModel
from typing import List, Dict


class JournalBase(BaseModel):
    data: List[Dict[str, str]]


class JournalCreate(JournalBase):
    pass


class JournalResponse(JournalBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True


class JournalOut(JournalBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True
