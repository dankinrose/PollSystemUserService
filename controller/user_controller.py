from typing import List
from fastapi import APIRouter, HTTPException
from starlette import status
from model.user_create_request import UserCreateRequest
from model.user import User
from service import user_service

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.get("/all", response_model=List[User])
async def get_all_users() -> List[User]:
    return await user_service.get_all_users()


@router.get("/{user_id}", response_model=User)
async def get_user_by_id(user_id: int) -> User:
    user = await user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found"
        )
    return user


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=User)
async def create_user(request: UserCreateRequest) -> User:
    return await user_service.create_user(request)




@router.put("/{user_id}", response_model=User)
async def update_user(user_id: int, user: User):
    updated_user = await user_service.update_user(user_id, user)

    if not updated_user:
        raise HTTPException(
            status_code=404,
            detail=f"Can't update user with id: {user_id}, user not found"
        )
    return updated_user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int):
    success = await user_service.delete_user(user_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found"
        )
    return


@router.put("/register/{user_id}", response_model=User)
async def register_user(user_id: int):
    registered_user = await user_service.register_user(user_id)
    if not registered_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found or cannot register"
        )
    return registered_user
