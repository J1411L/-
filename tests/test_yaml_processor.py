#  python -m unittest discover -s tests
# через эту команду производится запуск

import unittest
import yaml
from mod.yaml_processor import process_yaml_file

class TestYAMLProcessor(unittest.TestCase):

    def test_process_yaml_file(self):
        input_file = 'data/input.yaml'
        output_file = 'data/output.yaml'

        # Вызов функции обработки
        process_yaml_file(input_file, output_file)

        expected_output = '''expression1:
  with_regex: '8'
  without_regex: '8'
expression2:
  with_regex: '4'
  without_regex: '4'
expression3:
  with_regex: '21'
  without_regex: '21'
expression4:
  with_regex: '5.0'
  without_regex: '5.0'
'''

        with open(output_file, 'r') as f:
            output_data = f.read()

        self.assertEqual(output_data.strip(), expected_output.strip())

if __name__ == '__main__':
    unittest.main()