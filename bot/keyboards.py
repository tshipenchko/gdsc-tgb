from aiogram.utils.keyboard import InlineKeyboardBuilder


def add_menu(is_auth: bool):
    kb = InlineKeyboardBuilder()
    if not is_auth:
        kb.button(text="Login", callback_data="login")
    else:
        kb.button(text="Profile", callback_data="profile")
        kb.button(text="Events", callback_data="events")
        kb.button(text="Info", callback_data="info")
        kb.adjust(1, 2)

    return kb.as_markup()
