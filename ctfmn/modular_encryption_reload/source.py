from Crypto.Util.number import getPrime
from secret import flag

p = getPrime(256)
b = getPrime(256)

print([a * b % p for a in flag])
