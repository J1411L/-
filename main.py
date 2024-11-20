from mod.txt_processor import process_txt_file
from mod.xml_processor import process_xml_file
from mod.json_processor import process_json_file
from mod.yaml_processor import process_yaml_file
import os

def main():
    #print("Текущая рабочая директория:", os.getcwd())
    file_type = input("Введите тип входного файла (txt/xml/json/yaml): ").strip().lower()
    print("Выберите метод обработки:")
    print("1. Регулярные выражения")
    print("2. Парсинг")
    print("3. Математическая библиотека (eval)")
    method = int(input("Введите номер метода (1, 2 или 3): "))

    if file_type == 'txt':
        input_file = 'data/input.txt'
        output_file = 'data/output.txt'
        process_txt_file(input_file, output_file, method)
    elif file_type == 'xml':
        input_file = 'data/input.xml'
        output_file = 'data/output.xml'
        process_xml_file(input_file, output_file, method)
    elif file_type == 'json':
        input_file = 'data/input.json'
        output_file = 'data/output.json'
        process_json_file(input_file, output_file, method)
    elif file_type == 'yaml':
        input_file = 'data/input.yaml'
        output_file = 'data/output.yaml'
        process_yaml_file(input_file, output_file, method)
    else:
        print("Ошибка: неподдерживаемый тип файла. Пожалуйста, используйте 'txt', 'xml', 'json', 'yaml'.")

if __name__ == "__main__":
    main()