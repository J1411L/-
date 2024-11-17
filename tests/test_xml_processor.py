#  python -m unittest discover -s tests
# через эту команду производится запуск

import unittest
from mod.xml_processor import process_xml_file

class TestXMLProcessor(unittest.TestCase):

    def test_process_xml_file(self):
        input_file = 'data/input.xml'
        output_file = 'data/output.xml'

        # Вызов функции обработки
        process_xml_file(input_file, output_file)

        expected_output = '''<?xml version="1.0" ?>
<calculations>
    <expression>8</expression>
    <expression>8.0</expression>
    <final>5.0</final>
</calculations>
'''

        with open(output_file, 'r') as f:
            output_data = f.read()

        self.assertEqual(output_data.strip(), expected_output.strip())

if __name__ == '__main__':
    unittest.main()