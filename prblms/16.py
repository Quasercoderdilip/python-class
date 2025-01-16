import random
import string

# Global variables for consistent key
chars = ' ' + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
keys = chars.copy()
random.shuffle(keys)

# Encryption
def encryption(txt):
    cipher_msg = ''
    for letter in txt:
        if letter in chars:
            index = chars.index(letter)
            cipher_msg += keys[index]
        else:
            cipher_msg += letter  # Handle unknown characters
    # print(f'Original message: {txt}')
    print(f'Encrypted message: {cipher_msg}')
    return cipher_msg

# Decryption
def decryption(txt):
    msg = ''
    for letter in txt:
        if letter in keys:
            index = keys.index(letter)
            msg += chars[index]
        else:
            msg += letter  # Handle unknown characters
    # print(f'Encrypted message: {txt}')
    print(f'Original message: {msg}')
    return msg

# Input and testing
encrypted_message = encryption(input('Enter the message to encrypt: '))
decrypted_message = decryption(input('Enter the message to decrypt: '))
