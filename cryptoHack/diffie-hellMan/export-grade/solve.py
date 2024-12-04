from sympy.ntheory import discrete_log
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from galois import *
import hashlib

def solve_discrete_log(p, g, A, B):
    # F = GF(p)
    # g, A = F(g), F(A)
    a = discrete_log(p,A,g)
    return pow(B, int(a), p)




def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')


# host = "socket.cryptohack.org"
# port = 13379
# from pwn import *
# import json
# io = remote(host,port)
# (io.recv())
# data = io.recvuntil(b'\n').decode().strip()
# io.recvuntil("Send to Bob: ".encode())
# print(data)
# json_data = json.loads(data)

# io.send(json.dumps(json_data).encode())



# ("1",io.recv())
# data = io.recvuntil(b'\n')
# (io.recv())
# io.sendline(data)
# print(io.recv())
# alice_bob = io.recv().decode()
# parsed = alice_bob.split('\n')
# parsed.pop(-1) #suuliin hogiig ustgana

# io.close()
# first = json.loads(parsed[0])
# # print(1,first)
# second =  json.loads(parsed[1][22:])
# # print(2,second)
# third = json.loads(parsed[2][24:])
# # print(3,third)


# p = int(first['p'],16)
# g = int(first['g'],16)
# A = int(first['A'],16)
# B = int(second['B'],16)

# print("p: ",p)
# print(g)
# print("A: ",A)
# print()
# print(second)


p =  170211423340213335619890315701964596367945248276514520244678817439067130096324998127511342969908892058912749484588982313397564275823569054303745334070068855198518744024716272819605925778992568884399647476753727321262120112574453697534597065598599870833667305595574803533448657324362004298384951750848679478667
g = 2
A= 32732369190700436056713332886504922742879624789473770555019406485537945877077867835613280620471257699886503609257898404627982775175068063546644393165353099440030565387717584697946467555668579087223300867681334254375315827396860285452168089442233733635590645542396969154198756054321287063158878783327346796717
B = 0x4bd0d0340564f501db539be687d3c25b3e9646c0ee9293013c592313bc0db97c336d02f73ba4510c32e11062ce88164888f917e064ef69503029f664cc40cb81732797ddeebef5e39f6b9d4781ffff4fb144af7437bda4ece6b3d0ae24d4dfa54cfd9dd7b9b4300aece78dd9887cb1dbbc9b990e8607f4b9ca0a118414b5d751

import gmpy2
from gmpy2 import mpz
def pollards_rho_discrete_log(g, A, p):
    def f(x, a, b):
        if x % 3 == 0:
            return (x * x) % p, (a * 2) % (p - 1), (b * 2) % (p - 1)
        elif x % 3 == 1:
            return (x * g) % p, (a + 1) % (p - 1), b
        else:
            return (x * A) % p, a, (b + 1) % (p - 1)

    x, a, b = 1, 0, 0
    X, A_, B = x, a, b
    for i in range(1, p):
        x, a, b = f(x, a, b)
        X, A_, B = f(*f(X, A_, B))
        if x == X:
            r = (B - b) % (p - 1)
            if r == 0:
                raise ValueError("Failure in Pollard's Rho")
            return (a - A_) * gmpy2.invert(r, p - 1) % (p - 1)
    raise ValueError("Discrete log not found")

p = mpz(170211423340213335619890315701964596367945248276514520244678817439067130096324998127511342969908892058912749484588982313397564275823569054303745334070068855198518744024716272819605925778992568884399647476753727321262120112574453697534597065598599870833667305595574803533448657324362004298384951750848679478667)
A = mpz(32732369190700436056713332886504922742879624789473770555019406485537945877077867835613280620471257699886503609257898404627982775175068063546644393165353099440030565387717584697946467555668579087223300867681334254375315827396860285452168089442233733635590645542396969154198756054321287063158878783327346796717)
g = mpz(2)

x = pollards_rho_discrete_log(g, A, p)
print(x)





# print(s)











iv =  "9355d5787878d2a7650ff5137fccf846"

encrypted_flag = "32fd216c3cc95ccc19dff6d7b06734aeb5220ef21e0659effd02ca45826f3fb3"
