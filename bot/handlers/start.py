from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from fluentogram import TranslatorRunner

router = Router()


@router.message(CommandStart())
async def start(message: Message, i18n: TranslatorRunner):
    await message.answer(i18n.start())
