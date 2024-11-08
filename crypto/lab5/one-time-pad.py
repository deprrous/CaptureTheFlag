import os

def generate_otp_key(length):
    # Бүрэн санамсаргүй байт үүсгэх
    return os.urandom(length)

def otp_encrypt(plain_text, key):
    plain_bytes = plain_text.encode('utf-8')
    cipher_bytes = bytes([b ^ k for b, k in zip(plain_bytes, key)])
    return cipher_bytes

def otp_decrypt(cipher_bytes, key):
    plain_bytes = bytes([c ^ k for c, k in zip(cipher_bytes, key)])
    return plain_bytes.decode('utf-8')

# Жишээ ашиглалт
if __name__ == "__main__":
    plain_text = "HELLO WORLD"
    key = generate_otp_key(len(plain_text))
    print(f"Нийтлэл: {plain_text}")
    print(f"Түлхүүр (бинар): {key}")
    
    encrypted = otp_encrypt(plain_text, key)
    print(f"Шифрлэгдсэн (бинар): {encrypted}")
    
    decrypted = otp_decrypt(encrypted, key)
    print(f"Тайлагдсан: {decrypted}")

