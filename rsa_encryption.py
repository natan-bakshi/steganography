import pyinputplus as pyip
from rsa_generate import *


def get_ord(character):
    char_ord = str(ord(character))
    if len(char_ord) == 2:
        char_ord = "0" + char_ord
    return char_ord

def validate_tuple(text):
    try:
        return tuple(map(int, text.split(',')))  # Convert input to a tuple of integers
    except ValueError:
        raise Exception("Input must be a comma-separated list of integers.")


BLOCK_SIZE = 2


def rsa_encrypt(text):
    print("Do you need to generate a public and private key?")
    generate = pyip.inputMenu(['yes', 'no'], numbered=True)
    if generate == "yes":
        keys = generate_rsa_keys()
        for key, value in keys.items():
            print(f"{key}: {value}")
            key = keys["Public key"]
    else:
        key = pyip.inputCustom(validate_tuple, prompt="Enter public key (comma-separated): ")

    length = len(text)
    pad = ' '
    padding_length = BLOCK_SIZE - length % BLOCK_SIZE if length % BLOCK_SIZE != 0 else 0
    text = text + (pad * padding_length)
    len_message = len(text)
    out = []
    for i in range(0 , len_message - 1, BLOCK_SIZE):
        block_ord = ""
        for j in range(i, i + BLOCK_SIZE):
            char_ord = get_ord(text[j])
            block_ord += char_ord
        new_char = str(pow(int(block_ord), key[0], key[1]))
        out.append(new_char)
    out = " ".join(out)
    return out

def rsa_decrypt(enc_text):
    key = pyip.inputCustom(validate_tuple, prompt="Enter private key (comma-separated): ")
    out = ""
    enc_numbers = list(map(int, enc_text.split()))  # Convert space-separated string to integers
    for num in enc_numbers:
        joined_chars = str(pow(num, key[0], key[1]))
        for i in range(0, len(joined_chars) - 1, 3):
            new_char = chr(int(joined_chars[i:i + 3]))
            out += new_char
    return out

prv_key = (8736751, 69336961)
pub_key = (1999, 69336961)



