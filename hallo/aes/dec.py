from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Path to the binary file
file_path = 'flag.bin'

# Read the encrypted file directly
with open(file_path, 'rb') as file:
    data = file.read()

# Split data into IV and ciphertext
iv = data[:16]  # First 16 bytes are the IV
ciphertext = data[16:]  # The rest is the ciphertext

# Provided AES Key (in hexadecimal)
key_hex = "1d102d0acc81689fb580eee5155a8f29"
key = bytes.fromhex(key_hex)

# Initialize the AES cipher in CBC mode for decryption
cipher = AES.new(key, AES.MODE_CBC, iv)

# Decrypt and unpad the ciphertext to retrieve the original flag
padded_flag = cipher.decrypt(ciphertext)
flag = unpad(padded_flag, AES.block_size)

print("Decrypted Flag:", flag.decode())
