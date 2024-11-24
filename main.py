from tkinter import * # Библиотека для создания графического интерфейса.
from tkinter import messagebox # Модуль Tkinter для отображения сообщений об ошибках и уведомлениях.
from mod.txt_processor import process_txt_file
from mod.xml_processor import process_xml_file
from mod.json_processor import process_json_file
from mod.yaml_processor import process_yaml_file
import os

class FileProcessorApp:
    # Это основной класс приложения, который инициализирует графический интерфейс.
    def __init__(self, root):
    # Метод инициализации, который устанавливает заголовок окна
        self.root = root
        self.root.title("Обработка файлов")

        self.label_file_type = Label(root, text="Введите тип входного файла (txt/xml/json/yaml):")
        self.label_file_type.pack()

        self.entry_file_type = Entry(root, width=20)
        self.entry_file_type.pack()
        '''Label: Надпись для ввода типа файла.
           Entry: Поле ввода'''

        self.label_method = Label(root, text="Выберите метод обработки:")
        self.label_method.pack()

        self.method_var = IntVar() # Переменная для хранения значения выбранного метода.
        self.method_var.set(1)  # Установка метода по умолчанию

        # Кнопки для выбора одного из методов обработки
        self.radio1 = Radiobutton(root, text="1. Регулярные выражения", variable=self.method_var, value=1)
        self.radio1.pack()

        self.radio2 = Radiobutton(root, text="2. Парсинг", variable=self.method_var, value=2)
        self.radio2.pack()

        self.radio3 = Radiobutton(root, text="3. Математическая библиотека (eval)", variable=self.method_var, value=3)
        self.radio3.pack()

        # Кнопка, при нажатии на которую вызывается метод process_file.
        self.process_button = Button(root, text="Обработать файл", command=self.process_file)
        self.process_button.pack()

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
    root.geometry("400x200+550+300") # размер + сдвиг
    root.resizable(False, False)
    app = FileProcessorApp(root)
    root.mainloop()

    '''
    Создание главного окна: Tk() создает главное окно приложения.
    
    Создание экземпляра приложения: FileProcessorApp(root) инициализирует интерфейс.
    
    Запуск главного цикла: root.mainloop() запускает основной цикл обработки событий, 
    что позволяет взаимодействовать с приложением.'''