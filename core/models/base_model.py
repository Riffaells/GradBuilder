class BaseModel:
    """
    Базовый класс для LLM модели.
    Определяет общий интерфейс для различных операций с текстом.
    """
    def generate_text(self, prompt: str) -> str:
        """
        Генерирует текст на основе prompt.

        Args:
            prompt (str): Входной текст-промпт

        Returns:
            str: Сгенерированный текст
        """
        raise NotImplementedError("generate_text must be implemented in subclass.")

    def regenerate_text(self, previous_text: str) -> str:
        """
        Перегенерирует существующий текст, создавая новую версию.

        Args:
            previous_text (str): Текст для перегенерации

        Returns:
            str: Новая версия текста
        """
        raise NotImplementedError("regenerate_text must be implemented in subclass.")

    def expand_text(self, text: str, instructions: str = "Расширьте этот текст") -> str:
        """
        Расширяет существующий текст, добавляя больше деталей или контекста.

        Args:
            text (str): Исходный текст для расширения
            instructions (str): Инструкции по расширению текста

        Returns:
            str: Расширенный текст
        """
        raise NotImplementedError("expand_text must be implemented in subclass.")

    def expand_bullet_point(self, bullet_point: str) -> list[str]:
        """
        Расширяет один пункт в список подпунктов.

        Args:
            bullet_point (str): Исходный пункт

        Returns:
            list[str]: Список подпунктов
        """
        raise NotImplementedError("expand_bullet_point must be implemented in subclass.")

    def summarize_text(self, text: str, max_length: int = 200) -> str:
        """
        Создает краткое содержание текста.

        Args:
            text (str): Исходный текст для обобщения
            max_length (int): Максимальная длина итогового текста

        Returns:
            str: Сокращенная версия текста
        """
        raise NotImplementedError("summarize_text must be implemented in subclass.")
