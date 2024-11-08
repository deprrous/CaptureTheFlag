# Define the parameters in hexadecimal
p_hex = "0x8c5378994ef1b"
g_hex = "0x02"
A_hex = "0x269beb3b0e968"
B_hex = "0x4757336da6f70"

# Convert hexadecimal to decimal
p = int(p_hex, 16)
g = int(g_hex, 16)
A = int(A_hex, 16)
B = int(B_hex, 16)

# Alice and Bob's randomly chosen private keys (for demonstration)
a_hex = "0xA1B2C3D4E5F6"  # Alice's private key
b_hex = "0x1F2E3D4C5B6A"  # Bob's private key

a = int(a_hex, 16)
b = int(b_hex, 16)

# Compute the shared secret
s_alice = pow(B, a, p)
s_bob = pow(A, b, p)

# Verify that both shared secrets are equal
assert s_alice == s_bob, "Shared secrets do not match!"

print(f"Shared Secret (Alice's computation): {s_alice}")
print(f"Shared Secret (Bob's computation): {s_bob}")
