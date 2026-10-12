from fastapi import FastAPI

from app.api.routes.policy_routes import router as policy_router
from app.api.routes.user_routes import router as user_router
from app.repositories.policy_repository import PolicyRepository
from app.services.policy_service import PolicyService
from app.services.user_service import UserService
from app.repositories.user_repository import UserRepository

app=FastAPI(title="TFlInsurance API",description="Insurance Policy Management REST API",version="1.0")

policy_repository=PolicyRepository()
app.state.policy_service=PolicyService(policy_repository)

user_repository=UserRepository()
app.state.user_service=UserService(user_repository)

app.include_router(policy_router)
app.include_router(user_router)


@app.get("/")
def home():
    return{
        "application":"TFLInsurance",
        "message":"Welcome to TFLInsurance REST API",
        "docs":"/docs"
    }
