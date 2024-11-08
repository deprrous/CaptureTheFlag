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
