
def find_discrete_log(g, h, p):
    """
    Finds the smallest integer x such that g^x ≡ h mod p
    Returns x if found, else None
    """
    for x in range(1, p):
        if pow(g, x, p) == h:
            return x
    return None

# Given parameters
p = 0x304e332855
g = 0x2
A = 0x2809a0c342
B = 0x9009b1e22

# Find Alice's private key a
a = find_discrete_log(g, A, p)
print(f"Alice's Private Key (a): {a}")

# Find Bob's private key b
b = find_discrete_log(g, B, p)
print(f"Bob's Private Key (b): {b}")
