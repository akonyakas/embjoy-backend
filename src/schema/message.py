from pydantic import BaseModel


class MessageBase(BaseModel):
    content: str


class MessageCreate(MessageBase):
    sender_id: int
    receiver_id: int


class MessageOut(MessageBase):
    id: int
    sender_id: int
    receiver_id: int

    class Config:
        orm_mode = True
