from pwn import *
io = remote("archive.cryptohack.org" ,1024)
io.interactive()