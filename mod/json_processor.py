import json
from mod.expression_evaluator import RegexEvaluator, ParsingEvaluator, EvalEvaluator

def process_json_file(input_file, output_file, method):
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
        data = json.load(file)

    results = {}
    for key, expression in data.items():
        if isinstance(expression, str) and expression.strip():
            result = evaluator.evaluate(expression)
            results[key] = {
                "original": expression,
                "result": result
            }

    # Запись результатов обратно в JSON файл
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(results, file, ensure_ascii=False, indent=4)

    print(f"Обработка JSON файла завершена. Результаты записаны в '{output_file}'.")

