import math
import pyinputplus as pyip
import re

from sympy.codegen.ast import pointer_const


def transposition(text:str, key:list) -> str:
    # print(key)
    len_text = len(text)
    columns = len(key)
    lines = math.ceil(len_text / columns)
    pad = ' '
    padding_length = columns - len_text % columns if len_text % columns != 0 else 0
    text = text + (pad * padding_length)
    matrix = [[None] * columns for _ in range(lines)]
    pointer = 0
    for line in range(lines):
        for column in key:
            # print(column)
            matrix[line][column] = (text[pointer])
            pointer += 1
                # matrix.append(list(text[column * lines:(column + 1) * lines]))
    # print(matrix)

    new_text = ""
    for char in range(columns):
        for line in range(lines):
           new_text += matrix[line][char]

    return new_text


def transposition_decode(text:str, key:list) -> str:
    # print(key)
    len_text = len(text)
    columns = len(key)
    lines = math.ceil(len_text / columns)
    pad = ' '
    padding_length = columns - len_text % columns if len_text % columns != 0 else 0
    text = text + (pad * padding_length)
    matrix = [[None] * columns for _ in range(lines)]
    pointer = 0
    for column in range(columns):
        for line in range(lines):
            matrix[line][column] = (text[pointer])
            pointer += 1
            # matrix.append(list(text[column * lines:(column + 1) * lines]))
    # print(matrix)

    new_text = ""
    for line in range(lines):
        for char in key:
           new_text += matrix[line][char]

    return new_text



# def transposition_cipher_text(text:str) -> str:
#     key = pyip.inputInt("Please enter the key: ")
#     return transposition_text(text, key)
#
# def transposition_decipher_text(text:str) -> str:
#     key = pyip.inputInt("Please enter the key: ")
#     columns = math.ceil(len(text) / key)
#     return transposition_text(text, columns)


def transposition_cipher_text(text:str) -> str:
    key = input("Please enter the key: ")
    validation = bool(re.fullmatch(r'[A-Za-z0-9]+', key) and len(key) > 2)
    while not validation:
        print("A key can only contain English letters and numbers and a minimum of two characters\n")
        key = input("Please enter the key: ")

    sorted_key = sorted(range(len(key)), key=lambda i: key[i])
    return transposition(text, sorted_key)



def transposition_decipher_text(text:str) -> str:
    key = input("Please enter the key: ")
    validation = bool(re.fullmatch(r'[A-Za-z0-9]+', key) and len(key) > 2)
    while not validation:
        print("A key can only contain English letters and numbers and a minimum of two characters\n")
        key = input("Please enter the key: ")

    sorted_key = sorted(range(len(key)), key=lambda i: key[i])

    return transposition_decode(text, sorted_key)

