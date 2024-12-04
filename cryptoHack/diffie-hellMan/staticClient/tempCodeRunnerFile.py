from pwn import *
io = remote("socket.cryptohack.org",13373)
data = io.recv()
print(data)