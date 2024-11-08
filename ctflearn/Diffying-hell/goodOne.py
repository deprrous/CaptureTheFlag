import sympy

# Example usage
p = 0x304e332855
g = 0x2
A = 0x2809a0c342
B = 0x9009b1e22

# Using SymPy's discrete_log function
a = sympy.discrete_log(p, A, g)
b = sympy.discrete_log(p, B, g)

print(f"The Bob x is: {a}")    # Expected Output: 6
print(f"The Alice x is: {b}")  # Expected Output: 15

# Convert to bytes
def int_to_bytes(x):
    hex_str = hex(x)[2:]
    if len(hex_str) % 2:
        hex_str = '0' + hex_str
    return bytes.fromhex(hex_str)

fa = int_to_bytes(a)
fb = int_to_bytes(b)

print("[+] a secret is: ", fa)
print("[+] b secret is: ", fb)

s_alice = pow(B, a, p)
s_bob = pow(A, b, p)

assert s_alice == s_bob, "Нууц Түлхүүр тохирохгүй байна!"

print(f"Нууц Түлхүүр: {s_alice}")
