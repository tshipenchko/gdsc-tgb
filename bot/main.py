import logging
from pathlib import Path

from aiogram import Bot, Dispatcher

from bot.config_reader import Settings
from bot.handlers import setup_routers
from bot.middlewares import setup_middlewares
from bot.translator import generate_hub
from bot.db import create_session_maker, create_engine


async def main():
    # Setup logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    # Setup dependencies
    config = Settings()

    locales_dir = Path(__file__).parent.joinpath("locales")
    translator_hub = generate_hub(locales_dir, config.root_locale)

    engine = create_engine(config.db_url)
    session_maker = create_session_maker(engine)

    # Setup bot
    bot = Bot(token=config.bot_token.get_secret_value())
    dp = Dispatcher()
    router = setup_routers()
    dp.include_router(router)
    setup_middlewares(dp)

    # Prepare context data
    kwargs = {
        "config": config,
        "_translator_hub": translator_hub,
        "_session_maker": session_maker,
    }

    # Run bot
    try:
        # TODO: Add webhook support for production
        await bot.delete_webhook()
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types(), **kwargs)
    finally:
        await bot.session.close()
