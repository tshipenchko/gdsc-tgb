from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from fluentogram import TranslatorRunner
from sqlalchemy.ext.asyncio import AsyncSession

from bot.db.models import User

router = Router()


@router.message(CommandStart())
async def start(message: Message, i18n: TranslatorRunner, session: AsyncSession):
    async with session.begin():
        await session.merge(
            User(id=message.from_user.id)
        )

    await message.answer(i18n.start())
