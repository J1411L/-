Структура проекта:
```/my_project/
    ├── .venv/                # Виртуальное окружение 
    ├── mod/                  # Исходный код
    │   ├── __init__.py       # Указывает, что это пакет
    │   ├── expression_evaluator.py
    │   ├── txt_processor.py
    │   ├── xml_processor.py
    │   ├── json_processor.py
    │   └── yaml_processor.py
    ├── tests/                # Папка с тестами
    │   ├── __init__.py       
    │   ├── test_txt_processor.py
    │   ├── test_xml_processor.py
    │   ├── test_json_processor.py
    │   └── test_yaml_processor.py
    ├── data/                 # Папка для входных файлов
    │   ├── input.txt         
    │   ├── input.yaml       
    │   └── input.xml
    │   └── input.json        # После сюда же создаются выходные файлы
    └── main.py  
```
