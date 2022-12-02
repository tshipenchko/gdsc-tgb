from aiogram import Router

from . import (
    translator_runner,
    session_maker
)


def setup_middlewares(router: Router) -> None:
    router.message.middleware(translator_runner.TranslatorRunnerMiddleware())
    router.message.middleware(session_maker.SessionMakerMiddleware())

