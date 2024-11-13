import json
import re

def evaluate_expression(expression):
    """Вычисление арифметического выражения."""
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        print(f"Ошибка при вычислении выражения '{expression}': {e}")
        return expression

def process_expression_with_regex(expression):
    return re.sub(r'([-\d\s\(\)*/.+]+)', lambda match: evaluate_expression(match.group(0)), expression)

def process_expression_without_regex(expression):
    return evaluate_expression(expression)

def process_json_file(input_file, output_file):
    with open(input_file, 'r') as file:
        data = json.load(file)

    results = {}
    for key, expression in data.items():
        if isinstance(expression, str) and expression.strip():
            result_with_regex = process_expression_with_regex(expression)
            result_without_regex = process_expression_without_regex(expression)

            results[key] = {
                "with_regex": result_with_regex,
                "without_regex": result_without_regex
            }

    with open(output_file, 'w') as file:
        json.dump(results, file, ensure_ascii=False, indent=4)

    print(f"Обработка JSON файла завершена. Результаты записаны в '{output_file}'.")
