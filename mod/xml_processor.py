import xml.etree.ElementTree as ET
import re
from xml.dom import minidom
from mod.expression_evaluator import RegexEvaluator, ParsingEvaluator, EvalEvaluator

def process_xml_file(input_file, output_file, method):
    if method == 1:
        evaluator = RegexEvaluator()
    elif method == 2:
        evaluator = ParsingEvaluator()
    elif method == 3:
        evaluator = EvalEvaluator()
    else:
        print(f"Неизвестный метод: {method}")
        return

    # Чтение XML файла
    try:
        tree = ET.parse(input_file)
        root = tree.getroot()
    except ET.ParseError as e:
        print(f"Ошибка парсинга XML: {e}")
        return

    # Обработка XML
    process_xml_element(root, evaluator)

    # Запись результатов обратно в XML файл
    formatted_content = format_xml(ET.tostring(root, encoding='unicode'))

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(formatted_content)

    print(f"Обработка XML файла завершена. Результаты записаны в '{output_file}'.")

def process_xml_element(element, evaluator):
    # Если у элемента есть текст, обрабатываем его
    if element.text:
        element.text = process_expressions(element.text.strip(), evaluator)

    # Рекурсивно обрабатываем дочерние элементы
    for child in element:
        process_xml_element(child, evaluator)
        if child.tail:
            child.tail = process_expressions(child.tail.strip(), evaluator)

def process_expressions(text, evaluator):
    # Используем регулярное выражение для поиска выражений и их обработки
    expressions = re.findall(r'[\d\s()\-+*/.]+', text)
    for expression in expressions:
        result = evaluator.evaluate(expression)
        text = text.replace(expression, result)
    return text

def format_xml(xml_string):
    """Форматирует строку XML для лучшего представления."""
    parsed = minidom.parseString(xml_string)
    return parsed.toprettyxml(indent="    ")

