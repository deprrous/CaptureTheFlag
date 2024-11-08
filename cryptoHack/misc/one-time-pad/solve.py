from pwn import *

io = remote("socket.cryptohack.org",13372)

print(io.recv())
io.sendline(b'{"option": "get_flag"}')
a = io.recv()

io.sendline(b'{"option":"encrypt_data","input_data":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"}')


b = io.recv()
b =  bytes.fromhex(b.decode().split(":")[1].strip()[1:-2])


r = b"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


key = []

for i in range(len(b)):
	key.append(b[i] ^ r[i])

for i in range(len(a)):
	key.append(key[i] ^ a[i])
	print((key[i]),end="")



# a = bytes.fromhex(a.decode().split(":")[1].strip()[1:-2])
# f = []

# 	f.append(key[i] ^ a[i])

# print("".join(chr(i) for i in f))

	











