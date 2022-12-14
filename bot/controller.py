from bot.db.adapter import DatabaseAdapter
from bot.db.models import User


class Controller:
    def __init__(self, db: DatabaseAdapter):
        self.db = db

    async def sync_user(self, user_id: int) -> User:
        async with self.db.transaction():
            return await self.db.sync_user(user_id)

    async def authorize_user(self, user_id: int) -> None:
        async with self.db.transaction():
            await self.db.authorize_user(user_id)
