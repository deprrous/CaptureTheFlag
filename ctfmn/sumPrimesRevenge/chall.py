from Crypto.Util.number import getPrime,bytes_to_long

primes = [getPrime(512) for _ in range(8)]
key = [[getPrime(64) for _ in range(8)] for i in range(8)]
mod = getPrime(513)

enc = [0] * 8

for i in range(8):
    for j in range(8):
        enc[i] += key[i][j] * primes[j]
    enc[i] %= mod

n = 1
for i in primes:
    n *= i
e = 65537

flag = open('flag.txt','rb').read()
m = bytes_to_long(flag)

c = pow(m,e,n)

with open('out.txt','w') as f:
    f.write('key = '+ str(key) +'\n')
    f.write('mod = '+ str(mod) +'\n')
    f.write('enc = '+ str(enc) +'\n')
    f.write('c = '+str(c)+'\n')
