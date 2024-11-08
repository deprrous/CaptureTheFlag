import owiener

# Known vulnerable RSA public key values
e = 4021
N = 7429

# Attempt to recover the private exponent d
d = owiener.attack(e, N)

if d is not None:
    print(f"Recovered private exponent d: {d}")
else:
    print("Failed to recover the private exponent d.")
