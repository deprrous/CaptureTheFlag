import math

def baby_step_giant_step(g, h, p):
    m = math.isqrt(p) + 1

    baby_steps = {}
    current = 1
    for j in range(m):
        baby_steps[current] = j
        current = (current * g) % p

    g_inv_m = pow(g, p - 1 - m, p)

    current = h
    for i in range(m):
        if current in baby_steps:
            return i * m + baby_steps[current]
        current = (current * g_inv_m) % p

    return None  
# p = 1375571023180691
# g = 0x2
# A = 367614718735785 
# B = 129589722679614

p = 333870410550569
g = 3
A = 146771267179515
a = baby_step_giant_step(g, A, p)
print(a)
# b = baby_step_giant_step(g, B, p)
# print(f"The Alimaa x is: {a}") 
# print(f"The Boldoo x is: {b}")  


# fa = bytes.fromhex(hex(a)[2:])
# fb = bytes.fromhex(hex(b)[2:])


# print("Alimaa's a secret is: ",fa)
# print("Boldoo's secret is: ",fb)
