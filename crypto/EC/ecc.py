import random
import time

# 1. ECC functions for point operations
def GCD(x, y):
    if y != 0:
        x = GCD(y, x % y)
    return x

def PQ(P, Q, p):
    xQ, yQ = Q[0], Q[1]
    xP, yP = P[0], P[1]

    dtu = (yQ - yP) % p
    dtd = (xQ - xP) % p

    gcd = GCD(dtd, p)
    if gcd != 1:
        raise ValueError(f"dtd={dtd} ба p={p} харилцан анхны тоонууд биш.")

    dtd_inv = pow(dtd, -1, p)
    dt = (dtd_inv * dtu) % p

    return dt

def PP(P, a, p):
    xP, yP = P[0], P[1]
    dtu = (3 * (xP**2) + a) % p
    dtd = (2 * yP) % p

    gcd = GCD(dtd, p)
    if gcd != 1:
        raise ValueError(f"dtd={dtd} ба p={p} харилцан анхны тоонууд биш.")

    dtd_inv = pow(dtd, -1, p)
    dt = (dtd_inv * dtu) % p

    return dt

def ECC_PQ(P, Q, a, b, p):
    if P == Q:
        L = PP(P, a, p)
    else:
        L = PQ(P, Q, p)

    xP, yP = P
    xQ, yQ = Q

    xR = (L**2 - xP - xQ) % p
    yR = (L * (xP - xR) - yP) % p
    return (xR, yR)

def mult(n, P, a, b, p):
    # Ensure that the point P is a tuple (x, y) and not just an integer
    if isinstance(P, tuple) and len(P) == 2:
        Q = P
        for _ in range(1, n):
            Q = ECC_PQ(Q, P, a, b, p)
        return Q
    else:
        raise ValueError(f"Expected a point as input, but got {P}.")

# 2. Random Key Generation for ElGamal
def random_key_generation(p):
    a = random.randint(1, p - 1)  # Private key, random in range [1, p-1]
    k = random.randint(1, p - 1)  # Random 'k' for encryption
    G = (2, 4)  # Base point for elliptic curve (must be a point)
    A = modular_exp(G[0], a, p)  # Public key A = g^a mod p
    return (G, a, p), (G, A, p, k)

# 3. Modular Exponentiation for ElGamal and ECC
def modular_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp = exp // 2
    return result

# 4. Finding the inverse modulo p
def inverse(x, p):
    return pow(x, -1, p)

# 5. ElGamal Encryption/Decryption for ECC
def elgamal_encrypt(pu, m):
    # Ensure m is a valid ECC point before proceeding
    if isinstance(m, tuple) and len(m) == 2:
        k = pu[3]  # Random secret 'k' from public key
        C1 = mult(k, pu[0], a, b, p)  # C1 = k * G (random point)
        C2 = ECC_PQ(m, mult(k, pu[1], a, b, p), a, b, p)  # C2 = m + k * A
        return (C1, C2)
    else:
        raise ValueError(f"Expected a point for encryption, but got {m}.")

def elgamal_decrypt(pr, C1, C2):
    s = mult(pr[1], C1, a, b, p)  # s = C1^a
    s_inv = inverse(s, pr[2])  # s_inv = s^-1
    m = ECC_PQ(C2, s_inv, a, b, p)  # m = C2 - s_inv * C1
    return m

# 6. Define Parameters for ECC and ElGamal
p = 257  # Example prime for simplicity
a = 2    # Coefficient 'a' for elliptic curve equation
b = 3    # Coefficient 'b' for elliptic curve equation
G = (2, 4)  # Base point for elliptic curve

# Key Generation for ECC and ElGamal
pr, pu = random_key_generation(p)

# 7. ECC Mapping - Create a mapping for each character to ECC point
def useg2point(G, a, b, p):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 -'',.&!?"
    ecc_mapping = {}
    for index, char in enumerate(alphabet):
        ecc_mapping[char] = mult(index + 1, G, a, b, p)
    return ecc_mapping

# Generate ECC mapping for each character
ecc_mapping = useg2point(G, a, b, p)

# 8. Encrypt the file using ECC ElGamal
f = open("/home/deprrous/kali/crypto/EC/10MB.txt", 'r')
data = f.read()
f.close()

# Encrypt message using ECC ElGamal
cc = []
start = time.time()
for char in data:
    if char in ecc_mapping:
        m = ecc_mapping[char]  # Map each character to ECC point
        cc.append(elgamal_encrypt(pu, m))  # Encrypt using ECC ElGamal
    else:
        continue  # Handle undefined characters (e.g., spaces or special chars)
end = time.time()
print(f"Encryption time: {end - start:.2f} seconds")

# 9. Decrypt the file using ECC ElGamal
dec = []
start = time.time()
for c in cc:
    if c:
        m = elgamal_decrypt(pr, c[0], c[1])  # Decrypt using ECC ElGamal
        dec.append(m)  # Append decrypted message
    else:
        dec.append(" ")  # Handle None (undefined characters)
end = time.time()
print(f"Decryption time: {end - start:.2f} seconds")

# 10. Save encrypted and decrypted data
with open("encrypted.txt", 'w') as f:
    f.write(str(cc))

with open("decrypted.txt", 'w') as f:
    f.write("".join([chr(m[0]) if isinstance(m, tuple) else str(m) for m in dec]))  # Convert to characters or handle None

print("Encryption and Decryption process completed successfully!")
