# реализация рюкзачной криптосистемы

from random import randint

# класс генерации публичного и приватного ключа
class KeyPair:
    def __init__(self, n=128):
        self.public_key, self.private_key = self.Generate(n)

    # генерация ключей
    @staticmethod
    def Generate(n):
        # создание случайной последовательности
        sequence = [randint(1, 1000) for _ in range(n)]
        # публичный ключ - список, в котором каждый элемент равен 2 в степени соответствующего числа из последовательности
        public_key = [2 ** x for x in sequence]
        # приватный ключ вычисляется - сумма всех элементов публичного ключа.
        private_key = sum(public_key)
        return public_key, private_key

    # возвращение публичного ключа
    def GetPublicKey(self):
        return self.public_key

    # возврщание приватного ключа
    def GetPrivateKey(self):
        return self.private_key

# класс шифрования сообщения
class CipherText:
    def __init__(self, message, public_key):
        self.cipher_text = self.Encrypt(message, public_key)

    # шифрование сообщения
    @staticmethod
    def Encrypt(message, public_key):
        cipher_text = []
        # для каждого символа в сообщении
        for char in message:
            # добавление в список значения - вычисленного кода символа и умноженного кода символа на элемент публичного ключа
            cipher_text.append(ord(char) * public_key[len(cipher_text) % len(public_key)])
        return cipher_text

    # возвращение зашифрованного сообщения
    def Get(self):
        return self.cipher_text

# класс расшифровки зашифрованного сообщения с использованием приватного ключа
class PrivateKey:
    def __init__(self, private_key):
        self.private_key = private_key

    def DecipherString(self, cipher_text):
        # пустая строка
        original_message = ""
        # для каждого зашифрованного символа
        for encrypted_char in cipher_text:
            # вычисление кода символа
            char_code = encrypted_char // self.private_key  # Используем операцию модуля
            # преобразование в символ (из кода символа) и добавление к пустому сообщению
            original_message += chr(char_code)
        return original_message

# функция записи приватного ключа в файл
def SavePrivateKeyToFile(private_key, filename="private_key.txt"):
    with open(filename, "w") as file:
        file.write(str(private_key))
    print(f"Приватный ключ сохранен в файл {filename}")

# функция записи расшифрованного сообщения в файл
def SaveDecryptedMessageToFile(decrypted_message, filename="./decrypted_message.txt"):
    with open(filename, "w") as file:
        file.write(message)
    print(f"Расшифрованное сообщение сохранено в файл {filename}")

# генерация ключей
key_pair = KeyPair()
print("Публичный ключ:", key_pair.GetPublicKey())

# сообщение
message = "Hello, World!"
# шифрование сообщения
cipher_text = CipherText(message, key_pair.GetPublicKey()).Get()
private_key = PrivateKey(key_pair.GetPrivateKey())
# расшифрование сообщения
decrypted_message = private_key.DecipherString(cipher_text)
print("Зашифрованное сообщение:", cipher_text)
print("Расшифрованное сообщение:", decrypted_message)

# запись в файл приватного ключа и расшифрованного сообщения
SavePrivateKeyToFile(key_pair.GetPrivateKey())
SaveDecryptedMessageToFile(decrypted_message)
