from typing import Optional, List

from repository.database import database
from model.user import User


async def get_user_by_id(user_id: int) -> Optional[User]:
    query = "SELECT * FROM user WHERE id = :user_id"
    row = await database.fetch_one(query=query, values={"user_id": user_id})
    return User(**row) if row else None



async def get_all_users() -> List[User]:
    query = "SELECT * FROM user"
    rows = await database.fetch_all(query=query)
    return [User(**r) for r in rows]



async def create_user(user: User) -> int:
    query = """
    INSERT INTO user (first_name, last_name, email, age, address, join_date, is_registered)
    VALUES (:first_name, :last_name, :email, :age, :address, :join_date, :is_registered)
    """

    values = {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "age": user.age,
        "address": user.address,
        "join_date": user.join_date,
        "is_registered": user.is_registered,
    }

    last_id = await database.execute(query=query, values=values)
    return last_id



async def update_user(user: User) -> None:
    query = """
    UPDATE user
    SET first_name = :first_name,
        last_name = :last_name,
        email = :email,
        age = :age,
        address = :address,
        join_date = :join_date,
        is_registered = :is_registered
    WHERE id = :id
    """

    values = {
        "id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "age": user.age,
        "address": user.address,
        "join_date": user.join_date,
        "is_registered": user.is_registered,
    }

    await database.execute(query=query, values=values)



async def delete_user(user_id: int) -> None:
    query = "DELETE FROM user WHERE id = :user_id"
    await database.execute(query=query, values={"user_id": user_id})



async def register_existing_user(user_id: int, is_registered: bool) -> None:
    query = """
    UPDATE user
    SET is_registered = :is_registered
    WHERE id = :user_id
    """
    values = {
        "user_id": user_id,
        "is_registered": is_registered,
    }
    await database.execute(query=query, values=values)