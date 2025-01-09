from sqlalchemy.orm import Session
from app.domain.models import User
from app.repositories.user_repository import UserRepository

class UserUseCase:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def get_all_users(self, db: Session):
        """Fetch all users."""
        return self.repository.get_all_users(db)

    def get_user_by_id(self, db: Session, user_id: int):
        """Fetch a user by ID."""
        return self.repository.get_user_by_id(db, user_id)

    def create_user(self, db: Session, user_data: dict):
        """Create a new user."""
        user = User(**user_data)
        return self.repository.create_user(db, user)

    def update_user(self, db: Session, user_id: int, updates: dict):
        """Update an existing user."""
        updated_user = self.repository.update_user(db, user_id, updates)
        return updated_user

    def delete_user(self, db: Session, user_id: int):
        """Delete a user."""
        deleted_user = self.repository.delete_user(db, user_id)
        return deleted_user
