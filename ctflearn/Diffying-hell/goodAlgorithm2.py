def pollards_rho_dlp(g, h, p, max_steps=1000000):
    def f(x, a, b):
        if x % 3 == 0:
            return (g * x) % p, (a + 1) % (p-1), b
        elif x % 3 == 1:
            return (x * x) % p, (2 * a) % (p-1), (2 * b) % (p-1)
        else:
            return (h * x) % p, a, (b + 1) % (p-1)

    x, a, b = 1, 0, 0
    X, A, B = x, a, b

    for _ in range(max_steps):
        x, a, b = f(x, a, b)
        X, A, B = f(*f(X, A, B))  # Move two steps for tortoise and hare

        if x == X:
            if b == B:
                return None  # Failure
            # Solve (a - A) ≡ (B - b) * x mod (p-1)
            try:
                d = (B - b) % (p-1)
                inv_d = pow(d, -1, p-1)
                return ((a - A) * inv_d) % (p-1)
            except ValueError:
                return None  # Inverse doesn't exist
    return None  # Exceeded max steps

p = 0x304e332855
g = 0x2
A = 0x2809a0c342
B = 0x9009b1e22

# Find Alice's private key a
a = pollards_rho_dlp(g, A, p)
print(f"Alice's Private Key (a): {a}")

# Find Bob's private key b
b = pollards_rho_dlp(g, B, p)
print(f"Bob's Private Key (b): {b}")
