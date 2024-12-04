from modular_exp import *
import time
def keyGeneration(p):
    g = find_smallest_primitive_root(p)
    a = bbs(g * p,p-2,1)[0]
    k = bbs(g * p,p-2,1)[0]
    A = modular_exp(g, a, p)
    return (g,a,p) , (g,A,p,k)
      

def elgamal_encrypt(pu, m):
    C1 = modular_exp(pu[0], pu[3], pu[2])  
    C2 = (m * modular_exp(pu[1], pu[3], pu[2])) % pu[2] 
    return (C1, C2)

def elgamal_decrypt(pr, C1, C2):
    s = modular_exp(C1, pr[1], pr[2]) 
    s_inv = inverse(s, pr[2])  
    m = (C2 * s_inv) % pr[2] 
    return m

p = 191
pr,pu = keyGeneration(p)
f = open(r"/home/deprrous/Downloads/10mb.txt",'r')
d = f.read()
data = []
f.close()
for i in d:
    data.append(ord(i))
cc = []

start = time.time()
for m in data:
    cc.append(elgamal_encrypt(pu, (m)))
end = time.time()
res = end - start
print(res)

f = open(r"enc.txt",'w')
dec = []
start = time.time()
for c in cc:
    dec.append((elgamal_decrypt(pr, c[0],c[1])))
end = time.time()
res = end - start
print(res)

# for i in dec:
#     i = chr(i)
# print(dec)