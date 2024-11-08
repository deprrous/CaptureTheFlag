from pwn import *
import json
host = "socket.cryptohack.org"
port = 13371
io = remote(host,port)
io.recv()
# intercepted from alica
data = io.recv().decode()
data = data.replace("Send to Bob:","")

json_data = json.loads(data)
p = int((json_data['p']),16)
g = int(json_data['g'],16)
A = int(json_data['A'],16)
b = 123456789
B = pow(g,b,p)

K = pow(A,b,p)
print(K)
send = "{"
send += f'"p":"{str(p)}","g":"{str(g)}","A":"{str(B)}"'
send += "}"
# print(send)
io.send(send.encode())
# print(p)
# print(g)
# print(A)
io.recvuntil(b':')

# intercepted from Bob
data = (io.recvuntil(b'\n').decode().strip())
json_data = json.loads(data)

B2 = int(json_data['B'],16)
K2 = pow(B,b,p)
print(K == K2)
data2 = {"B": hex(B)}
data2 = json.dumps(data2).encode()
io.send(data2)


print(io.recv())
print(io.recv())
print(io.recv())
print(io.recv())


enc_flag = "7864a0a22508113e2d527ff0c89907ec61c286dd5814c7c142bd308d8c1cff09"


iv = "da7a63826f660f650ec09a8595b6a673"