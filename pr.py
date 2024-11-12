import os # Для получения путей к файлам
import re # Для регулярных выражений
import xml.etree.ElementTree as ET # Для обработки и создания XML-документов

def evaluate_expression(match):
    expression = match.group(0)
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        print(f"Ошибка при вычислении выражения '{expression}': {e}")
        return expression

def process_file(input_file, output_file):
    # Определяем тип файла по расширению
    _, file_extension = os.path.splitext(input_file)
    file_extension = file_extension.lower()

    if file_extension == '.txt':
        with open(input_file, 'r') as file:
            content = file.read()
        processed_content = re.sub(r'\b[\d+\-*/\s]+\b', evaluate_expression, content)
        with open(output_file, 'w') as file:
            file.write(processed_content)
        print(f"Обработка текстового файла завершена. Результаты записаны в '{output_file}'.")

    elif file_extension == '.xml':
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()

        try:
            tree = ET.fromstring(content)
        except ET.ParseError as e:
            print(f"Ошибка парсинга XML: {e}")
            return

        process_xml(tree)
        processed_content = ET.tostring(tree, encoding='unicode')
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(processed_content)
        print(f"Обработка XML файла завершена. Результаты записаны в '{output_file}'.")

    else:
        print("Ошибка: неподдерживаемый тип файла. Пожалуйста, используйте .txt или .xml.")

def process_xml(element):
    if element.text:
        element.text = re.sub(r'\b[\d+\-*/\s]+\b', evaluate_expression, element.text)

    for child in element:
        process_xml(child)
        if child.tail:
            child.tail = re.sub(r'\b[\d+\-*/\s]+\b', evaluate_expression, child.tail)

def main():
    file_type = input("Введите тип входного файла (txt/xml/json/yaml): ").strip().lower()

    if file_type == 'txt':
        input_file = 'input.txt'
        output_file = 'output.txt'
    elif file_type == 'xml':
        input_file = 'input.xml'
        output_file = 'output.xml'
    elif file_type == 'json':
        input_file = 'input.json'
        output_file = 'output.json'
    elif file_type == 'yaml':
        input_file = 'input.yaml'
        output_file = 'output.yaml'
    else:
        print("Ошибка: неподдерживаемый тип файла. Пожалуйста, используйте 'txt' или 'xml'.")
        return

    process_file(input_file, output_file)

if __name__ == "__main__":
    main()