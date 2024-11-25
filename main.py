from tkinter import *
from tkinter import messagebox
from mod.txt_processor import process_txt_file
from mod.xml_processor import process_xml_file
from mod.json_processor import process_json_file
from mod.yaml_processor import process_yaml_file
import os

class FileProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Обработка файлов")
        self.root.configure(bg="#FDF4E3")

        self.label_file_type = Label(root, text="Введите тип входного файла (txt/xml/json/yaml):",
                                     font=("Calibri", 12, "bold"), fg="#503D33", bg="#FDF4E3")
        self.label_file_type.pack(pady=10)

        self.entry_file_type = Entry(root, width=20, font=("Calibri", 12))
        self.entry_file_type.pack(pady=5)

        self.label_method = Label(root, text="Выберите метод обработки:",
                                     font=("Calibri", 12, "bold"), bg="#FDF4E3", fg="#503D33")
        self.label_method.pack(pady=10)

        self.method_var = IntVar()
        self.method_var.set(1)

        self.radio1 = Radiobutton(root, text="1. Регулярные выражения", variable=self.method_var, value=1,
                                  font=("Calibri", 12), indicatoron=0, width=30, relief=FLAT, bg="#F5E6CB",
                                  activebackground="#E7C697", fg="#503D33")
        self.radio1.pack(pady=5)

        self.radio2 = Radiobutton(root, text="2. Парсинг", variable=self.method_var, value=2, font=("Calibri", 12),
                                  indicatoron=0, width=30, relief=FLAT, bg="#F5E6CB", activebackground="#E7C697",
                                  fg="#503D33")
        self.radio2.pack(pady=5)

        self.radio3 = Radiobutton(root, text="3. Математическая библиотека (eval)", variable=self.method_var,
                                  value=3, font=("Calibri", 12), indicatoron=0, width=40, relief=FLAT, bg="#F5E6CB",
                                  activebackground="#E7C697", fg="#503D33")
        self.radio3.pack(pady=5)

        self.process_button = Button(root, text="Обработать файл", command=self.process_file, font=("Calibri", 12),
                                     bg="#8A6642", fg="#FDF4E3", activebackground="#6DAE81", borderwidth=0,
                                     relief=FLAT)
        self.process_button.pack(pady=20)

    def process_file(self):
        file_type = self.entry_file_type.get().strip().lower()
        method = self.method_var.get()

        input_file = f'data/input.{file_type}'
        output_file = f'data/output.{file_type}'

        try:
            if file_type == 'txt':
                process_txt_file(input_file, output_file, method)
            elif file_type == 'xml':
                process_xml_file(input_file, output_file, method)
            elif file_type == 'json':
                process_json_file(input_file, output_file, method)
            elif file_type == 'yaml':
                process_yaml_file(input_file, output_file, method)
            else:
                raise ValueError("Неподдерживаемый тип файла.")

            messagebox.showinfo("Успех", f"Файл успешно обработан и сохранён в {output_file}.")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))


if __name__ == "__main__":
    root = Tk()
    root.geometry("400x350+550+300")
    root.resizable(False, False)
    app = FileProcessorApp(root)
    root.mainloop()