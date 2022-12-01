import logging
from pathlib import Path

from aiogram import Bot, Dispatcher
from fluent_compiler.bundle import FluentBundle
from fluentogram import TranslatorHub, FluentTranslator

from bot.config_reader import Settings
from bot.handlers import setup_routers
from bot.middlewares import setup_middlewares


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    config = Settings()
    locales_dir = Path(__file__).parent.joinpath("locales")
    translator_hub = TranslatorHub(  # FIXME: Find a better way to create a TranslatorHub
        {
            "en": ("en",),
            "ru": ("ru", "en"),
        },
        [
            FluentTranslator(
                "en", translator=FluentBundle.from_files("en", [str(locales_dir.joinpath("en", "main.ftl"))])
            ),
            FluentTranslator(
                "ru", translator=FluentBundle.from_files("ru", [str(locales_dir.joinpath("ru", "main.ftl"))])
            ),
        ],
    )

    # Setup bot
    bot = Bot(token=config.bot_token.get_secret_value())
    dp = Dispatcher()
    router = setup_routers()
    setup_middlewares(router)
    dp.include_router(router)

    # Prepare context data
    kwargs = {
        "config": config,
        "_translator_hub": translator_hub,
    }

    # Run bot
    try:
        # TODO: Add webhook support for production
        await bot.delete_webhook()
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types(), **kwargs)
    finally:
        await bot.session.close()
