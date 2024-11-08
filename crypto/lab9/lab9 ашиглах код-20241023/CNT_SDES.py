from sdes import *

text="TTT One Nine Two"
key10='1010000010'
marray=bArray(text)

C=[]
n=0
for p in marray:
    nt=decimalToBinary(n,8)
    O=SDES(key10,nt,'en')
    lxr=logical_xor(p,O)
    C.append(lxr)
    n+=1

print('Counter',C)
