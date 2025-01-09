from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

from app.db.database import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    userId = Column(UUID(as_uuid=True), default=uuid4, unique=True, index=True)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    mobileNumber = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    createdOn = Column(DateTime, default=datetime.utcnow)
    updatedOn = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    isActive = Column(Boolean, default=True)
