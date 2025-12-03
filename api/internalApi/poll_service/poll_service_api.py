import httpx

from config.config import Config

config = Config()


async def delete_answers_for_user(user_id: int) -> None:
    url = f"{config.POLL_SERVICE_BASE_URL}/answer/user/{user_id}"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.delete(url)
            response.raise_for_status()
        except Exception as exc:
            print(f"Error deleting answers for user {user_id} from Poll Service: {exc}")
