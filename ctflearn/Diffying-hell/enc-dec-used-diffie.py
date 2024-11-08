from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

# Shared secret from Diffie-Hellman (both Alice and Bob have this)
shared_secret = 2  # Example shared secret

# Convert the shared secret to bytes
shared_secret_bytes = shared_secret.to_bytes((shared_secret.bit_length() + 7) // 8, 'big')

# Derive a symmetric key using HKDF
hkdf = HKDF(
    algorithm=hashes.SHA256(),
    length=32,  # 32 bytes = 256 bits for AES-256
    salt=None,  # Optional salt
    info=b'diffie-hellman-key-exchange',
)
symmetric_key = hkdf.derive(shared_secret_bytes)

print(f"Derived Symmetric Key: {symmetric_key.hex()}")
