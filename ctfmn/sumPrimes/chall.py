from Crypto.Util.number import *

flag = open('flag.txt','rb').read()

m = bytes_to_long(flag)

p = getPrime(1024)
q = getPrime(1024)

e = 0x10001
n = p*q
c = pow(m,e,n)
xD = p+q

with open('out.txt','w') as f:
    f.write('n = '+str(n)+'\n')
    f.write('e = '+str(e)+'\n')
    f.write('c = '+str(c)+'\n')
    f.write('xD = '+str(xD)+'\n')
