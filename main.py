from txt_processor import process_txt_file
from xml_processor import process_xml_file
from json_processor import process_json_file
from yaml_processor import process_yaml_file
import os

def main():
    file_type = input("Введите тип входного файла (txt/xml/json/yaml): ").strip().lower()

    if file_type == 'txt':
        input_file = 'input.txt'
        output_file = 'output.txt'
        process_txt_file(input_file, output_file)
    elif file_type == 'xml':
        input_file = 'input.xml'
        output_file = 'output.xml'
        process_xml_file(input_file, output_file)
    elif file_type == 'json':
        input_file = 'input.json'
        output_file = 'output.json'
        process_json_file(input_file, output_file)
    elif file_type == 'yaml':
        input_file = 'input.yaml'
        output_file = 'output.yaml'
        process_yaml_file(input_file, output_file)
    else:
        print("Ошибка: неподдерживаемый тип файла. Пожалуйста, используйте 'txt', 'xml', 'json', 'yaml'.")

if __name__ == "__main__":
    main()