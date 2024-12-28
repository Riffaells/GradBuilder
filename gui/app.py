import customtkinter as ctk
from conf.config import Config
from gui.frames.mainframe import MainFrame
from gui.frames.sidebar import Sidebar


class GradBuilderApp(ctk.CTk):
    def __init__(self, config: Config):
        super().__init__()

        self.config = config
        self.language_manager = self.config.language_manager

        # Настройки окна
        self.title(self.language_manager.get("app_title"))
        self.geometry("1100x580")

        # Грид компоновка
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # Боковая панель (Sidebar)
        self.sidebar = Sidebar(self, self.config, corner_radius=0)
        self.sidebar.grid(row=0, column=0, rowspan=4, sticky="nsew")

        # Основная часть (MainFrame)
        self.main_frame = MainFrame(self, self.config, corner_radius=10)
        self.main_frame.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # Область для вывода информации (Textbox)
        self.textbox = ctk.CTkTextbox(self, width=400)
        self.textbox.grid(row=0, column=2, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.textbox.insert("0.0", "Information will be displayed here...")

        # Передаём ссылку на textbox, чтобы при генерации диплома выводить текст
        self.main_frame.set_output_textbox(self.textbox)
        self.sidebar.set_output_textbox(self.textbox)

    def run(self):
        self.mainloop()


