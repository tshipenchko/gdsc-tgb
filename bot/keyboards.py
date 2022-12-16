from aiogram.utils.keyboard import InlineKeyboardBuilder
from fluentogram import TranslatorRunner


def add_menu(is_auth: bool, i18n: TranslatorRunner):
    kb = InlineKeyboardBuilder()
    if not is_auth:
        kb.button(text=i18n.login_btn(), callback_data="login")
    else:
        kb.button(text=i18n.profile_btn(), callback_data="profile")
        kb.button(text=i18n.events_btn(), callback_data="events")
        kb.button(text=i18n.info_btn(), callback_data="info")
        kb.adjust(1, 2)

    return kb.as_markup()


def add_back_btn(i18n: TranslatorRunner):
    kb = InlineKeyboardBuilder()
    kb.button(text=i18n.back_to_menu_btn(), callback_data="menu")

    return kb.as_markup()
