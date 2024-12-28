import json
import os


class LanguageManager:
    def __init__(self, default_language="en"):
        """
        Загружает переводы из папки `lang`.
        :param default_language: Язык по умолчанию.
        """
        # Определяем путь к папке lang относительно текущего файла
        self.lang_folder = os.path.join(os.path.dirname(__file__), "lang")
        self.translations = {}
        self.current_language = default_language

        self.load_translations()

    def load_translations(self):
        """Загружает все JSON-файлы из папки `lang_folder`."""
        if not os.path.exists(self.lang_folder):
            raise FileNotFoundError(f"Папка перевода не найдена: {self.lang_folder}")

        for file_name in os.listdir(self.lang_folder):
            if file_name.endswith(".json"):
                lang_code = os.path.splitext(file_name)[0]
                with open(os.path.join(self.lang_folder, file_name), "r", encoding="utf-8") as file:
                    self.translations[lang_code] = json.load(file)

    def set_language(self, language):
        """Устанавливает текущий язык."""
        if language in self.translations:
            self.current_language = language
        else:
            raise ValueError(f"Язык '{language}' не найден в доступных переводах.")

    def get(self, key):
        """Возвращает перевод для текущего языка."""
        # Проверяем, есть ли язык и ключ
        translation = self.translations.get(self.current_language, {})
        return translation.get(key, f"<{key}>")
