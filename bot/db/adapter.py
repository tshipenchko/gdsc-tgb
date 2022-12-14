from sqlalchemy.ext.asyncio import AsyncSession, AsyncSessionTransaction
from sqlalchemy import select, update, delete, insert  # noqa: F401 Basic SQL queries for SQLAlchemy

from bot.db.models import User


class DatabaseAdapter:
    def __init__(self, session: AsyncSession):
        self.session = session

    def transaction(self) -> AsyncSessionTransaction:
        """
        Creates a new transaction
        :return: transaction object
        """
        return self.session.begin()

    async def sync_user(self, user_id: int) -> User:
        """
        Creates a new user in the database if it does not exist and returns it
        :param user_id: telegram user id
        :return: user object
        """
        return await self.session.merge(User(id=user_id))

    async def authorize_user(self, user_id: int) -> None:
        """
        Authorizes user
        :param user_id: telegram user id
        :return: None
        """
        await self.session.execute(
            update(User).where(User.id == user_id).values(is_auth=True)
        )
