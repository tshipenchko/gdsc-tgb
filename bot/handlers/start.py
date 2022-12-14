from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Text
from fluentogram import TranslatorRunner
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from bot.db.models import User
from bot.keyboards import add_menu

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, i18n: TranslatorRunner, session: AsyncSession):
    async with session.begin():
        await session.merge(
            User(id=message.from_user.id)
        )
        is_auth = await session.scalar(
            select(User.is_auth).where(User.id == message.from_user.id)
        )
    if is_auth:
        text = i18n.start()
    else:
        text = i18n.login()
    await message.answer(text, reply_markup=add_menu(is_auth))


@router.callback_query(Text("login"))
async def login(call, i18n: TranslatorRunner, session: AsyncSession):
    async with session.begin():
        await session.execute(
            update(User).where(User.id == call.from_user.id).values(is_auth=True)
        )
    await call.message.edit_text(i18n.start(), reply_markup=add_menu(is_auth=True))
