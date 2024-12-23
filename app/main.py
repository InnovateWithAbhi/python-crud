from fastapi import FastAPI
from app.routers.user_router import router as user_router

app = FastAPI()

# Include your routers
app.include_router(user_router, prefix="/users", tags=["Users"])

@app.get("/")
async def root():
    return {"message": "Hello, FastAPI"}
