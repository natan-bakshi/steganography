import math
import pyinputplus as pyip

def transposition_cipher_text(text:str, key:int) -> str:
    length = len(text)
    columns = math.ceil(length / key)
    pad = ' '
    padding_length = key - length % key if length % key != 0 else 0
    text = text + (pad * padding_length)
    matrix = []
    for column in range(key):
        matrix.append(list(text[column * columns:(column + 1) * columns]))
    print(matrix)

    new_text = ""
    for char in range(columns):
        for column in range(key):
           new_text += matrix[column][char]

    return new_text


def transposition_decipher_text(text:str, key:int) -> str:
    columns = math.ceil(len(text) / key)
    return transposition_cipher_text(text, columns)





def transposition_method_choices(mode):
    while True:
        path = input("Enter the file path: ")
        try:
            with open(path, "r", encoding="utf-8") as file:
                text = file.read()
                break
        except:
            print("The path is incorrect")

    key = pyip.inputInt("Please enter the key number: ")

    if mode == 'encryption':
        return caesar_cipher(text, key)
    if mode == 'deciphering':
        return caesar_decipher(text, key)