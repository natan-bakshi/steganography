from PIL import Image
import numpy as np
import os

def text_to_bits(text):
    return ''.join(format(ord(c), '08b') for c in text)


def bits_to_text(bits):
    chars = [bits[i:i + 8] for i in range(0, len(bits), 8)]
    return ''.join(chr(int(c, 2)) for c in chars)


def encode_image(image_path, text):
    print("Working on your request...\n")
    # Ensure the image is converted to PNG format internally
    image = Image.open(image_path).convert("RGB")

    # Convert JPG to PNG before processing (to avoid compression issues)
    if image_path.lower().endswith(".jpg") or image_path.lower().endswith(".jpeg"):
        temp_png_path = image_path.rsplit(".", 1)[0] + ".png"
        image.save(temp_png_path, "PNG")
        image_path = temp_png_path  # Use converted PNG

    # Process as usual
    pixels = np.array(image)

    # Read the secret message
    # with open(text_path, 'r') as file:
    #     text = file.read()

    message_bits = text_to_bits(text)
    message_length = len(message_bits)
    length_bits = format(message_length, '032b')  # Store length in first 32 bits
    full_bits = length_bits + message_bits

    height, width, _ = pixels.shape
    max_bits = height * width * 3

    if len(full_bits) > max_bits:
        raise ValueError("Message too large to hide in image")

    bit_index = 0
    for i in range(height):
        for j in range(width):
            for k in range(3):  # Iterate over R, G, B
                if bit_index < len(full_bits):
                    pixel_bin = format(pixels[i, j, k], '08b')
                    pixel_bin = pixel_bin[:-1] + full_bits[bit_index]
                    pixels[i, j, k] = int(pixel_bin, 2)
                    bit_index += 1

    output_path = os.path.splitext(image_path)[0]
    output_path += "_encoded.png"
    encoded_image = Image.fromarray(pixels)
    encoded_image.save(output_path, "PNG")  # Always save as PNG to prevent loss
    print("Message successfully hidden in", output_path,"\n")


def decode_image(image_path):
    print("Working on your request...\n")
    image = Image.open(image_path)
    image = image.convert("RGB")
    pixels = np.array(image)

    height, width, _ = pixels.shape

    bits = ""
    for i in range(height):
        for j in range(width):
            for k in range(3):
                bits += str(pixels[i, j, k] & 1)  # Extract LSB

    message_length = int(bits[:32], 2)
    message_bits = bits[32:32 + message_length]
    secret_message = bits_to_text(message_bits)

    output_text_path = os.path.splitext(image_path)[0]
    output_text_path += "_decoded.txt"
    with open(output_text_path, 'w') as file:
        file.write(secret_message)

    print("Message successfully extracted to", output_text_path, "\n")


def lsb(mode):
    while True:
        image_path = input("""Enter the image path: 
To return press 'back', To end press 'exit'
    """).strip("\"'")
        if image_path == "back":
            return True
        if image_path == "exit":
            return False
        try:
            image = Image.open(image_path).convert("RGB")
            break
        except:
            print("The path is incorrect")

    if mode == 'hide':
        while True:
            path = input("""Enter the text path:
To return press 'back', To end press 'exit'""").strip("\"'")
            if image_path == "back":
                return True
            if image_path == "exit":
                return False
            try:
                with open(path, "r") as file:
                    text = file.read()
                    break
            except:
                print("The path is incorrect")
        encode_image(image_path, text)
    if mode == 'expose':
        decode_image(image_path)

    return True


img_path = "/home/mefathim-77/Pictures/austrian castle.jpeg"
text_path = r"C:\Users\natib\OneDrive\שולחן העבודה\encrypted.txt"
enc_path = r"C:\Users\natib\OneDrive\שולחן העבודה\encrypted.png"

# encode_image(img_path, text_path, enc_path)
# decode_image(enc_path, text_path)
# Example usage
# encode_image("cover.png", "message.txt", "stego.png")
# decode_image("stego.png", "extracted_message.txt")
