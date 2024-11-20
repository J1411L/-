from mod.expression_evaluator import RegexEvaluator, ParsingEvaluator, EvalEvaluator

def process_txt_file(input_file, output_file, method):
    if method == 1:
        evaluator = RegexEvaluator()
    elif method == 2:
        evaluator = ParsingEvaluator()
    elif method == 3:
        evaluator = EvalEvaluator()
    else:
        print(f"Неизвестный метод: {method}")
        return

    with open(input_file, 'r') as file:
        lines = file.readlines()

    results = []
    for line in lines:
        line = line.strip()
        if line:
            # Используем оцениватель для вычисления выражения
            result = evaluator.evaluate(line)
            if result is not None:
                results.append(result)


    with open(output_file, 'w') as file:
        file.write('\n'.join(results))

    print(f"Обработка текстового файла завершена. Результаты записаны в '{output_file}'.")