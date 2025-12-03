from typing import Optional, List

from model.user import User
from model.user_create_request import UserCreateRequest
from repository import user_repository
from api.internalApi.poll_service.poll_service_api import delete_answers_for_user



async def get_user_by_id(user_id: int) -> Optional[User]:
    return await user_repository.get_user_by_id(user_id)



async def get_all_users() -> List[User]:
    return await user_repository.get_all_users()



async def create_user(request: UserCreateRequest) -> User:

    user = User(
        id=None,
        first_name=request.first_name,
        last_name=request.last_name,
        email=request.email,
        age=request.age,
        address=request.address,
        join_date=request.join_date,
        is_registered=False,
    )

    new_id = await user_repository.create_user(user)
    created_user = await user_repository.get_user_by_id(new_id)
    return created_user



async def update_user(user_id: int, user: User) -> Optional[User]:
    existing = await user_repository.get_user_by_id(user_id)
    if not existing:
        return None

    user.id = user_id
    await user_repository.update_user(user)
    updated = await user_repository.get_user_by_id(user_id)
    return updated



async def delete_user(user_id: int) -> bool:
    existing = await user_repository.get_user_by_id(user_id)
    if not existing:
        return False

    try:
        await delete_answers_for_user(user_id)
    except Exception as exc:
        print(f"Error deleting answers for user {user_id} from Poll Service: {exc}")

    await user_repository.delete_user(user_id)
    return True



async def register_user(user_id: int) -> Optional[User]:
    existing_user = await user_repository.get_user_by_id(user_id)
    if not existing_user:
        return None

    await user_repository.register_existing_user(user_id=user_id, is_registered=True)
    registered_user = await user_repository.get_user_by_id(user_id)
    return registered_user
