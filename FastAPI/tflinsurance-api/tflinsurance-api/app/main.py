from fastapi import FastAPI

from app.api.routes.user_routes import router as user_router
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService


app = FastAPI(
    title="TFLInsurance API",
    description="Insurance Policy Management REST API",
    version="1.0"
)

# Create shared application dependencies
repository = UserRepository()
app.state.user_service = UserService(repository)

# Register API routes
app.include_router(user_router)


@app.get("/")
def home():
    return {
        "application": "TFLInsurance",
        "message": "Welcome to TFLInsurance REST API",
        "docs": "/docs"
    }