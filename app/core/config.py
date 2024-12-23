from typing import Optional

class Settings:
    # Database connection details
    DATABASE_URL: str = "postgresql://postgres:admin@localhost:5432/postgres"  # Replace with your actual credentials
    TEST_DATABASE_URL: Optional[str] = None  # Optional URL for testing environment

    # Secret key for generating tokens (replace with a random string)
    SECRET_KEY: str = "a7e41175debf03cded041bc58d44819c02be94515cf0dcf24992e151d49c2aeb"

    # Algorithm used for hashing passwords
    ALGORITHM: str = "HS256"  # Consider using a more secure algorithm like argon2

    # Access token expiration time (in minutes)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Additional configurations (if needed)
    # ...

settings = Settings()