xored = b'\t\x1b\x11\x00\x16\x0b\x1d\x19\x17\x0b\x05\x1d(\x05\x005\x1b\x1f\t,\r\x00\x18\x1c\x0e'
pat = b'ctflearn{'
key = []
for i in range(len(xored)):
    key.append(chr(xored[i] ^ pat[i % len(pat)]))

print("".join(key))

k = b'jowls'
flag = []
for i in range(len(xored)):
    flag.append(chr(xored[i] ^ k[i % len(k)]))
print("".join(flag))