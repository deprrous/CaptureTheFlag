# cipher.py

# Caesar Cipher Encryption
def caesar_encrypt(text, shift):
    return ''.join(chr((ord(char) + shift - 65) % 26 + 65) if char.isalpha() else char for char in text)

# Caesar Cipher Decryption
def caesar_decrypt(text, shift):
    return ''.join(chr((ord(char) - shift - 65) % 26 + 65) if char.isalpha() else char for char in text)

# Affine Cipher Encryption
def affine_encrypt(text, a, b):
    return ''.join(chr(((a * (ord(char) - 65) + b) % 26) + 65) if char.isalpha() else char for char in text)

# Affine Cipher Decryption
def affine_decrypt(text, a, b):
    a_inv = pow(a, -1, 26)  # Modular multiplicative inverse of a modulo 26
    return ''.join(chr(((a_inv * ((ord(char) - 65) - b)) % 26) + 65) if char.isalpha() else char for char in text)
