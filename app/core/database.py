from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# Database engine creation
engine = create_engine(settings.DATABASE_URL)

# Declarative base for SQLAlchemy models
Base = declarative_base()

# SessionLocal class for creating database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()