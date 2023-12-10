import os
import pyaes
from pathlib import Path

def decrypt_file(file_path, key):
    with open(file_path, "rb") as ransom_file:
        crypto_data = ransom_file.read()

    os.remove(file_path)

    aes = pyaes.AESModeOfOperationCTR(key)
    decrypted_data = aes.decrypt(crypto_data)

    original_file_path = Path(file_path).with_suffix("") 
    with open(original_file_path, "wb") as original_file:
        original_file.write(decrypted_data)

def decrypt_directory(directory_path, key):
    path = Path(directory_path)
    for ransom_file_path in path.glob("*.ransomwaretroll"):
        decrypt_file(ransom_file_path, key)

if __name__ == "__main__":
    key = b"testeransomwares"

    target = input("Digite o caminho do arquivo ou diretório a ser descriptografado: ")

    if os.path.isfile(target):
        decrypt_file(target, key)
        print(f"Arquivo {target} descriptografado com sucesso!")
    elif os.path.isdir(target):
        decrypt_directory(target, key)
        print(f"Arquivos em {target} descriptografados com sucesso!")
    else:
        print("Caminho inválido. Certifique-se de inserir o caminho correto para o arquivo ou diretório.")
