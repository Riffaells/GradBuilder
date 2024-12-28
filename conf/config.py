from conf.lang import LanguageManager


class Config:
    def __init__(self, lang="en"):
        """
        Класс конфигурации приложения.
        :param lang: Язык.
        """
        self.language_manager = LanguageManager(lang)
