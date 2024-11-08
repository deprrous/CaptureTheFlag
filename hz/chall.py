from sage.all import *
import string, base64, math

flag = ""
CHILDREN = string.printable[:62] + '\\='

Z = list(GF(64))

def maptokindergarten(c):
    assert c in CHILDREN
    return Z[CHILDREN.index(c)]

def keygen(l):
    key = [Z[randint(1, 63)] for _ in range(l)] 
    key = math.prod(key)
    return key

def encrypt(msg, key):
    m64 = base64.b64encode(msg.encode())
    enc, pkey = '', key**5 + key**3 + key**2 + 1
    for m in m64:
        enc += CHILDREN[Z.index(pkey * maptokindergarten(chr(m)))]
    return enc

key = keygen(14) 
# Hmm, 64**14 > 2**64 looks unhackable to me.

enc = encrypt(flag, key)
print(f'Output: {enc}')

#Output: HudnBsx03TGdBIK4NS50=vlo=8NoMouoMSCdBLm9yoK41vl03M0Q