from caesar_cipher import  *
import pyinputplus as pyip
from config import  *


def encryption_choices():
    encryption_choice = pyip.inputMenu(ENCRYPTION_CHOICES, numbered=True)
    if encryption_choice == 'caesar cipher':
        caesar_method_choices('encryption')
    if encryption_choice == 'exit':
        return False
    return True

def deciphering_choices():
    encryption_choice = pyip.inputMenu(DECIPHERING_CHOICES, numbered=True)
    if encryption_choice == 'caesar_decipher':
        caesar_method_choices('deciphering')
    if encryption_choice == 'exit':
        return False
    return True