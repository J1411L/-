import os
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
          # re.sub(pattern, repl, string)
    return re.sub(r'([-\d\s\(\)*/.+]+)', lambda match: evaluate_expression(match.group(0)), expression)

def process_expression_without_regex(expression):
    return evaluate_expression(expression)

def process_txt_file(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    results = []
    for line in lines:
        line = line.strip()
        if line:
            result_with_regex = process_expression_with_regex(line)
            result_without_regex = process_expression_without_regex(line)

            results.append(f"{result_with_regex} (with regex)")
            results.append(f"{result_without_regex} (-)")

    with open(output_file, 'w') as file:
        file.write('\n'.join(results))

    print(f"Обработка текстового файла завершена. Результаты записаны в '{output_file}'.")



'''
Функция С регулярными выражениями (process_expression_with_regex):
Использует регулярные выражения для поиска и замены всех подходящих подстрок в строке.
Эта функция может находить множество арифметических выражений в одной строке. Например, 
если строка содержит несколько выражений, разделенных пробелами или другими символами, 
она сможет их обнаружить и обработать.
Сначала она ищет все подстроки, соответствующие регулярному выражению, а затем вызывает 
evaluate_expression для каждой найденной подстроки.

Функция БЕЗ регулярных выражений (process_expression_without_regex):
Предполагает, что строка, переданная ей, является одним валидным арифметическим выражением.
Она просто передает это выражение в evaluate_expression без предварительного анализа или 
поиска других выражений.
Если передать строку с несколькими выражениями или некорректным синтаксисом, она не сможет 
обработать это правильно.
'''