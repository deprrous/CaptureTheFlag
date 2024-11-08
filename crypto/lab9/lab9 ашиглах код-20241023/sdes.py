


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

def initial_permutation(key, st):

    return ''.join([st[i-1] for i in key])

def logical_xor(str1, str2):

    if len(str1) != len(str2):
        raise ValueError("Binary strings must be of the same length for XOR.")
    return ''.join(['1' if str1[i] != str2[i] else '0' for i in range(len(str1))])

def RC(str1):
 
    return int(str1, 2)

def key_schedule(key10):
 
    key10 = initial_permutation(p10, key10)  # Apply P10 permutation
    k1, key10 = derive_key(key10, 1)         # Derive first key (K1)
    k2, key10 = derive_key(key10, 2)         # Derive second key (K2)
    return k1, k2

def derive_key(key10, shift_amount):
  
    left_half = key10[:5]
    right_half = key10[5:]
    left_half = left_half[shift_amount:] + left_half[:shift_amount]
    right_half = right_half[shift_amount:] + right_half[:shift_amount]
    key10 = left_half + right_half
    return initial_permutation(p8, key10), key10

def feistel_round(P, subkey):
  
    L = P[:4]
    R = P[4:]
    ep = initial_permutation(ep8, R)          # Expansion Permutation (EP)
    ep = logical_xor(ep, subkey)              # XOR with subkey
    
    # S-Box lookups
    s0_row = RC(ep[0] + ep[3])
    s0_col = RC(ep[1] + ep[2])
    s1_row = RC(ep[4] + ep[7])
    s1_col = RC(ep[5] + ep[6])
    
    # S-Box substitutions
    P4 = s0[s0_row][s0_col] + s1[s1_row][s1_col]
    P4 = initial_permutation(pi4, P4)         # Apply P4 permutation
    return logical_xor(P4, L) + R             # XOR with left half and swap

def SDES(key10, P, mode):
  
    k1, k2 = key_schedule(key10)
    if mode == 'de':  # Reverse keys for decryption
        k1, k2 = k2, k1

    P = initial_permutation(ip8, P)          # Initial Permutation (IP)
    P = feistel_round(P, k1)                 # First round
    P = feistel_round(P[4:] + P[:4], k2)     # Second round (with swap)
    return initial_permutation(ip_1, P[4:] + P[:4])  # Final permutation (IP inverse)

def bArray(text):
  
    return [format(ord(c), '08b') for c in text]

def binary_to_text(binary_str):
  
    chars = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
    return ''.join([chr(int(c, 2)) for c in chars])

def decimalToBinary(n, bits):
    
    return format(n, '0{}b'.format(bits))
