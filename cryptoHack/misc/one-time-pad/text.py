from pwn import *

# Connect to the remote service
io = remote("socket.cryptohack.org", 13372)

io.recv()
io.sendline(b'{"option": "get_flag"}')
a = io.recv()

io.sendline(b'{"option":"encrypt_data","input_data":"141414141414141414141414141414141414141414141414141414141414"}')

b = io.recv()

print(a)
print(b)



# 861bd50932afb922579570e30542bcd09dc0573d204df87947f63a