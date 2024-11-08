# modes.py
from cipher import *

def encrypt(text, mode, cipher_type, key, iv_or_nonce):
    if mode == 'CBC' and cipher_type == 'Caesar':
        return cbc_encrypt_caesar(text, key, iv_or_nonce)
    elif mode == 'OFB' and cipher_type == 'Affine':
        return ofb_encrypt_affine(text, key[0], key[1], iv_or_nonce)
    elif mode == 'CTR' and cipher_type == 'Caesar':
        return ctr_encrypt_caesar(text, key, iv_or_nonce)
    elif mode == 'CBC' and cipher_type == 'Affine':
        return cbc_encrypt_affine(text, key[0], key[1], iv_or_nonce)
    elif mode == 'CTR' and cipher_type == 'Affine':
        return ctr_encrypt_affine(text, key[0], key[1], iv_or_nonce)
    else:
        raise ValueError(f"Invalid mode {mode} or cipher type {cipher_type}.")

def decrypt(ciphertext, mode, cipher_type, key, iv_or_nonce):
    if mode == 'CBC' and cipher_type == 'Caesar':
        return cbc_decrypt_caesar(ciphertext, key, iv_or_nonce)
    elif mode == 'OFB' and cipher_type == 'Affine':
        return ofb_decrypt_affine(ciphertext, key[0], key[1], iv_or_nonce)
    elif mode == 'CTR' and cipher_type == 'Caesar':
        return ctr_decrypt_caesar(ciphertext, key, iv_or_nonce)
    elif mode == 'CBC' and cipher_type == 'Affine':
        return cbc_decrypt_affine(ciphertext, key[0], key[1], iv_or_nonce)
    elif mode == 'CTR' and cipher_type == 'Affine':
        return ctr_decrypt_affine(ciphertext, key[0], key[1], iv_or_nonce)
    else:
        raise ValueError(f"Invalid mode {mode} or cipher type {cipher_type}.")

# CBC Mode with Caesar Cipher
def cbc_encrypt_caesar(text, shift, iv):
    ciphertext = ''
    previous_block = iv
    
    for char in text:
        xor_result = chr((ord(char) ^ ord(previous_block)) % 256)
        encrypted_char = caesar_encrypt(xor_result, shift)
        ciphertext += encrypted_char
        previous_block = encrypted_char
    
    return ciphertext

def cbc_decrypt_caesar(ciphertext, shift, iv):
    decrypted_text = ''
    previous_block = iv
    
    for char in ciphertext:
        decrypted_char = caesar_decrypt(char, shift)
        original_char = chr((ord(decrypted_char) ^ ord(previous_block)) % 256)
        decrypted_text += original_char
        previous_block = char
    
    return decrypted_text

# OFB Mode with Affine Cipher
def ofb_encrypt_affine(text, a, b, iv):
    ciphertext = ''
    feedback = iv
    
    for char in text:
        feedback = affine_encrypt(feedback, a, b)
        encrypted_char = chr((ord(char) ^ ord(feedback)) % 256)
        ciphertext += encrypted_char
    
    return ciphertext

def ofb_decrypt_affine(ciphertext, a, b, iv):
    decrypted_text = ''
    feedback = iv
    
    for char in ciphertext:
        feedback = affine_encrypt(feedback, a, b)
        decrypted_char = chr((ord(char) ^ ord(feedback)) % 256)
        decrypted_text += decrypted_char
    
    return decrypted_text

# CTR Mode with Caesar Cipher
def ctr_encrypt_caesar(text, shift, nonce):
    ciphertext = ''
    
    for i, char in enumerate(text):
        counter_value = nonce + i
        encrypted_counter = caesar_encrypt(chr(counter_value % 256), shift)
        encrypted_char = chr((ord(char) ^ ord(encrypted_counter)) % 256)
        ciphertext += encrypted_char
    
    return ciphertext

def ctr_decrypt_caesar(ciphertext, shift, nonce):
    decrypted_text = ''
    
    for i, char in enumerate(ciphertext):
        counter_value = nonce + i
        encrypted_counter = caesar_encrypt(chr(counter_value % 256), shift)
        decrypted_char = chr((ord(char) ^ ord(encrypted_counter)) % 256)
        decrypted_text += decrypted_char
    
    return decrypted_text

# CTR Mode with Affine Cipher
def ctr_encrypt_affine(text, a, b, nonce):
    ciphertext = ''
    
    for i, char in enumerate(text):
        counter_value = nonce + i
        encrypted_counter = affine_encrypt(chr(counter_value % 256), a, b)
        encrypted_char = chr((ord(char) ^ ord(encrypted_counter)) % 256)
        ciphertext += encrypted_char
    
    return ciphertext

def ctr_decrypt_affine(ciphertext, a, b, nonce):
    decrypted_text = ''
    
    for i, char in enumerate(ciphertext):
        counter_value = nonce + i
        encrypted_counter = affine_encrypt(chr(counter_value % 256), a, b)
        decrypted_char = chr((ord(char) ^ ord(encrypted_counter)) % 256)
        decrypted_text += decrypted_char
    
    return decrypted_text
