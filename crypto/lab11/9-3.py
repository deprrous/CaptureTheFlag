from modular_exp import *



c = 20
e = 13
n = 77

pq = prime_factors(77)
print("factors: ",pq)
phi = 1
for i in pq:
    phi *= (i-1)
print("phi: ", phi)

d = inverse(e,phi)

m = modular_exp(c,d,n)

print("d: ",d)
print("m: ",m)
