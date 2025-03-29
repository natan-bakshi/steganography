from caesar_cipher import  *
from config import  *
from transposition_cipher import *
import pyinputplus as pyip
import os



def cipher(model, filename, text, key):
    ciphered_text = ""
    if model == "caesar":
        ciphered_text = caesar_cipher_text(text, key)
    if model == "transposition":
        ciphered_text = transposition_cipher_text(text, key)
    file_path = f"{filename}.enc"
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(ciphered_text)
    print(f"Encrypted file saved as {file_path}")


def decipher(model, filename, text, key):
    decrypted_text = ""
    if model == "caesar":
        decrypted_text = caesar_decipher_text(text, key)
    if model == "transposition":
        decrypted_text = transposition_decipher_text(text, key)
    file_path = f"{filename}.txt"
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(decrypted_text)
    print(f"Encrypted file saved as {file_path}")


def get_parameters(model):
    while True:
        path = input("""To return press 'back', To end press 'exit'
Enter the file path: """)
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
    key = pyip.inputInt("Please enter the key number: ")

    if model == 'caesar_cipher':
        cipher('caesar', filename, text, key)
    if model == 'caesar_decipher':
        decipher('caesar', filename, text, key)
    if model == 'transposition_cipher':
        cipher('transposition', filename, text, key)
    if model == 'transposition_decipher':
        decipher('transposition', filename, text, key)

    return True


def encryption_choices():
    encryption_choice = pyip.inputMenu(ENCRYPTION_CHOICES, numbered=True)
    if encryption_choice == 'caesar_cipher':
        return get_parameters('caesar_cipher')
    if encryption_choice == 'transposition_cipher':
        return get_parameters('transposition_cipher')
    if encryption_choice == 'exit':
        return False
    return True


def deciphering_choices():
    encryption_choice = pyip.inputMenu(DECIPHERING_CHOICES, numbered=True)
    if encryption_choice == 'caesar_decipher':
        return get_parameters('caesar_decipher')
    if encryption_choice == 'transposition_decipher':
        return get_parameters('transposition_decipher')
    if encryption_choice == 'exit':
        return False
    return True