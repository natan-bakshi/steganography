# Cryptography Toolkit

A comprehensive Python-based toolkit for encryption, decryption, and steganography operations. This project includes multiple cipher implementations, RSA encryption, and LSB steganography for hiding messages in images.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Main Menu](#main-menu)
  - [Encryption Methods](#encryption-methods)
  - [Decryption Methods](#decryption-methods)
  - [Steganography](#steganography)
  - [RSA Key Generation](#rsa-key-generation)
- [Module Details](#module-details)
  - [Caesar Cipher](#caesar-cipher)
  - [Transposition Cipher](#transposition-cipher)
  - [RSA Encryption](#rsa-encryption)
  - [LSB Steganography](#lsb-steganography)
- [File Formats](#file-formats)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Overview

This cryptography toolkit provides various methods for securing text and hiding information. It features a user-friendly command-line interface that guides users through encryption, decryption, and steganography operations. The project supports classical ciphers (Caesar and Transposition), modern cryptography (RSA), and steganography techniques for hiding messages in images.

## Features

- **Multiple Cipher Methods**:
  - Caesar Cipher
  - Transposition Cipher
  - RSA Encryption
- **Steganography**:
  - Hide text messages in images using LSB technique
  - Extract hidden messages from images
- **RSA Key Management**:
  - Generate new RSA key pairs
  - Use existing keys for encryption/decryption
- **File-based Operations**:
  - Process text files for all encryption/decryption operations
  - Save results to new files with appropriate naming

## Installation

### Prerequisites

- Python 3.6+
- Required packages:
  - pyinputplus
  - PIL (Pillow)
  - numpy
  - sympy

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/cryptography-toolkit.git
cd cryptography-toolkit
```

2. Install required packages:
```bash
pip install pyinputplus pillow numpy sympy
```

## Usage

### Main Menu

Run the application using:
```bash
python main.py
```

This will display the main menu with the following options:
1. Encrypt a text file
2. Decrypt a text file
3. Hide a message in an image
4. Extract a message from an image
5. Create RSA keys
6. Exit

### Encryption Methods

To encrypt a file, select option 1 from the main menu, then choose your encryption method:
- Caesar cipher
- Transposition cipher
- RSA cipher

You will be prompted to:
1. Enter the path to the text file you want to encrypt
2. Provide additional parameters specific to the chosen cipher (e.g., key)

### Decryption Methods

To decrypt a file, select option 2 from the main menu, then choose your decryption method:
- Caesar decipher
- Transposition decipher
- RSA decipher

You will be prompted to:
1. Enter the path to the encrypted file
2. Provide the correct key or parameters needed for decryption

### Steganography

#### Hiding a Message
To hide a message in an image:
1. Select option 3 from the main menu
2. Enter the path to your image file (supports various formats, converts to PNG)
3. Enter the path to the text file containing your message

The program will create a new image file with "_encoded" appended to the original filename.

#### Extracting a Message
To extract a hidden message:
1. Select option 4 from the main menu
2. Enter the path to the encoded image

The program will extract the hidden message and save it to a text file with "_decoded" appended to the original filename.

### RSA Key Generation

To generate new RSA keys:
1. Select option 5 from the main menu
2. The program will display a new public and private key pair

## Module Details

### Caesar Cipher

**Module**: `caesar_cipher.py`

The Caesar cipher shifts each character in the text by a given number of positions in the alphabet.

**Functions**:
- `caesar_text(text, key)`: Applies Caesar cipher with the specified key
- `caesar_cipher_text(text)`: Prompts for a key and encrypts text
- `caesar_decipher_text(text)`: Prompts for a key and decrypts text

**Usage Example**:
```python
from caesar_cipher import caesar_cipher_text
encrypted = caesar_cipher_text("Hello World")  # Will prompt for key
```

### Transposition Cipher

**Module**: `transposition_cipher.py`

The Transposition cipher rearranges characters according to a key-based pattern, creating a matrix and reading it in a different order.

**Functions**:
- `transposition(text, key)`: Encrypt using transposition with key list
- `transposition_decode(text, key)`: Decrypt using transposition with key list
- `transposition_cipher_text(text)`: Prompts for key string and encrypts
- `transposition_decipher_text(text)`: Prompts for key string and decrypts

**Key Format**:
The key must contain only English letters and numbers, with a minimum length of 2 characters. The key is converted to a sorted index array internally.

**Usage Example**:
```python
from transposition_cipher import transposition_cipher_text
encrypted = transposition_cipher_text("Hello World")  # Will prompt for key
```

### RSA Encryption

**Modules**: `rsa_encryption.py`, `rsa_generate.py`

Implements RSA public-key cryptography for secure encryption and decryption.

**Functions**:
- `generate_rsa_keys()`: Creates new RSA key pairs
- `rsa_encrypt(text)`: Encrypts text using RSA
- `rsa_decrypt(enc_text)`: Decrypts RSA-encrypted text

**Note**: RSA implementation processes text in blocks of 2 characters for efficiency.

**Usage Example**:
```python
from rsa_encryption import rsa_encrypt
encrypted = rsa_encrypt("Secret message")  # Will prompt for key
```

### LSB Steganography

**Module**: `lsb_steganography.py`

Implements Least Significant Bit (LSB) steganography to hide messages in images without noticeable visual changes.

**Functions**:
- `encode_image(image_path, text)`: Hides text in image
- `decode_image(image_path)`: Extracts hidden text from image
- `lsb(mode)`: Interactive menu for steganography operations

**Supported Image Formats**:
Automatically converts input images to PNG to prevent compression loss.

**Usage Example**:
```python
from lsb_steganography import encode_image, decode_image
encode_image("example.jpg", "This is a hidden message")
```

## File Formats

- **Input Text Files**: Any text file (.txt preferred)
- **Encrypted Files**: Saved with `.enc` extension
- **Decrypted Files**: Saved with `.txt` extension
- **Steganography Images**: 
  - Input: Various formats (JPG, PNG, etc.)
  - Output: Always PNG to preserve data integrity

## Examples

### Caesar Cipher Encryption

1. Create a text file `message.txt` with your secret message
2. Run the program and select "Encrypt a text file"
3. Choose "caesar_cipher"
4. Enter the path to `message.txt`
5. Enter a key (e.g., 3)
6. The encrypted file will be saved as `caesar_encrypted_message.enc`

### Hiding a Message in an Image

1. Create a text file `secret.txt` with your message
2. Prepare an image file (e.g., `cover.jpg`)
3. Run the program and select "Hide a message in an image"
4. Enter the path to `cover.jpg`
5. Enter the path to `secret.txt`
6. The steganographic image will be saved as `cover_encoded.png`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
