import math

def baby_step_giant_step(g, h, p):
    m = math.isqrt(p) + 1

    # Baby steps: compute g^j for j from 0 to m-1 and store in a dictionary
    baby_steps = {}
    current = 1
    for j in range(m):
        baby_steps[current] = j
        current = (current * g) % p

    # Compute g^-m using Fermat's Little Theorem
    g_inv_m = pow(g, p - 1 - m, p)

    # Giant steps: look for h * (g^-m)^i in baby_steps
    current = h
    for i in range(m):
        if current in baby_steps:
            return i * m + baby_steps[current]
        current = (current * g_inv_m) % p

    return None  # Logarithm not found

# Example usage
# p = 0x8c5378994ef1b
# g = 0x02

# A = 0x269beb3b0e968
# B = 0x4757336da6f70
p = 14868003561817111
g = 6
A = 4075572427361901
B = 14868003561817032
a = baby_step_giant_step(g, A, p)
b = baby_step_giant_step(g, B, p)
print(f"The Bob x is: {a}")  # Output: 6
print(f"The Alice x is: {b}")  # Output: 6


fa=bytes.fromhex(hex(a)[2:])
fb=bytes.fromhex(hex(b)[2:])


print("[+] a secret is: ",fa)
print("[+] b secret is: ",fb)

s_alice = pow(B, a, p)
s_bob = pow(A, b, p)

assert s_alice == s_bob, "Нууц Түлхүүр тохирохгүй байна!"

print(f"Нууц Түлхүүр: {s_alice}")