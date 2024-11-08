# Permutation and S-Box Tables
p10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
p8 = [6, 3, 7, 4, 8, 5, 10, 9]
ip8 = [2, 6, 3, 1, 4, 8, 5, 7]
ep8 = [4, 1, 2, 3, 2, 3, 4, 1]
pi4 = [2, 4, 3, 1]
ip_1 = [4, 1, 3, 5, 7, 2, 8, 6]

s0 = [
    ['01', '00', '11', '10'],
    ['11', '10', '01', '00'],
    ['00', '10', '01', '11'],
    ['11', '01', '11', '10']
]

s1 = [
    ['00', '01', '10', '11'],
    ['10', '00', '01', '11'],
    ['11', '00', '01', '00'],
    ['10', '01', '00', '11']
]

# Initial Permutation (IP) function
def initial_permutation(key, st):
    return ''.join([st[i-1] for i in key])

# XOR between two binary strings
def logical_xor(str1, str2):
    return ''.join(['1' if str1[i] != str2[i] else '0' for i in range(len(str1))])

# Row-Column Index (for S-Box lookup)
def RC(str1):
    return int(str1, 2)  # Convert binary string to integer

# Key Scheduling: Split key10 into left and right halves, rotate, and generate subkeys
def key_schedule(key10):
    key10 = initial_permutation(p10, key10)  # Apply P10 permutation
    # Generate two subkeys
    k1, key10 = derive_key(key10, 1)
    k2, key10 = derive_key(key10, 2)
    return k1, k2

# Key Derivation: Left rotation and apply P8 to derive subkeys
def derive_key(key10, shift_amount):
    left_half = key10[:5]
    right_half = key10[5:]
    # Left circular shifts
    left_half = left_half[shift_amount:] + left_half[:shift_amount]
    right_half = right_half[shift_amount:] + right_half[:shift_amount]
    # Concatenate and apply P8 permutation to get the subkey
    key10 = left_half + right_half
    k = initial_permutation(p8, key10)
    return k, key10

# One round of Feistel function
def feistel_round(P, subkey):
    L = P[:4]
    R = P[4:]
    # Expansion Permutation (EP)
    ep = initial_permutation(ep8, R)
    # XOR with subkey
    ep = logical_xor(ep, subkey)

    # S-Box lookups
    s0_row = RC(ep[0] + ep[3])
    s0_col = RC(ep[1] + ep[2])
    s1_row = RC(ep[4] + ep[7])
    s1_col = RC(ep[5] + ep[6])

    # S-Box substitutions
    P4 = s0[s0_row][s0_col] + s1[s1_row][s1_col]
    P4 = initial_permutation(pi4, P4)

    # XOR with left half
    P4 = logical_xor(P4, L)
    return R + P4  # Swap halves

# Simplified DES encryption/decryption
def SDES(key10, P, mode):
    # Generate the subkeys
    k1, k2 = key_schedule(key10)
    if mode == 'de':  # Reverse keys for decryption
        k1, k2 = k2, k1
    
    # Initial permutation
    P = initial_permutation(ip8, P)
    
    # First round of Feistel
    P = feistel_round(P, k1)
    
    # Second round of Feistel (including swap)
    P = feistel_round(P, k2)
    
    # Final permutation (IP inverse)
    P = P[4:] + P[:4]  # Swap halves
    P = initial_permutation(ip_1, P)
    
    return P

# Convert text to binary (8-bit blocks)
def text_to_binary(text):
    return ''.join([format(ord(c), '08b') for c in text])

# Convert binary string to text
def binary_to_text(binary_str):
    chars = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
    return ''.join([chr(int(c, 2)) for c in chars])

# Pad the binary string to ensure it's a multiple of 8
def pad_binary(binary_str):
    padding_length = (8 - len(binary_str) % 8) % 8
    return binary_str + '0' * padding_length

# Main function to encrypt a file and save the result
def file(input_file, output_file, key10, mode):
    with open(input_file, "rb") as f:  # Read as binary
        data = f.read().strip()  # Read the file content and strip whitespace

    # Convert bytes to binary
    binary_data = ''.join(format(byte, '08b') for byte in data)
    binary_data = pad_binary(binary_data)  # Ensure binary data is padded

    encrypted_data = ""
    
    for i in range(0, len(binary_data), 8):
        block = binary_data[i:i+8]
        encrypted_block = SDES(key10, block, mode)
        encrypted_data += encrypted_block

    # Write the encrypted content as binary to a new file
    with open(output_file, "wb") as f:  # Write as binary
        f.write(bytearray(int(encrypted_data[i:i+8], 2) for i in range(0, len(encrypted_data), 8)))

# Example usage
key10 = '1010000010'
file("data.txt", "encrypted.txt", key10, 'en')
file("encrypted.txt", "decrypted.txt", key10, 'de')
