import pyinputplus as pyip
from config import  *


def main():
    print('What would you like to do?')
    choice = pyip.inputMenu(FIRST_CHOICES, numbered=True)

    if choice == 'Encrypt a text file':
        encryption_choice = pyip.inputMenu(ENCRYPTION_CHOICES, numbered=True)
        if encryption_choice == 'exit':
            pass

    if choice == 'Decrypt a text file':
        pass

    if choice == 'Hide a message in an image':
        pass

    if choice == 'Extract a message from an image':
        pass

    if choice == 'Exit':
        pass


main()