import os
import yaml
from mod.expression_evaluator import RegexEvaluator, ParsingEvaluator, EvalEvaluator

def process_yaml_file(input_file, output_file, method):
    if method == 1:
        evaluator = RegexEvaluator()
    elif method == 2:
        evaluator = ParsingEvaluator()
    elif method == 3:
        evaluator = EvalEvaluator()
    else:
        print(f"Неизвестный метод: {method}")
        return

    with open(input_file, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)

    results = {}
    for key, expression in data.items():
        if isinstance(expression, str) and expression.strip():
            result = evaluator.evaluate(expression)
            results[key] = {
                "original": expression,
                "result": result
            }

    with open(output_file, 'w', encoding='utf-8') as file:
        for key, value in results.items():
            file.write(f"{key}:\n")
            file.write(f"  original: '{value['original']}'\n")
            file.write(f"  result: '{value['result']}'\n")
            file.write("\n")

    print(f"Обработка YAML файла завершена. Результаты записаны в '{output_file}'.")