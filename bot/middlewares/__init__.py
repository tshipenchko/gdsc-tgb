from aiogram import Dispatcher

from bot.middlewares import (
    translator_runner,
    controller,
)


def setup_middlewares(dp: Dispatcher) -> None:
    dp.update.middleware(translator_runner.TranslatorRunnerMiddleware())
    dp.update.middleware(controller.ControllerMiddleware())
