from cryptography.hazmat.backends import default_backend  # Импорт бэкенда по умолчанию для криптографических операций
from cryptography.hazmat.primitives import hashes  # Импорт хеш-функций
from cryptography.hazmat.primitives.asymmetric import dsa  # Импорт асимметричного алгоритма DSA
from cryptography.exceptions import InvalidSignature  # Импорт исключения InvalidSignature для обработки недопустимых подписей
from cryptography.hazmat.backends import default_backend  # Импорт бэкенда по умолчанию для криптографических операций
from cryptography.hazmat.primitives import hashes  # Импорт хеш-функций
from cryptography.hazmat.primitives.asymmetric import dsa  # Импорт асимметричного алгоритма DSA
from cryptography.exceptions import InvalidSignature  # Импорт исключения InvalidSignature для обработки недопустимых подписей

# Приватный ключ используется для создания цифровой подписи данных.
# Только владелец приватного ключа может создавать подписи, и он
# должен хранить свой приватный ключ в безопасном месте, так как его
# компрометация может позволить злоумышленникам создавать поддельные подписи от имени владельца.

# Публичный ключ используется для проверки цифровой подписи.
# Он распространяется открыто и может быть доступен всем.
# Проверка подписи выполняется с помощью публичного ключа:
# если подпись проверяется успешно с использованием публичного ключа,
# это означает, что данные подписаны с использованием соответствующего
# приватного ключа и не были изменены после подписания.

def generate_key_pair():  # Определение функции для генерации ключевой пары
    private_key = dsa.generate_private_key(key_size=1024, backend=default_backend())  # Генерация приватного ключа DSA
    public_key = private_key.public_key()  # Получение публичного ключа из приватного
    return private_key, public_key  # Возвращение сгенерированных ключей

def sign_message(private_key, message):  # Определение функции для подписи сообщения
    signature = private_key.sign(  # Подписание сообщения приватным ключом
        message,  # Сообщение, которое требуется подписать
        hashes.SHA256()  # Используемая хеш-функция SHA-256
    )
    return signature  # Возвращение подписи

def verify_signature(public_key, message, signature):  # Определение функции для проверки подписи
    try:
        public_key.verify(  # Проверка подписи с использованием публичного ключа
            signature,  # Подпись, которую нужно проверить
            message,  # Оригинальное сообщение
            hashes.SHA256()  # Используемая хеш-функция SHA-256
        )
        return True  # Если подпись верна, возвращаем True
    except InvalidSignature:
        return False  # Если подпись недействительна, возвращаем False

def read_file(file_path):  # Определение функции для чтения файла
    with open(file_path, "rb") as file:  # Открытие файла для чтения в бинарном режиме
        return file.read()  # Возвращение содержимого файла

def write_file(file_path, data):  # Определение функции для записи данных в файл
    with open(file_path, "wb") as file:  # Открытие файла для записи в бинарном режиме
        file.write(data)  # Запись данных в файл

# Генерация ключевой пары
private_key, public_key = generate_key_pair()  # Генерация ключевой пары

# Чтение файла, который нужно подписать
file_path = "test.txt"  # Путь к файлу, который нужно подписать
message = read_file(file_path)  # Чтение содержимого файла

# Подписание файла
signature = sign_message(private_key, message)  # Подписание файла

# Запись подписи в файл
signature_file_path = "signature.sig"  # Путь к файлу, в который будет записана подпись
write_file(signature_file_path, signature)  # Запись подписи в файл

print(public_key)
print(private_key)
# Проверка подписи
signature_to_verify = read_file(signature_file_path)  # Чтение подписи из файла
is_valid_signature = verify_signature(public_key, message, signature_to_verify)  # Проверка подписи
if is_valid_signature:  # Если подпись верна
    print("Подпись верна.")  # Вывод сообщения о верности подписи
else:  # Если подпись недействительна
    print("Подпись неверна.")  # Вывод сообщения о недействительности подписи

# Приватный ключ используется для создания цифровой подписи данных.
# Только владелец приватного ключа может создавать подписи, и он
# должен хранить свой приватный ключ в безопасном месте, так как его
# компрометация может позволить злоумышленникам создавать поддельные подписи от имени владельца.

# Публичный ключ используется для проверки цифровой подписи.
# Он распространяется открыто и может быть доступен всем.
# Проверка подписи выполняется с помощью публичного ключа:
# если подпись проверяется успешно с использованием публичного ключа,
# это означает, что данные подписаны с использованием соответствующего
# приватного ключа и не были изменены после подписания.

def generate_key_pair():  # Определение функции для генерации ключевой пары
    private_key = dsa.generate_private_key(key_size=1024, backend=default_backend())  # Генерация приватного ключа DSA
    public_key = private_key.public_key()  # Получение публичного ключа из приватного
    return private_key, public_key  # Возвращение сгенерированных ключей

def sign_message(private_key, message):  # Определение функции для подписи сообщения
    signature = private_key.sign(  # Подписание сообщения приватным ключом
        message,  # Сообщение, которое требуется подписать
        hashes.SHA256()  # Используемая хеш-функция SHA-256
    )
    return signature  # Возвращение подписи

def verify_signature(public_key, message, signature):  # Определение функции для проверки подписи
    try:
        public_key.verify(  # Проверка подписи с использованием публичного ключа
            signature,  # Подпись, которую нужно проверить
            message,  # Оригинальное сообщение
            hashes.SHA256()  # Используемая хеш-функция SHA-256
        )
        return True  # Если подпись верна, возвращаем True
    except InvalidSignature:
        return False  # Если подпись недействительна, возвращаем False

def read_file(file_path):  # Определение функции для чтения файла
    with open(file_path, "rb") as file:  # Открытие файла для чтения в бинарном режиме
        return file.read()  # Возвращение содержимого файла

def write_file(file_path, data):  # Определение функции для записи данных в файл
    with open(file_path, "wb") as file:  # Открытие файла для записи в бинарном режиме
        file.write(data)  # Запись данных в файл

# Генерация ключевой пары
private_key, public_key = generate_key_pair()  # Генерация ключевой пары

# Чтение файла, который нужно подписать
file_path = "test.txt"  # Путь к файлу, который нужно подписать
message = read_file(file_path)  # Чтение содержимого файла

# Подписание файла
signature = sign_message(private_key, message)  # Подписание файла

# Запись подписи в файл
signature_file_path = "signature.sig"  # Путь к файлу, в который будет записана подпись
write_file(signature_file_path, signature)  # Запись подписи в файл

print(public_key)
print(private_key)
# Проверка подписи
signature_to_verify = read_file(signature_file_path)  # Чтение подписи из файла
is_valid_signature = verify_signature(public_key, message, signature_to_verify)  # Проверка подписи
if is_valid_signature:  # Если подпись верна
    print("Подпись верна.")  # Вывод сообщения о верности подписи
else:  # Если подпись недействительна
    print("Подпись неверна.")  # Вывод сообщения о недействительности подписи
