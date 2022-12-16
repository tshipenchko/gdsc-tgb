from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Text
from fluentogram import TranslatorRunner

from bot.keyboards import add_menu, add_back_btn
from bot.controller import Controller

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, i18n: TranslatorRunner, controller: Controller):
    user = await controller.sync_user(message.from_user.id)

    if user.is_auth:
        text = i18n.start()
    else:
        text = i18n.login_text()

    await message.answer(text, reply_markup=add_menu(is_auth=user.is_auth, i18n=i18n))


@router.callback_query(Text("login"))
async def login(call: CallbackQuery, i18n: TranslatorRunner, controller: Controller):
    await controller.authorize_user(call.from_user.id)
    await call.answer(i18n.login_success(), show_alert=True)
    await call.message.edit_text(i18n.start(), reply_markup=add_menu(is_auth=True, i18n=i18n))


@router.callback_query(Text("profile"))
async def profile(call: CallbackQuery, i18n: TranslatorRunner, controller: Controller):
    await call.message.edit_text(i18n.profile_text(), reply_markup=add_back_btn(i18n=i18n))


@router.callback_query(Text("events"))
async def profile(call: CallbackQuery, i18n: TranslatorRunner, controller: Controller):
    await call.message.edit_text(i18n.events_text(), reply_markup=add_back_btn(i18n=i18n))


@router.callback_query(Text("info"))
async def profile(call: CallbackQuery, i18n: TranslatorRunner, controller: Controller):
    await call.message.edit_text(i18n.info_text(), reply_markup=add_back_btn(i18n=i18n))


@router.callback_query(Text("menu"))
async def menu(call: CallbackQuery, i18n: TranslatorRunner, controller: Controller):
    await call.message.edit_text(i18n.start(), reply_markup=add_menu(is_auth=True, i18n=i18n))
