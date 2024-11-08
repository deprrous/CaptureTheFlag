from Crypto.PublicKey import RSA

with open('2048-rsa-example-cert.der', 'rb') as f:
    public_key_der = f.read()

public_key = RSA.import_key(public_key_der)
print(public_key.n)
