import argparse


class ArgumentParser:
    """Класс для работы с аргументами командной строки."""

    def __init__(self, language_manager):
        self.language_manager = language_manager

    def parse_arguments(self):
        """Создаёт и парсит аргументы командной строки."""
        parser = argparse.ArgumentParser(
            description=self.language_manager.get("app_title")
        )

        # Параметры диплома
        parser.add_argument(
            "--title", required=True, help=self.language_manager.get("diploma_title")
        )
        parser.add_argument(
            "--author", required=True, help=self.language_manager.get("author")
        )
        parser.add_argument(
            "--supervisor", required=True, help=self.language_manager.get("supervisor")
        )
        parser.add_argument(
            "--year", required=True, help=self.language_manager.get("year")
        )

        # Настройки отступов
        parser.add_argument(
            "--margin-left",
            type=float,
            default=1.0,
            help=self.language_manager.get("left"),
        )
        parser.add_argument(
            "--margin-right",
            type=float,
            default=1.0,
            help=self.language_manager.get("right"),
        )
        parser.add_argument(
            "--margin-top",
            type=float,
            default=1.0,
            help=self.language_manager.get("top"),
        )
        parser.add_argument(
            "--margin-bottom",
            type=float,
            default=1.0,
            help=self.language_manager.get("bottom"),
        )

        # Язык
        parser.add_argument(
            "--lang",
            type=str,
            choices=["en", "ru"],
            default=self.language_manager.current_language,
            help="Language for the application.",
        )

        # Имя выходного файла
        parser.add_argument(
            "--output",
            type=str,
            default="Diploma.docx",
            help="Output file name (default: Diploma.docx).",
        )

        return parser.parse_args()
