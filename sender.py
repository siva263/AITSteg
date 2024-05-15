import sys
from embed import embedFunc
from extract import extractFunc
from AES import encrypt, decrypt
import pygetwindow as gw

# SM=input("Enter secret message:")
# CM=input("Enter cover message:")
# password=input("Enter password for encryption:")

def copy_to_clipboard(text):
    window = gw.getWindowsWithTitle('Your Window Title')[0]  # Adjust window title as needed
    window.copyToClipboard(text)

def hideFunc(SM, password, CM):
    encSM = encrypt(password, SM)
    print("Encrypted secret message going to send:", encSM)
    CM_HM = embedFunc(encSM, CM)
    print("Cover message=", CM_HM)
    copy_to_clipboard(CM_HM)
    return CM_HM

# Example usage:
# SM = input("Enter secret message:")
# CM = input("Enter cover message:")
# password = input("Enter password for encryption:")
# hideFunc(SM, password, CM)
