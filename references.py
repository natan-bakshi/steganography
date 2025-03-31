from caesar_cipher import  *
from config import  *
from transposition_cipher import *
import pyinputplus as pyip
import os
from rsa_encryption import *


def cipher(model, filename, text):
    ciphered_text = ""
    if model == "caesar":
        ciphered_text = caesar_cipher_text(text)
    if model == "transposition":
        ciphered_text = transposition_cipher_text(text)
    if model == 'RSA':
        ciphered_text = rsa_encrypt(text)
    file_path = f"{model}_encrypted_{filename}.enc"
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(ciphered_text)
    print(f"Encrypted file saved as {file_path}\n")


def decipher(model, filename, text):
    decrypted_text = ""
    if model == "caesar":
        decrypted_text = caesar_decipher_text(text)
    if model == "transposition":
        decrypted_text = transposition_decipher_text(text)
    if model == 'RSA':
        decrypted_text = rsa_decrypt(text)
    file_path = f"{model}_deciphered_{filename}.txt"
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(decrypted_text)
    print(f"Encrypted file saved as {model}_deciphered_{file_path}\n")


def get_parameters(model):
    while True:
        path = input("""Enter the file path: 
To return press 'back', To end press 'exit'
""")
        if path == "back":
            return True
        if path == "exit":
            return False
        try:
            with open(path, "r", encoding="utf-8") as file:
                text = file.read()
                break
        except:
            print("The path is incorrect")

    filename = os.path.splitext(os.path.basename(path))[0]

    if model == 'caesar_cipher':
        cipher('caesar', filename, text)
    if model == 'caesar_decipher':
        decipher('caesar', filename, text)
    if model == 'transposition_cipher':
        cipher('transposition', filename, text)
    if model == 'transposition_decipher':
        decipher('transposition', filename, text)
    if model == 'RSA_cipher':
        cipher('RSA', filename, text)
    if model == 'RSA_decipher':
        decipher('RSA', filename, text)

    return True


def encryption_choices():
    encryption_choice = pyip.inputMenu(ENCRYPTION_CHOICES, numbered=True)
    if encryption_choice == 'exit':
        return False
    if encryption_choice == 'Back to main menu':
        return True
    return get_parameters(encryption_choice)


def deciphering_choices():
    decryption_choice = pyip.inputMenu(DECIPHERING_CHOICES, numbered=True)
    if decryption_choice == 'exit':
        return False
    if decryption_choice == 'Back to main menu':
        return True
    return get_parameters(decryption_choice)


