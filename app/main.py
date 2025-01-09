from fastapi import FastAPI
from app.controllers.user_controller import router
from app.db.database import Base, engine

app = FastAPI(title="User CRUD API")

# Initialize database
Base.metadata.create_all(bind=engine)

# Register routers
app.include_router(router, prefix="/users", tags=["Users"])
