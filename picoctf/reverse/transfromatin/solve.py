

a = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸強㕤㐸㤸扽"
dec = []
# for i in range(0, len(flag), 2):
#     dec.append(chr((ord(flag[i]) << 8) + ord(flag[i + 1])) )
flag = ""

for i in range(len(a)):
    ch1 = chr(ord(a[i]) >> 8)
    ch2 = chr(a[i].encode('utf-16be')[-1])
    flag += ch1
    flag +=ch2
print(flag)