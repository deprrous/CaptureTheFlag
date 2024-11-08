from Crypto.Util.number import *

c = [3185,2038, 2460, 2550]
e =17
p,q =53,61
n = p*q
phi = (p-1)*(q-1)
d = pow(e,-1, phi)
for i in c:
    print((pow(i,d,n)))


print(c)