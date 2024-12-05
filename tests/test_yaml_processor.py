#  python -m unittest discover -s tests
# через эту команду производится запуск

import unittest
import yaml
from mod.yaml_processor import process_yaml_file

class TestYAMLProcessor(unittest.TestCase):

    def test_process_yaml_file(self):
        input_file = 'data/input.yaml'
        output_file = 'outputs/processed_input.yaml'

        # Вызов функции обработки
        process_yaml_file(input_file, output_file, method = 3)

        expected_output = '''expression1:
  original: '3 + 5'
  result: '8'

expression2:
  original: '10 - 2 * 3'
  result: '4'

expression3:
  original: '(1 + 2) * (3 + 4)'
  result: '21'

expression4:
  original: '15 / (1 + 2)'
  result: '5.0' '''

        with open(output_file, 'r') as f:
            output_data = f.read()

        self.assertEqual(output_data.strip(), expected_output.strip())

if __name__ == '__main__':
    unittest.main()