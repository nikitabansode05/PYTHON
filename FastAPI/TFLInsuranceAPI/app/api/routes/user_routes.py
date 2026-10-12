from fastapi import (APIRouter,Depends,HTTPException,Request,status)
from app.services.user_service import UserService

router=APIRouter(prefix="/api/user",tags=["Users"])

def get_user_service(request:Request)-> UserService:
    return request.app.state.user_service

@router.get("/")
def get_all_users(service:UserService=Depends(get_user_service)):
    users=service.get_all_users()
    return{
        "message":"Users retrieved successfully",
        "data":users
    }
    
@router.get("/{user_id}")
def get_user_by_id(user_id:int,service:UserService=Depends(get_user_service)):
    return service.get_user_by_id(user_id)