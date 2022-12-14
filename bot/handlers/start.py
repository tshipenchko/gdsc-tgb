from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Text
from fluentogram import TranslatorRunner

from bot.keyboards import add_menu
from bot.controller import Controller

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, i18n: TranslatorRunner, controller: Controller):
    user = await controller.sync_user(message.from_user.id)

    if user.is_auth:
        text = i18n.start()
    else:
        text = i18n.login()

    await message.answer(text, reply_markup=add_menu(is_auth=user.is_auth))


@router.callback_query(Text("login"))
async def login(call: CallbackQuery, i18n: TranslatorRunner, controller: Controller):
    await controller.authorize_user(call.from_user.id)
    await call.answer(i18n.login_success(), show_alert=True)
    await call.message.edit_text(i18n.start(), reply_markup=add_menu(is_auth=True))
