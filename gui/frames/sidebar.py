import customtkinter as ctk


class Sidebar(ctk.CTkFrame):
    """
    Минимальный дизайн:
    1. Кнопка "Generate" вверху.
    2. Выпадающий список для выбора языка посередине.
    3. Выбор темы (Appearance Mode) снизу.
    Без лишних подписей.
    """

    def __init__(self, master, config, **kwargs):
        super().__init__(master, **kwargs)
        self.config = config
        self.language_manager = config.language_manager
        self.output_textbox = None

        # Разрешаем строке 3 растягиваться, чтобы Appearance Mode был "внизу"
        self.grid_rowconfigure(3, weight=1)

        # ----- 1. Генерация диплома (вверху) -----
        self.sidebar_button_generate = ctk.CTkButton(
            self,
            text=self.language_manager.get("generate"),  # Ключ из локализации
            command=self.generate_diploma
        )
        self.sidebar_button_generate.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="n")

        # ----- 2. Выбор языка (посередине) -----
        self.language_optionmenu = ctk.CTkOptionMenu(
            self,
            values=list(self.language_manager.translations.keys()),
            command=self.change_language_event
        )
        self.language_optionmenu.grid(row=2, column=0, padx=20, pady=(5, 10), sticky="ew")
        self.language_optionmenu.set(self.language_manager.current_language)

        # ----- 3. Выбор темы (внизу) -----
        self.appearance_mode_optionmenu = ctk.CTkOptionMenu(
            self,
            values=["Light", "Dark", "System"],
            command=self.change_appearance_mode_event
        )
        self.appearance_mode_optionmenu.grid(row=5, column=0, padx=20, pady=(5, 20), sticky="ew")
        self.appearance_mode_optionmenu.set("Dark")

    def set_output_textbox(self, textbox):
        """Устанавливаем Textbox, куда выводить информацию."""
        self.output_textbox = textbox

    def change_language_event(self, language):
        """Смена языка + обновление текстов."""
        self.language_manager.set_language(language)
        self.update_texts()

    def change_appearance_mode_event(self, mode):
        """Смена темы (Light/Dark/System)."""
        ctk.set_appearance_mode(mode)

    def update_texts(self):
        """Обновляет все тексты элементов интерфейса при смене языка."""
        self.sidebar_button_generate.configure(text=self.language_manager.get("generate"))

    def generate_diploma(self):
        """Пример вывода в textbox."""
        if self.output_textbox:
            self.output_textbox.delete("0.0", "end")
            self.output_textbox.insert(
                "0.0", self.language_manager.get("generating_diploma")
            )
