from Crypto.PublicKey import RSA

with open("bruce_rsa.pub","r") as f:

    pub_key = RSA.import_key(f.read())




print(pub_key.n)
