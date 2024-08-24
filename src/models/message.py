from sqlalchemy import Column, Integer, ForeignKey, Date, JSON, DateTime, String, Boolean
from sqlalchemy.sql import func
from src.core.database import Base


class Message(Base):
    __tablename__ = "journals"

    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey("users.id"))
    receiver_id = Column(Integer, ForeignKey("users.id"))
    content = Column(String)
    timestamp = Column(DateTime, default=func.now())
    is_read = Column(Boolean, default=False)
