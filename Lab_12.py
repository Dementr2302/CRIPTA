# построение SHA-256 для введённого текста (библиотечная реализация)

# импорт готовой библиотеки
import hashlib

def calculate_sha256(text):
    # преобразование текста в байтовую строку
    text_bytes = text.encode('utf-8')

    # создание объекта хеша SHA-256
    sha256_hash = hashlib.sha256()

    # обновление хеша с данными из текста
    sha256_hash.update(text_bytes)

    # получение хеша в виде шестнадцатеричной строки
    hashed_text = sha256_hash.hexdigest()

    return hashed_text

# ввод текст для хеширования
user_text = input("Введите текст: ")

# вычисление SHA-256 хеш
hashed_result = calculate_sha256(user_text)

# вывод результата
print(f"SHA-256 хеш для введенного текста: {hashed_result}")
