import random
import string

def generate_monoalphabetic_key():
    alphabet = list(string.ascii_uppercase)
    shuffled_alphabet = alphabet.copy()
    random.shuffle(shuffled_alphabet)
    key = ''.join(shuffled_alphabet)
    return key

def monoalphabetic_encrypt(plain_text, key):
    alphabet = string.ascii_uppercase
    plain_text = plain_text.upper()
    cipher_text = ''

    for char in plain_text:
        if char in alphabet:
            idx = alphabet.index(char)
            cipher_text += key[idx]
        else:
            cipher_text += char

    return cipher_text

def monoalphabetic_decrypt(cipher_text, key):
    alphabet = string.ascii_uppercase
    cipher_text = cipher_text.upper()
    plain_text = ''

    for char in cipher_text:
        if char in key:
            idx = key.index(char)
            plain_text += alphabet[idx]
        else:
            plain_text += char

    return plain_text

# Generate a random key
key = generate_monoalphabetic_key()
print(f'Generated Key: {key}')

# Encrypt a message
plain_text = 'HELLO WORLD'
cipher_text = monoalphabetic_encrypt(plain_text, key)
print(f'Encrypted: {cipher_text}')

# Decrypt the message
decrypted_text = monoalphabetic_decrypt(cipher_text, key)
print(f'Decrypted: {decrypted_text}')
