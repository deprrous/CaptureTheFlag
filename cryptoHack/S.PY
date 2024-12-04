from Crypto.Cipher import AES
import binascii

# Your variables
shared_secret = 0x05734ccafa89c4efad49184b6b40bce7f6cc293042272cb35da12a56d095dd4a
iv = 'a1efce8fa97b59a44e2193df0a4b539e'
ciphertext = '65df69b71f58664a02c2dd7c6053e363'

# Convert shared secret (key) to 32-byte hex and then to bytes
key = shared_secret.to_bytes(32, byteorder='big')

# Convert IV and ciphertext from hex to bytes
iv_bytes = bytes.fromhex(iv)
ciphertext_bytes = bytes.fromhex(ciphertext)

# Set up the AES cipher in CBC mode
cipher = AES.new(key, AES.MODE_CBC, iv_bytes)

# Decrypt the ciphertext (don't unpad yet)
decrypted_message = cipher.decrypt(ciphertext_bytes)

# Output the decrypted message (it may still be padded)
decrypted_hex = binascii.hexlify(decrypted_message).decode('utf-8')
print("Decrypted (raw):", bytes.fromhex(decrypted_hex))
