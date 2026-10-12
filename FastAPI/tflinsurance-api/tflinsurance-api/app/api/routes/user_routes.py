from fastapi import (APIRouter,Depends,HTTPException,Request,status)

from fastapi import APIRouter
from app.services.user_service import UserService
from app.schemas.user_schema import (UserCreate, UserUpdate,UserResponse)

router = APIRouter(prefix="/api/users", tags=["users"])


def get_user_services(request: Request) -> UserService:
    return request.app.state.user_service


@router.get("/")
def get_all_users(service: UserService = Depends(get_user_services)):
    users = service.get_all_users()

    return {
        "message": "users retrieved successfully",
        "count": len(users),
        "data": users
    }


# @router.get("/{policy_id}",response_model=userResponse)
# def get_policy(user_id: int,service: userResponse = Depends(get_user_services)
# ):
#     user = service.get_user(user_id)

#     if user is None:
#         raise HTTPException(
#             status_code=404,
#             detail="user not found"
#         )

#     return user


@router.post("/",status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def create_user(
    # user_id: UserCreate,
    user: UserCreate,
    service:UserService=Depends(get_user_services)
):
    try:
        return service.create_user(user)

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


# # @router.put("/{policy_id}", response_model=PolicyResponse)
# # def update_policy( policy_id: int,policy: PolicyUpdate,service: PolicyService = Depends(get_policy_service)):
# #     updated = service.update_policy( policy_id,policy.model_dump())

# #     if updated is None:
# #         raise HTTPException(status_code=404,detail="Policy not found")

# #     return updated


# @router.delete("/{user_id}")
# def delete_users(user_id: int,service: UserService = Depends(get_user_services)):
#     deleted = service.delete_user(user_id)

#     if deleted is None:
#         raise HTTPException(status_code=404,detail="user not found")

#     return {
#         "message": "user deleted successfully",
#         "deleted_user": deleted
#     }