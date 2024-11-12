import argparse
import re
import os
import json
import yaml
import xml.etree.ElementTree as ET

def evaluate_expression(match):
    expression = match.group(0)
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        print(f"Ошибка при вычислении выражения '{expression}': {e}")
        return expression

def process_file(input_file, output_file, file_type):
    try:
        if not os.path.isfile(input_file):
            print(f"Ошибка: файл '{input_file}' не найден.")
            return

        if file_type == 'txt':
            with open(input_file, 'r') as file:
                content = file.read()
            processed_content = re.sub(r'\b[\d+\-*/\s]+\b', evaluate_expression, content)
            with open(output_file, 'w') as file:
                file.write(processed_content)

        elif file_type == 'json':
            with open(input_file, 'r') as file:
                content = json.load(file)
            processed_content = process_json_yaml(content)
            with open(output_file, 'w') as file:
                json.dump(processed_content, file, ensure_ascii=False, indent=4)

        elif file_type == 'yaml':
            with open(input_file, 'r') as file:
                content = yaml.safe_load(file)
            processed_content = process_json_yaml(content)
            with open(output_file, 'w') as file:
                yaml.dump(processed_content, file, allow_unicode=True)

        elif file_type == 'xml':
            tree = ET.parse(input_file)
            root = tree.getroot()
            process_xml(root)
            tree.write(output_file, encoding='utf-8', xml_declaration=True)

        print(f"Обработка завершена. Результаты записаны в файл '{output_file}'.")

    except Exception as e:
        print(f"Ошибка при обработке файла: {e}")

def process_json_yaml(data):
    if isinstance(data, dict):
        return {k: process_json_yaml(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [process_json_yaml(item) for item in data]
    elif isinstance(data, str):
        return re.sub(r'\b[\d+\-*/\s]+\b', evaluate_expression, data)
    return data

def process_xml(element):
    if element.text:
        element.text = re.sub(r'\b[\d+\-*/\s]+\b', evaluate_expression, element.text)
    for child in element:
        process_xml(child)



def main():
    parser = argparse.ArgumentParser(description="Приложение для замены арифметических выражений на результаты.")
    parser.add_argument('input_file', type=str, help='Путь к входному файлу')
    parser.add_argument('output_file', type=str, help='Путь к выходному файлу')
    args = parser.parse_args()

    file_type = input("Введите тип входного файла (txt, xml, json, yaml): ").strip().lower()
    if file_type not in ['txt', 'xml', 'json', 'yaml']:
        print("Ошибка: недопустимый тип файла. Пожалуйста, введите один из следующих: txt, xml, json, yaml.")
        return

    process_file(args.input_file, args.output_file, file_type)

if __name__ == "__main__":
    main()
