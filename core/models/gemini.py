import google.generativeai as genai

from core.models.base_model import BaseModel


class GeminiModel(BaseModel):
    """
    Реализация BaseModel для работы с Gemini API.
    """
    def __init__(self, api_key: str, model_name: str = "gemini-1.5-pro"):
        """
        Инициализация модели Gemini.

        Args:
            api_key (str): API ключ для доступа к Gemini
            model_name (str): Название модели Gemini для использования
        """
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)

    def _process_response(self, response) -> str:
        """
        Вспомогательный метод для обработки ответа от API.
        """
        return response.text

    def generate_text(self, prompt: str) -> str:
        response = self.model.generate_content(prompt)
        return self._process_response(response)

    def regenerate_text(self, previous_text: str) -> str:
        prompt = f"Создайте альтернативную версию следующего текста:\n{previous_text}"
        response = self.model.generate_content(prompt)
        return self._process_response(response)

    def expand_text(self, text: str, instructions: str = "Расширьте этот текст") -> str:
        prompt = f"{instructions}:\n{text}"
        response = self.model.generate_content(prompt)
        return self._process_response(response)

    def expand_bullet_point(self, bullet_point: str) -> list[str]:
        prompt = f"Разверните следующий пункт в список подпунктов:\n{bullet_point}"
        response = self.model.generate_content(prompt)
        # Разделяем ответ на строки и фильтруем пустые строки
        return [line.strip() for line in self._process_response(response).split('\n') if line.strip()]

    def summarize_text(self, text: str, max_length: int = 200) -> str:
        prompt = f"Создайте краткое содержание следующего текста (максимум {max_length} символов):\n{text}"
        response = self.model.generate_content(prompt)
        return self._process_response(response)[:max_length]
