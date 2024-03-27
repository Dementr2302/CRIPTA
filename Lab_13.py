from pyDes import des, CBC, PAD_PKCS5
import os

# Функция для шифрования DES в режиме CFB
def encrypt_DES_CFB(plaintext, key, iv):
    # Создание объекта DES шифра с указанным ключом, режимом (CBC) и вектором инициализации (iv)
    cipher = des(key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    # Шифрование исходного текста
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

# Функция для расшифрования DES в режиме CFB
def decrypt_DES_CFB(ciphertext, key, iv):
    # Создание объекта DES шифра с указанным ключом, режимом (CBC) и вектором инициализации (iv)
    cipher = des(key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    # Расшифрование зашифрованного текста
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

# Пример использования
key = b'01234567'  # 8-байтовый ключ DES
iv = os.urandom(8)  # 8-байтовый вектор инициализации

plaintext = b'Hello, World!'  # Исходный текст
print("Исходный текст:", plaintext)

# Зашифровка текста
ciphertext = encrypt_DES_CFB(plaintext, key, iv)
print("Зашифрованный текст:", ciphertext)

# Расшифровка текста
decrypted_text = decrypt_DES_CFB(ciphertext, key, iv)
print("Расшифрованный текст:", decrypted_text)
