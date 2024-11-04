import tkinter as tk
from tkinter import filedialog, messagebox

class GameDirectoryApp:
    def __init__(self, master):
        self.master = master
        master.title("Game Directory Manager")

        # Метка для ввода директории
        self.label = tk.Label(master, text="Укажите директорию игры:")
        self.label.pack(pady=10)

        # Создаем фрейм для поля ввода и кнопки "Обзор"
        self.input_frame = tk.Frame(master)
        self.input_frame.pack(pady=5)

        # Поле ввода для директории
        self.directory_entry = tk.Entry(self.input_frame, width=50)
        self.directory_entry.pack(side=tk.LEFT, padx=(0, 5))

        # Кнопка для выбора директории
        self.browse_button = tk.Button(self.input_frame, text="Обзор", command=self.browse_directory)
        self.browse_button.pack(side=tk.LEFT)

        # Разделительная линия для визуального отделения
        self.separator = tk.Frame(master, height=2, bd=1, relief=tk.SUNKEN)
        self.separator.pack(fill=tk.X, padx=10, pady=10)

        # Фрейм для кнопок "Заменить" и "Возобновить"
        self.button_frame = tk.Frame(master)
        self.button_frame.pack(pady=5)

        # Кнопка "Заменить"
        self.replace_button = tk.Button(self.button_frame, text="Заменить", command=self.replace_directory)
        self.replace_button.pack(side=tk.LEFT, padx=(20, 10))

        # Кнопка "Возобновить"
        self.resume_button = tk.Button(self.button_frame, text="Возобновить", command=self.resume_game)
        self.resume_button.pack(side=tk.LEFT, padx=(10, 20))

    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.directory_entry.delete(0, tk.END)
            self.directory_entry.insert(0, directory)

    def replace_directory(self):
        directory = self.directory_entry.get()
        if directory:
            # Здесь можно добавить логику замены директории
            messagebox.showinfo("Информация", f"Названия заменены: {directory}")
        else:
            messagebox.showwarning("Предупреждение", "Пожалуйста, укажите директорию.")

    def resume_game(self):
        directory = self.directory_entry.get()
        if directory:
            # Здесь можно добавить логику возобновления игры
            messagebox.showinfo("Информация", f"Восстановлена старая версия игры: {directory}")
        else:
            messagebox.showwarning("Предупреждение", "Пожалуйста, укажите директорию.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GameDirectoryApp(root)
    root.mainloop()
