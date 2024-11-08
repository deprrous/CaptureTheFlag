from Crypto.Util.number import getPrime
from secret import flag

p = getPrime(256)
q = getPrime(256)

print([a * q % p for a in flag])
