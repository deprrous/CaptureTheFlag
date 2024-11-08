from sdes import *

text="TTT One Nine Two"
key10='1010000010'
marray=bArray(text)
print(marray)
C=[]
IV='00000000'
lxr=logical_xor(marray[0], IV)
C.append(SDES(key10,lxr,'en'))

for j in range(1,len(marray),1):
    lxr=logical_xor(C[j-1],marray[j])
    c=SDES(key10,lxr,'en')
    C.append(c)

print('CBC',C)
