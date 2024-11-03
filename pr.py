import argparse
import re

def evaluate_expression(match):
    expression = match.group(0) # содержит строку с найденным регулярным выражением
    try:
        result = eval(expression)  # Вычисляем выражение
        return str(result)
    except Exception as e:
        print(f"Ошибка при вычислении выражения '{expression}': {e}")
        return expression  # В случае ошибки возвращаем исходное выражение

def process_file(input_file, output_file):

    try:
        with open(input_file, 'r') as file:
            content = file.read()

        # Ищем арифметические выражения с операциями +, -, *, /
        processed_content = re.sub(r'\b[\d+\-*/\s]+\b', evaluate_expression, content)

        with open(output_file, 'w') as file:
            file.write(processed_content)

        print(f"Обработка завершена. Результаты записаны в файл '{output_file}'.")

    except FileNotFoundError:
        print(f"Ошибка: файл '{input_file}' не найден.")
    except Exception as e:
        print(f"Ошибка при обработке файла: {e}")


def main():
    # создали объект с указанием его описания
    parser = argparse.ArgumentParser(description="приложение для замены арифметических выражений на результаты.")
    """
    Далее, с помощью метода parser.add_argument(), описывается переменная input_file, в которую планируется 
    записать путь к папке с файлом. При этом указывается то, что она имеет строковой тип, а 
    также задаётся справочная информация о ней. После этого, точно так же, создаётся переменная output_file, 
    в которую попадёт путь к папке, в которую скрипт должен будет поместить файлы, созданные на 
    основе входных файлов. 
    """
    parser.add_argument('input_file', type=str, help='input.txt')
    parser.add_argument('output_file', type=str, help='output.txt')
    """
    На следующем шаге работы в переменную args попадает результат разбора аргументов 
    командной строки. То, что передано скрипту при запуске, теперь будет доступно в виде свойств input_file и 
    output_file объекта args. Теперь с этими значениями можно работать. 
    """
    args = parser.parse_args()

    process_file(args.input_file, args.output_file)

if __name__ == "__main__":
    main()
