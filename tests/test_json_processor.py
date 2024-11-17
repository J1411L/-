#  python -m unittest discover -s tests
# через эту команду производится запуск

import unittest
from mod.json_processor import process_json_file

class TestJSONProcessor(unittest.TestCase):

    def test_process_json_file(self):
        input_file = 'data/input.json'
        output_file = 'data/output.json'

        # Вызов функции обработки
        process_json_file(input_file, output_file)

        expected_output = '''{
    "expression1": {
        "with_regex": "8",
        "without_regex": "8"
    },
    "expression2": {
        "with_regex": "4",
        "without_regex": "4"
    },
    "expression3": {
        "with_regex": "21",
        "without_regex": "21"
    },
    "expression4": {
        "with_regex": "5.0",
        "without_regex": "5.0"
    }
}
'''

        with open(output_file, 'r') as f:
            output_data = f.read()

        self.assertEqual(output_data.strip(), expected_output.strip())

if __name__ == '__main__':
    unittest.main()