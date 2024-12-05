#  python -m unittest discover -s tests
# через эту команду производится запуск

import unittest
from mod.json_processor import process_json_file

class TestJSONProcessor(unittest.TestCase):

    def test_process_json_file(self):
        input_file = 'data/input.json'
        output_file = 'outputs/processed_input.json'

        # Вызов функции обработки
        process_json_file(input_file, output_file, method = 2)

        expected_output = '''{
    "expression1": {
        "original": "3 + 5",
        "result": "8.0"
    },
    "expression2": {
        "original": "10 - 2 * 3",
        "result": "4.0"
    },
    "expression3": {
        "original": "(1 + 2) * (3 + 4)",
        "result": "21.0"
    },
    "expression4": {
        "original": "15 / (1 + 2)",
        "result": "5.0"
    }
}'''

        with open(output_file, 'r') as f:
            output_data = f.read()

        self.assertEqual(output_data.strip(), expected_output.strip())

if __name__ == '__main__':
    unittest.main()