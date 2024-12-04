import sympy

def find_smallest_primitive_root(p):
    # Prime тоо эсэхийг шалгах
    if not sympy.isprime(p):
        print(f"{p} нь prime тоо биш байна.")
        return None

    # p-1-ийг factorize хийх
    factors = sympy.factorint(p-1)
    prime_factors = list(factors.keys())
    print(f"{p}-ийн p-1-ийн prime факторууд: {prime_factors}")

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
