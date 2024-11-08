import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def euler_totient_list(n):
    coprime_list = []
    for i in range(1, n):
        if gcd(i, n) == 1:
            coprime_list.append(i)
    return coprime_list

def miller_rabin(n):
    if n == 2:
        return True
    if n % 2 ==0:
        return False
    k,q = 0, n-1
    while q % 2==0:
        k += 1
        q //= 2
    a = random.randrange(2,n-1)
    x = pow(a,q,n)
    if x==1 or x==n-1:
        return True
    for _ in range(k-1):
        x = pow(x,2,n)
        if x == n-1:
            return True
    return False



n = int(input("Give me your number: "))

if miller_rabin(n):
    print(f"Euler's Totient list for {n} is {n-1}")


totient_list = euler_totient_list(n)
print(f"Euler's Totient list for {n} (numbers coprime with {n}): {totient_list}")
