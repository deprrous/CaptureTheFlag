from modular_exp import *
st = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
st += "0123456789 ,;@?"

f = open(r"/home/deprrous/kali/crypto/lab11/data.txt", "r")
message = f.read()
abc = []
abcN = []
for m in message:
    abc.append(st.index(m))
for i in range(0, len(abc), 2):
    abcN.append(abc[i] * 100 + abc[i + 1])
p = 73
q = 151
def keyGen(p,q):
   phi = (p-1)*(q-1)
   e = -1
   for i in range(p*q,2,-2):
      if gcd(phi,i) == 1:
          e = i
          break
   d = inverse(e, phi)
   return (e,p * q) , (d,q * p)
def rsa(m, key):
    return modular_exp(m, key[0], key[1])
pu ,pr = keyGen(p,q)
ciphers = []


for i in abcN:
    ciphers.append(rsa(i, pu))


print("ciphers: ", ciphers)
dec = []


for c in ciphers:
    dec.append(rsa(c, pr))

    
decoded_message = []
for number in dec:
    index1 = number // 100  
    index2 = number % 100   
    decoded_message.append(st[index1%len(st)])
    decoded_message.append(st[index2%len(st)])
original_message = ''.join(decoded_message)
print(original_message)