from aiogram import Router

from . import (
    translator_runner,
)


def setup_middlewares(router: Router) -> None:
    router.message.middleware(translator_runner.TranslatorRunnerMiddleware())
