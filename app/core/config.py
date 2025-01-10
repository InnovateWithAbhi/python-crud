from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:579394@localhost:5433/pythonCrud"

    class Config:
        env_file = ".env"

settings = Settings()
