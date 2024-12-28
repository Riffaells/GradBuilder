import customtkinter as ctk

class MainFrame(ctk.CTkFrame):
    def __init__(self, master, config, **kwargs):
        super().__init__(master, **kwargs)
        self.config = config
        self.language_manager = self.config.language_manager
        self.output_textbox = None

        # Заголовок
        self.title_label = ctk.CTkLabel(
            self,
            text=self.language_manager.get("app_title"),
            font=ctk.CTkFont(size=18, weight="bold")
        )
        self.title_label.pack(pady=10)

        # Поля для ввода
        self.title_entry = self.create_input(self, "diploma_title")
        self.author_entry = self.create_input(self, "author")
        self.supervisor_entry = self.create_input(self, "supervisor")
        self.year_entry = self.create_input(self, "year", width=100)

        # Параметры страницы (отступы)
        self.margins_frame = ctk.CTkFrame(self, corner_radius=10)
        self.margins_frame.pack(pady=10)
        self.margins_label = ctk.CTkLabel(
            self.margins_frame, text=self.language_manager.get("page_margins"), font=ctk.CTkFont(size=14)
        )
        self.margins_label.pack(pady=5)
        self.margin_left = self.create_margin_input(self.margins_frame, "left", default=1.0)
        self.margin_right = self.create_margin_input(self.margins_frame, "right", default=1.0)
        self.margin_top = self.create_margin_input(self.margins_frame, "top", default=1.0)
        self.margin_bottom = self.create_margin_input(self.margins_frame, "bottom", default=1.0)

    def set_output_textbox(self, textbox):
        """Получаем ссылку на textbox, чтобы выводить туда информацию."""
        self.output_textbox = textbox

    def create_input(self, parent, label_key, width=400):
        """Создание текстового поля с меткой."""
        frame = ctk.CTkFrame(parent, corner_radius=10)
        frame.pack(pady=5, fill="x", padx=20)
        label = ctk.CTkLabel(frame, text=self.language_manager.get(label_key), font=("Arial", 14))
        label.pack(side="left", padx=10)
        entry = ctk.CTkEntry(frame, width=width)
        entry.pack(side="right", padx=10)
        return entry

    def create_margin_input(self, parent, label_key, default):
        """Создание поля для ввода отступов."""
        frame = ctk.CTkFrame(parent, corner_radius=10)
        frame.pack(pady=5, fill="x", padx=20)
        label = ctk.CTkLabel(frame, text=self.language_manager.get(label_key), font=("Arial", 14))
        label.pack(side="left", padx=10)
        entry = ctk.CTkEntry(frame, width=100)
        entry.insert(0, str(default))
        entry.pack(side="right", padx=10)
        return entry
