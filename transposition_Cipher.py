import math

def transposition_cipher_text(text:str, columns:int) -> str:
    length = len(text)
    rows = math.ceil(length / columns)
    pad = ' '
    padding_length = columns - length % columns if length % columns != 0 else 0
    text = text + (pad * padding_length)
    matrix = []
    for column in range(columns):
        matrix.append(list(text[column * rows:(column + 1) * rows]))
    print(matrix)

    new_text = ""
    for char in range(rows):
        for column in range(columns):
           new_text += matrix[column][char]

    return new_text








transposition_cipher_text("natan bakshi hamelech", 6)