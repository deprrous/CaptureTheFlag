from pwn import *

io = remote("94.237.50.25", 51920)
print("Connected to server")

print(io.recv(timeout=5).decode()) 
io.send(b'dasd')
print(io.recv(timeout=5).decode())