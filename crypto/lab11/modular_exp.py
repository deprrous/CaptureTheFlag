import math
def modular_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def inverse(a, p):
    return pow(a, -1, p)

def egcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        g, x1, y1 = egcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return g, x, y

def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def gcd(a, b):
    if(b == 0):
        return abs(a)
    else:
        return gcd(b, a % b)
    

def discrete_log(a, b, p):
    m = int(math.ceil(math.sqrt(p - 1)))

    baby_steps = {}
    current = 1
    for i in range(m):
        baby_steps[current] = i
        current = (current * a) % p

    a_inv_m = pow(a, m * (p - 2), p)  
    current = b
    for j in range(m):
        if current in baby_steps:
            return j * m + baby_steps[current]
        current = (current * a_inv_m) % p

    return None

def is_primitive_root(a, q):
    powers = set()

    for i in range(1, q):
        power = pow(a, i, q)
        powers.add(power)

    return len(powers) == q - 1


import sympy

def find_smallest_primitive_root(p):
    # Prime тоо эсэхийг шалгах
    if not sympy.isprime(p):
        print(f"{p} нь prime тоо биш байна.")
        return None

    # p-1-ийг factorize хийх
    factors = sympy.factorint(p-1)
    prime_factors = list(factors.keys())
    # print(f"{p}-ийн p-1-ийн prime факторууд: {prime_factors}")

    # 2-с p хүртэлх тоонуудыг шалгах
    for g in range(2, p):
        flag = True
        for q in prime_factors:
            if pow(g, (p-1)//q, p) == 1:
                flag = False
                break
        if flag:
            return g  # Хамгийн жижиг primitive root олсон
    return None  # Primitive root олдсонгүй

def bbs(seed, M, n=10000):
    numbers = []  
    x = (seed**2) % M  
    for _ in range(n):
        x = (x**2) % M  
        numbers.append(x) 
    return numbers