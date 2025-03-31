import pyinputplus as pyip

def caesar_text(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = key % 26
            new_char = chr(((ord(char.lower()) - ord('a') + shift_amount) % 26) + ord('a'))
            if char.isupper():
                new_char = new_char.upper()
            result += new_char
        else:
            result += char
    return result


def caesar_cipher_text(text):
    key = pyip.inputInt("Please enter the key: ")
    return caesar_text(text, key)

def caesar_decipher_text(text):
    key = pyip.inputInt("Please enter the key: ")
    return caesar_text(text, -key)




