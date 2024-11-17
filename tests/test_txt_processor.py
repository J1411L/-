#  python -m unittest discover -s tests
# через эту команду производится запуск

import unittest
from mod.txt_processor import process_txt_file

class TestTxtProcessor(unittest.TestCase):

    def test_process_txt_file(self):
        input_file = 'data/input.txt'
        output_file = 'data/output.txt'

        # Вызов функции обработки
        process_txt_file(input_file, output_file)

        expected_output = '''8.0 (with regex)
8.0 (-)
1 (with regex)
1 (-)'''

        with open(output_file, 'r') as f:
            output_data = f.read()

        self.assertEqual(output_data.strip(), expected_output.strip())

if __name__ == '__main__':
    unittest.main()



'''
python:
Это команда для запуска интерпретатора Python. Вы можете использовать python, python3, 
или полный путь к интерпретатору в зависимости от вашей системы и настроек.

-m unittest:
Опция -m говорит Python запустить модуль как скрипт. В данном случае мы запускаем модуль 
unittest, который является встроенным модулем для тестирования в Python. Это позволяет 
использовать функции и классы, определенные в unittest.

discover:
Это команда для unittest, которая ищет и обнаруживает тестовые файлы и тестовые случаи 
автоматически. Она ищет файлы с именами, начинающимися с test (По умолчанию это файлы, 
начинающиеся с test_ или заканчивающиеся на _test.py.), и классы, производные 
от unittest.TestCase.

-s tests:
Опция -s указывает директорию, в которой unittest должен искать тесты. В данном случае 
tests — это папка, в которой вы разместили свои тестовые файлы.
'''