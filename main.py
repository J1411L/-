from txt_processor import process_txt_file
from xml_processor import process_xml_file
import os

def main():
    file_type = input("Введите тип входного файла (txt/xml): ").strip().lower()

    if file_type == 'txt':
        input_file = 'input.txt'
        output_file = 'output.txt'
        process_txt_file(input_file, output_file)
    elif file_type == 'xml':
        input_file = 'input.xml'
        output_file = 'output.xml'
        process_xml_file(input_file, output_file)
    else:
        print("Ошибка: неподдерживаемый тип файла. Пожалуйста, используйте 'txt' или 'xml'.")

if __name__ == "__main__":
    main()