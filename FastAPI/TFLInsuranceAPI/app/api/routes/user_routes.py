from fastapi import (APIRouter,Depends,HTTPException,Request,status)
from app.services.user_service import UserService

router=APIRouter(prefix="api/user",tags=["Users"])

def get_user_service(request:Request)-> UserService:
    return request.app.state.user_service

