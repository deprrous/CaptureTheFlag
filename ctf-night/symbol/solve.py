f = open("flag.txt",'r')
flag = f.read()

per = [')','!','@','#','$','%','^','&','*','(']

flag = flag.split(",")
ascii = []
for i in flag:
    b = ""
    for j in i:
        if j == '\n':
            continue
        else:
            b += str(per.index(j))
    ascii.append(int(b))
    b = ""

f = "".join(chr(i) for i in ascii)
f = f.split()
for i in f:
    if 'ccsCTF' in i:
        print("flag is here",i)
        break
