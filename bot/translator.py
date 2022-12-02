from pathlib import Path

from fluent_compiler.bundle import FluentBundle
from fluentogram import TranslatorHub, FluentTranslator


def generate_hub(locales_dir: Path, root_locale: str) -> TranslatorHub:
    locales = [locale.name for locale in locales_dir.glob("*") if locale.is_dir()]

    return TranslatorHub(
        {
            locale: (locale, root_locale) if locale != root_locale else (locale,)
            for locale in locales
        },
        [
            FluentTranslator(
                locale,
                translator=FluentBundle.from_files(
                    locale,
                    [locales_dir / locale / "main.ftl"],
                ),
            )
            for locale in locales
        ],
    )
