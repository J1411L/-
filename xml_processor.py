import os
import re
import xml.etree.ElementTree as ET
from xml.dom import minidom

def evaluate_expression(match):
    expression = match.group(0)
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        print(f"Ошибка при вычислении выражения '{expression}': {e}")
        return expression

def process_xml_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    try:
        tree = ET.fromstring(content)
    except ET.ParseError as e:
        print(f"Ошибка парсинга XML: {e}")
        return

    process_xml(tree)
    processed_content = ET.tostring(tree, encoding='unicode')

    # Форматируем XML для лучшего вида
    formatted_content = format_xml(processed_content)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(formatted_content)

    print(f"Обработка XML файла завершена. Результаты записаны в '{output_file}'.")

def process_xml(element):
    if element.text:
        element.text = re.sub(r'[\d\s()\-+*/.]+', evaluate_expression, element.text.strip())

    for child in element:
        process_xml(child)
        if child.tail:
            child.tail = re.sub(r'[\d\s()\-+*/.]+', evaluate_expression, child.tail.strip())

def format_xml(xml_string):
    """Форматирует строку XML для лучшего представления."""
    parsed = minidom.parseString(xml_string)
    return parsed.toprettyxml(indent="    ")

# Пример использования
if __name__ == "__main__":
    input_file = 'input.xml'
    output_file = 'output.xml'
    process_xml_file(input_file, output_file)


'''
Указание encoding='utf-8' помогает избежать ошибок, таких как UnicodeDecodeError

В случае XML это также соответствует стандартам, так как XML-документы могут содержать 
декларацию кодировки в заголовке, но если вы не укажете кодировку при чтении, это может привести к несовпадению.
'''