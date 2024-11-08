from sdes import *

text="TTT One Nine Two"
key10='1010000010'
marray=bArray(text)

C=[]
nonce='00000000'

for p in marray:
    O=SDES(key10,nonce,'en')
    lxr=logical_xor(p,O)
    nonce=O
    C.append(lxr)

print('OFB',C)
