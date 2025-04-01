import pyinputplus as pyip
from references import encryption_choices, deciphering_choices
from rsa_generate import *
from lsb_steganography import *

def main():
    starter = True
    while starter:
        print('What would you like to do?')
        choice = pyip.inputMenu(FIRST_CHOICES, numbered=True)

        if choice == 'Encrypt a text file':
            starter = encryption_choices()

        if choice == 'Decrypt a text file':
            starter = deciphering_choices()

        if choice == 'Hide a message in an image':
            starter = lsb('hide')

        if choice == 'Extract a message from an image':
            starter = lsb('expose')

        if choice == 'Create RSA keys':
            generate_rsa_keys()


        if choice == 'Exit':
            starter = False


main()