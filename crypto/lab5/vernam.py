def vernam_encrypt(plain_text, key):
    enc = []
    for i in range(len(plain_text)):
        enc.append(chr(ord(plain_text[i]) ^ ord(key[i % len(key)])))
    return "".join(i for i in enc)

def vernam_decrypt(cipher_text, key):
    dec = []
    for i in range(len(cipher_text)):
        dec.append(chr(ord(cipher_text[i] ^ ord(key[i % len(key)]))))


f = open("data.txt","r")

plain_text = f.read()
f.close()

key = "yuipojlk"

c = vernam_encrypt(plain_text, key)

f = open("enc.txt","w")

f.write(c)
f.close()
