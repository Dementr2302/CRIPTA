from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
import os

def generate_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

def sign_file(private_key, file_path):
    with open(file_path, 'rb') as f:
        file_data = f.read()

    signature = private_key.sign(
        file_data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    with open(file_path + '.sig', 'wb') as signature_file:
        signature_file.write(signature)

def verify_signature(public_key, file_path, signature_path):
    with open(file_path, 'rb') as f:
        file_data = f.read()

    with open(signature_path, 'rb') as signature_file:
        signature = signature_file.read()

    try:
        public_key.verify(
            signature,
            file_data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print("Signature is valid.")
    except:
        print("Signature is invalid.")

# Генерация ключевой пары
private_key, public_key = generate_key_pair()

# Подпись файла
file_to_sign = 'example.txt'
with open(file_to_sign, 'w') as f:
    f.write("This is some data.")

sign_file(private_key, file_to_sign)

# Проверка подписи
signature_file = file_to_sign + '.sig'
verify_signature(public_key, file_to_sign, signature_file)

# Попытка изменить файл
with open(file_to_sign, 'a') as f:
    f.write("\nThis data is added to modify the file.")

# Проверка подписи после изменения файла
verify_signature(public_key, file_to_sign, signature_file)
