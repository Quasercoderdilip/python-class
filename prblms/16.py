import random
import string




def encrypt(s):
    msg = input('Enter a message to encrypt : ')
    cipher_msg = '';







chars = '' + string.punctuation + string.digits + string.ascii_letters
chars = list(chars);
keys = chars.copy();

random.shuffle(keys);