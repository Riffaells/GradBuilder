import customtkinter as ctk


class MainFrame(ctk.CTkFrame):
    """
    Главная часть приложения с возможностью добавления разделов.
    """

    def __init__(self, master, config, **kwargs):
        super().__init__(master, **kwargs)
        self.config = config
        self.language_manager = config.language_manager

        # Список разделов
        self.sections = []
        self.output_textbox = None  # Ссылка на внешнее текстовое поле

        # Заголовок
        self.title_label = ctk.CTkLabel(
            self,
            text=self.language_manager.get("app_title"),
            font=ctk.CTkFont(size=18, weight="bold")
        )
        self.title_label.pack(pady=10)

        # Текстовое поле для ввода раздела
        self.section_entry = ctk.CTkEntry(
            self,
            placeholder_text=self.language_manager.get("enter_section"),
            width=400
        )
        self.section_entry.pack(pady=(5, 10))

        # Кнопка "Добавить раздел"
        self.add_section_button = ctk.CTkButton(
            self,
            text=self.language_manager.get("add_section"),
            command=self.add_section
        )
        self.add_section_button.pack(pady=(5, 10))

        # Список добавленных разделов
        self.sections_listbox = ctk.CTkTextbox(self, height=150, width=400)
        self.sections_listbox.pack(pady=(10, 10))

        # Кнопки "Удалить последний раздел" и "Очистить все разделы"
        self.clear_buttons_frame = ctk.CTkFrame(self)
        self.clear_buttons_frame.pack(pady=(10, 10))

        self.remove_last_button = ctk.CTkButton(
            self.clear_buttons_frame,
            text=self.language_manager.get("remove_last"),
            command=self.remove_last_section
        )
        self.remove_last_button.grid(row=0, column=0, padx=(5, 10))

        self.clear_all_button = ctk.CTkButton(
            self.clear_buttons_frame,
            text=self.language_manager.get("clear_all"),
            command=self.clear_all_sections
        )
        self.clear_all_button.grid(row=0, column=1, padx=(10, 5))

    def set_output_textbox(self, textbox):
        """Устанавливает внешнее текстовое поле для вывода."""
        self.output_textbox = textbox

    def add_section(self):
        """Добавляет новый раздел в список."""
        section = self.section_entry.get().strip()
        if section:
            self.sections.append(section)
            self.update_sections_listbox()
            self.section_entry.delete(0, "end")
            self.update_output_textbox(f"Section added: {section}")

    def remove_last_section(self):
        """Удаляет последний раздел из списка."""
        if self.sections:
            removed = self.sections.pop()
            self.update_sections_listbox()
            self.update_output_textbox(f"Section removed: {removed}")

    def clear_all_sections(self):
        """Очищает все разделы."""
        self.sections = []
        self.update_sections_listbox()
        self.update_output_textbox("All sections cleared.")

    def update_sections_listbox(self):
        """Обновляет отображение списка разделов."""
        self.sections_listbox.delete("0.0", "end")
        for i, section in enumerate(self.sections, 1):
            self.sections_listbox.insert("end", f"{i}. {section}\n")

    def update_output_textbox(self, message):
        """Выводит сообщение во внешнее текстовое поле."""
        if self.output_textbox:
            self.output_textbox.insert("end", message + "\n")
            self.output_textbox.see("end")
