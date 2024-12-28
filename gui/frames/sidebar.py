import customtkinter as ctk


class Sidebar(ctk.CTkFrame):
    def __init__(self, master, config, **kwargs):
        super().__init__(master, **kwargs)
        self.config = config
        self.language_manager = config.language_manager
        self.output_textbox = None  # Ссылка на textbox для вывода информации

        self.grid_rowconfigure(4, weight=1)

        self.logo_label = ctk.CTkLabel(
            self,
            text="GradBuilder",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Кнопка генерации
        self.sidebar_button_generate = ctk.CTkButton(
            self,
            text=self.language_manager.get("generate"),
            command=self.generate_diploma
        )
        self.sidebar_button_generate.grid(row=1, column=0, padx=20, pady=10)

        # Appearance Mode
        self.appearance_mode_label = ctk.CTkLabel(
            self, text="Appearance Mode:", anchor="w"
        )
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))

        self.appearance_mode_optionmenu = ctk.CTkOptionMenu(
            self,
            values=["Light", "Dark", "System"],
            command=self.change_appearance_mode_event
        )
        self.appearance_mode_optionmenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.appearance_mode_optionmenu.set("Dark")

    def set_output_textbox(self, textbox):
        """Получаем ссылку на textbox, чтобы выводить туда информацию."""
        self.output_textbox = textbox

    def change_appearance_mode_event(self, mode):
        """Смена темы интерфейса."""
        ctk.set_appearance_mode(mode)

    def generate_diploma(self):
        """Пример вывода в textbox."""
        if self.output_textbox:
            self.output_textbox.delete("0.0", "end")
            self.output_textbox.insert("0.0", "Generate diploma from Sidebar...\n")


