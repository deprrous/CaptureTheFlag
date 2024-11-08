from itertools import cycle

# Function to perform XOR with the given key
def perform_xor(key, hexdump):
    return bytes([a ^ b for a, b in zip(hexdump, cycle(key))])

# Decrypt the file using XOR
def xor_file(hex_file, key):
    # Open the encrypted file as binary
    with open(hex_file, 'rb') as f:
        hexdump = f.read()

    # Perform XOR operation using the key
    decrypted_data = perform_xor(key, hexdump)

    # Save the decrypted data to a new file
    with open('decrypted_output.jpg', 'wb') as output_file:
        output_file.write(decrypted_data)

    print("Decryption completed successfully, saved as 'decrypted_output.jpg'.")

# XOR key generation from the provided hex strings
a = bytes.fromhex("b9 14 06 45 71 e0 b5 f7 37 07 cb 85")
b = bytes.fromhex("FF D8 FF E0 00 10 4A 46 49 46 00 01")

# XOR the two byte sequences to generate the key
key = bytes(x ^ y for x, y in zip(a, b))

# File to be decrypted
hex_file = "my.jpg.enc"

# Perform XOR decryption
xor_file(hex_file, key)
