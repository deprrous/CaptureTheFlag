import pwn

pwn.context.log_level = "debug"

p = pwn.remote("94.237.48.203", "39384")

p.sendlineafter("(y/n)", "y")
p.recvuntil("Ok then! Let's go!\n")

while True:
    line = p.recvline().decode().strip()
    line = line.replace("GORGE", "STOP")
    line = line.replace("PHREAK", "DROP")
    line = line.replace("FIRE", "ROLL")
    line = line.replace(", ", "-")
    p.sendlineafter("What do you do? ", line)

