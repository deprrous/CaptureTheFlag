from modular_exp import *

e = 65
n = 2881

pq = prime_factors(n)
phi = 1
for i in pq:
    phi *= (i-1)
d = inverse(e,phi)

print(d)
