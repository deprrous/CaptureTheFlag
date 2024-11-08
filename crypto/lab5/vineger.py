def generate_vigenere_key(plain_text, key):
    key = list(key)
    if len(plain_text) == len(key):
        return key
    else:
        for i in range(len(plain_text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)



def vigenere_encrypt(plain_text, key):
    cipher_text = []
    for i in range(len(plain_text)):
        x = (ord(plain_text[i]) + ord(key[i])) % 26
        x += 65
        cipher_text.append(chr(x))
    return "".join(cipher_text)

def vigenere_decrypt(cipher_text, key):
    plain_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += 65
        plain_text.append(chr(x))
    return "".join(plain_text)

plain_text = "HELLO"
key = "KEY"

key = generate_vigenere_key(plain_text, key)
cipher_text = vigenere_encrypt(plain_text, key)
print(f"Cipher Text: {cipher_text}")

decrypted_text = vigenere_decrypt(cipher_text, key)
print(f"Decrypted Text: {decrypted_text}")

