from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import os


def encrypt_flag(flag):
 
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC)  
    padded_flag = pad(flag.encode(), AES.block_size)
    ciphertext = cipher.encrypt(padded_flag)
    return key, cipher.iv, ciphertext

with open('flag.txt', 'r') as file:
    flag = file.read().strip()

key, iv, ciphertext = encrypt_flag(flag)

with open('encrypted_flag.bin', 'wb') as file:
    file.write(iv + ciphertext)


print(f"AES Key (hex): {key.hex()}")
print(f"Ciphertext (hex): {ciphertext.hex()}")
print("The encrypted flag has been saved to 'encrypted_flag.bin'.")
