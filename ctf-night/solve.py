import sympy

p = 0x304e332855
g = 0x2
A = 0x2809a0c342
B = 0x9009b1e22

a = sympy.discrete_log(p, A, g)
b = sympy.discrete_log(p, B, g)

def int_to_bytes(x):
    hex_str = hex(x)[2:]
    if len(hex_str) % 2:
        hex_str = '0' + hex_str
    return bytes.fromhex(hex_str)

fa = int_to_bytes(a)
fb = int_to_bytes(b)

print("Alimaa: ", fa)
print("Boldoo: ", fb)

s_alice = pow(B, a, p)
s_bob = pow(A, b, p)
