import sympy
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from galois import *


def solve_discrete_log(p, g, A, B):
    F = GF(p)
    g, A = F(g), F(A)
    a = sympy.discrete_log(A,g)
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


host = "socket.cryptohack.org"
port = 13379
from pwn import *
import json
io = remote(host,port)
(io.recv())
data = io.recvuntil(b'\n').decode().strip()
io.recvuntil("Send to Bob: ".encode())
print(data)
json_data = json.loads(data)

io.send(json.dumps(json_data).encode())



("1",io.recv())
data = io.recvuntil(b'\n')
# print(data)
(io.recv())
io.sendline(data)
print(io.recv())
alice_bob = io.recv().decode()
parsed = alice_bob.split('\n')
parsed.pop(-1) #suuliin hogiig ustgana

io.close()
first = json.loads(parsed[0])
# print(1,first)
second =  json.loads(parsed[1][22:])
# print(2,second)
third = json.loads(parsed[2][24:])
# print(3,third)


p = int(first['p'],16)
g = int(first['g'],16)
A = int(first['A'],16)
B = int(second['B'],16)

print(p)
print(g)
print(A)
print(B)
# secret = solve_discrete_log(p,g,A,B)
# secret = 
# print("secret:  ",secret)
# flag = decrypt_flag(secret,third['iv'],third['encrypted_flag'])
# print(flag)



F = GF(p)
g, A = F(g), F(A)
a = sympy.discrete_log(A,g)


iv = "288632c87154f32b8d5b40e995fbe582"
enc_flag = "4bf5988818383efef8fde913f0063dbab474656e41e3cdbc662287606dea24a9"

# p = 0xf2639ce2bdb2e67154813bcbda8e5a09ddaa1235c5e76300602e29ada9dd6dfddf36b3c6a676891ddb1462de67cc27a45f84d8720b8bfdcb653c82814397998e84aafca63a8b4ae05d3193e7566173441d505dc3caea006f938d421de7e80748297496436e559fe9c443201de066cd7570a8a40c80a306309dfb4da48277858b
# g = 2
# A = 0xb159546bc47fa2e1c7cfa68e439ef51f0398bd75b704e9b8ec3292f2670e08a73c33367c891d2774c271a2fc2e3038f98722ec92a411e5f4d3a15e8f54f48ccdb3df837e951c7e477d3de7ab943e9fdee0e24f53b8d4ba8e59422a465d9c3a5f0de07e66c956a5fab5f52c
# B = 0x5e33b3de2c09d2309668fc23ce3ab422638e860ec12326f91c686e660b0b298e803b7bdd3334b5fdd0f032027a10a7fb31273d0e1647d15c00a47849958a3bb4be6a5f16d6c0f5a35baf57c1ff77e6b44912749ba8d77f300fc8b6932b306f5ddd5d99c21ec222f15e36a5cb5bc8e01624e78fad568f5fa131d3dafa34f9247e
p = 170211423340213335619890315701964596367945248276514520244678817439067130096324998127511342969908892058912749484588982313397564275823569054303745334070068855198518744024716272819605925778992568884399647476753727321262120112574453697534597065598599870833667305595574803533448657324362004298384951750848679478667

g = 2
A = 210802616608892656108199843104126619441721778826738643179275056528611525095562705356800956717909951185767110120220438010940539248245614152044413293034650906576831830076870528051672353319655038755422544636360190050027060154161304850729004370530031659301842046
B = 167382729520826214414260851642776785394792906769006619628012898887558436560580022863752667534036953085762973446513998639291084009983032151297409419459595669999857268105657183960855710705604540306764749579577377625535804777902810140051785213836220080280346069160960060833673839954005320628708596306576626834502

# Create the finite field GF(p)
F = GF(p)

# Convert g and A to elements in the finite field
g = F(g)
A = F(A)

# Compute the discrete logarithm a such that A = g^a (mod p)
a = discrete_log(A, g)

# Output the result
print("The discrete logarithm a is:", a)
