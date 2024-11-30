from flask import Flask, render_template, request, jsonify  # HTML-шаблонов,
                                                            # для работы с HTTP-запросами
                                                            #  для формирования JSON-ответов.
from flask import send_from_directory # для отправки файлов из определенной директории
from werkzeug.utils import secure_filename # для безопасного имени файла
import os

from mod.txt_processor import process_txt_file
from mod.xml_processor import process_xml_file
from mod.json_processor import process_json_file
from mod.yaml_processor import process_yaml_file

app = Flask(__name__) # Создание экземпляра приложения

# Папка для загрузки файлов
UPLOAD_FOLDER = 'data'
OUTPUT_FOLDER = 'outputs'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(OUTPUT_FOLDER, filename, as_attachment=True)

# Главная страница с формой
@app.route('/')
def index():
    return render_template('index.html')

# Обработка файла
@app.route('/process', methods=['POST'])
def process_file():
    try:
        # Получаем файл и параметры
        uploaded_file = request.files['file']
        #file_type = request.form['file_type']
        method = int(request.form['method'])

        if uploaded_file.filename == '':
            return jsonify({'status': 'error', 'message': 'Файл не выбран.'})

        # Сохраняем файл
        filename = secure_filename(uploaded_file.filename)
        input_path = os.path.join(UPLOAD_FOLDER, filename)
        output_path = os.path.join(OUTPUT_FOLDER, f"processed_{filename}")
        uploaded_file.save(input_path)

        file_type = filename.rsplit('.', 1)[-1].lower()  # Получаем тип файла из названия файла

        # Определяем обработку
        if file_type == 'txt':
            process_txt_file(input_path, output_path, method)
        elif file_type == 'xml':
            process_xml_file(input_path, output_path, method)
        elif file_type == 'json':
            process_json_file(input_path, output_path, method)
        elif file_type == 'yaml':
            process_yaml_file(input_path, output_path, method)
        else:
            return jsonify({'status': 'error', 'message': 'Неподдерживаемый тип файла.'})

        return jsonify({'status': 'success', 'message': f'Файл успешно обработан. Скачать: {output_path}'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
