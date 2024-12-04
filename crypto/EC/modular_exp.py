def modular_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

def inverse(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception("error")
    return x % m

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