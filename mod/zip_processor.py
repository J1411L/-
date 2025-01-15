import zipfile
import os

def extract_zip(input_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)  # Создаем выходную папку, если она не существует

    try:
        with zipfile.ZipFile(input_path, 'r') as zip_ref:
            zip_ref.extractall(output_folder)  # Извлекаем все файлы
            return [os.path.join(output_folder, name) for name in zip_ref.namelist()]  # Возвращаем список извлеченных файлов
    except zipfile.BadZipFile:
        print(f"Ошибка: файл '{input_path}' не является корректным ZIP-архивом.")
        return []  # Возвращаем пустой список в случае ошибки
    except Exception as e:
        print(f"Ошибка при извлечении ZIP файла: {e}")
        return []  # Возвращаем пустой список в случае других ошибок