from typing import Dict, Any, Awaitable, Callable

from aiogram import BaseMiddleware
from aiogram.types import Update, User
from fluentogram import TranslatorHub


class TranslatorRunnerMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
            event: Update,
            data: Dict[str, Any]
    ) -> Any:
        hub: TranslatorHub = data.get("_translator_hub")
        from_user: User = data.get("event_from_user")

        data["i18n"] = hub.get_translator_by_locale(from_user.language_code)
        return await handler(event, data)
