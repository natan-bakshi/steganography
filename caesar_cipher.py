import pyinputplus as pyip


def caesar_cipher_text(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr(((ord(char.lower()) - ord('a') + shift_amount) % 26) + ord('a'))
            if char.isupper():
                new_char = new_char.upper()
            result += new_char
        else:
            result += char
    return result


def caesar_decipher_text(text, shift):
    return caesar_cipher_text(text, -shift)


# def caesar_cipher(text, shift):
#     ciphered_text = caesar_cipher_text(text, shift)
#     file_path = "secret.enc"
#     with open(file_path, "w", encoding="utf-8") as file:
#         file.write(ciphered_text)
#     print(f"Encrypted file saved as {file_path}")
#
#
# def caesar_decipher(text, shift):
#     decrypted_text = caesar_decipher_text(text, shift)
#     file_path = "text.txt"
#     with open(file_path, "w", encoding="utf-8") as file:
#         file.write(decrypted_text)
#     print(f"Encrypted file saved as {file_path}")


# def caesar_method_choices(mode):
#     while True:
#         path = input("Enter the file path: ")
#         try:
#             with open(path, "r", encoding="utf-8") as file:
#                 text = file.read()
#                 break
#         except:
#             print("The path is incorrect")
#
#     key = pyip.inputInt("Please enter the key number: ")
#
#     if mode == 'encryption':
#         return caesar_cipher(text, key)
#     if mode == 'deciphering':
#         return caesar_decipher(text, key)


