from Crypto.PublicKey import RSA

with open('public_key.pem','r') as key_file:
    key = RSA.importKey(key_file.read())
    print(key)
