from sqlalchemy.orm import Session
from app.domain.models import User

class UserRepository:
    def get_all_users(self, db: Session):
        """Fetch all users."""
        return db.query(User).all()

    def get_user_by_id(self, db: Session, user_id: int):
        """Fetch a user by ID."""
        return db.query(User).filter(User.id == user_id).first()

    def create_user(self, db: Session, user: User):
        """Create a new user."""
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def update_user(self, db: Session, user_id: int, updates: dict):
        """Update an existing user."""
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            for key, value in updates.items():
                setattr(user, key, value)
            db.commit()
            db.refresh(user)
        return user

    def delete_user(self, db: Session, user_id: int):
        """Delete a user by ID."""
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            db.delete(user)
            db.commit()
        return user
