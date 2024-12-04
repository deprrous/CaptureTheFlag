from modular_exp import *


p = 3
q = 7
e = 5
M = 10
n = p * q
phi = (p-1)*(q-1)
d = inverse(e,phi)
c = modular_exp(M,e,n)
dec = modular_exp(c,d,n)
print("orig m: ",M)
print("n: ",n)
print("c: ")
print("d: ",d)
print("decrypted: ",dec)

print()



p = 5
q = 13
e = 5
M = 8
n = p * q
phi = (p-1)*(q-1)
d = inverse(e,phi)
c = modular_exp(M,e,n)
dec = modular_exp(c,d,n)
print("orig m: ",M)
print("n: ",n)
print("c: ")
print("d: ",d)
print("decrypted: ",dec)

print()



p = 7
q = 17
e = 11
M = 11
n = p * q
phi = (p-1)*(q-1)
d = inverse(e,phi)
c = modular_exp(M,e,n)
dec = modular_exp(c,d,n)
print("orig m: ",M)
print("n: ",n)
print("c: ")
print("d: ",d)
print("decrypted: ",dec)


print()



p = 7
q = 13
e = 11
M = 2
n = p * q
phi = (p-1)*(q-1)
d = inverse(e,phi)
c = modular_exp(M,e,n)
dec = modular_exp(c,d,n)
print("orig m: ",M)
print("n: ",n)
print("c: ")
print("d: ",d)
print("decrypted: ",dec)


print()

p = 17
q = 23
e = 9
M = 7
n = p * q
phi = (p-1)*(q-1)
d = inverse(e,phi)
c = modular_exp(M,e,n)
dec = modular_exp(c,d,n)
print("orig m: ",M)
print("n: ",n)
print("c: ")
print("d: ",d)
print("decrypted: ",dec)
