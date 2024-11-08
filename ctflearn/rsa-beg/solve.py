p = 416064700201658306196320137931
q =  590872612825179551336102196593
n = p * q
e = 3
c = 219878849218803628752496734037301843801487889344508611639028
from Crypto.Util.number import long_to_bytes,inverse
phi = (p-1) * (q-1)
d = inverse(e,phi)
m = long_to_bytes(pow(c,d,n))
print(m)
