
from gmpy2 import iroot

def miller_rabin(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    k, q = 0, n - 1
    while q % 2 == 0:
        k += 1
        q //= 2
        a = random.randrange(2, n - 1)
        x = pow(a, q, n)
        if x == 1 or x == n - 1:
            return True
    for _ in range(k - 1):
        x = pow(x, 2, n)
        if x == n - 1:
            return True
        return False


import math
import random
def primefactors(n):
    pf=[]
    #тэгш тоо байвал
    r=0
    while n % 2 == 0:
        r+=1
        n //=2
    if r!=0:
        pf.append([2,r])
    #n сондгой тоо болсон
    for i in range(3,int(math.sqrt(n))+1,2):
        r=0
        while (n % i == 0):
            r+=1
            n //=i
        if r!=0:
            pf.append([i,r])
    if n > 2:
        pf.append([n,1])
    return pf

def EulerTot(p) -> int:
    res = 0
    for i in range(2,10):
        if iroot(p,i)[1] and miller_rabin(iroot(p,i)[0]):
            a = iroot(p,i)[0]
            res = pow(a,i-1) * (a-1)
    if miller_rabin(p) == True:
        res = p - 1

    return res
        
p = int(input("enter num: "))
phi = EulerTot(p)
for num in range(1, p):
    temp = 1
    for power in range(1, phi):
        if pow(num, power, p) == 1:
            temp = 0
    if temp == 1 and pow(num, phi, p) == 1:
        print(num)
