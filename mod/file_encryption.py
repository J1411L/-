def xor_encrypt_decrypt(data, key):
    """Шифрование и дешифрование с использованием XOR."""
    return bytearray([data[i] ^ key[i % len(key)] for i in range(len(data))])


def encrypt_file(file_path):
    key = b'secret_key'  # Ваш ключ шифрования

    with open(file_path, 'rb') as file:
        original_data = file.read()

    # Шифрование данных
    encrypted_data = xor_encrypt_decrypt(original_data, key)

    # Запись зашифрованных данных в новый файл
    encrypted_file_path = f"{file_path}.encrypted"
    with open(encrypted_file_path, 'wb') as file:
        file.write(encrypted_data)

    return encrypted_file_path