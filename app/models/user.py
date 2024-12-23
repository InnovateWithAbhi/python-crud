from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP
from app.core.database import Base

class User(Base):
    __tablename__ = "tblusers"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, index=True, nullable=False)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    phone_number = Column(String(255), unique=True, index=True, nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    created_on = Column(TIMESTAMP, default=datetime.now)
    updated_on = Column(TIMESTAMP, default=datetime.now)

    # Relationships (if applicable)
    # Example:
    # items = relationship("Item", back_populates="owner")