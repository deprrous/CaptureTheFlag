from modular_exp import *
def keyGeneration(p):
    g = find_smallest_primitive_root(p)
    a = bbs(g * p,p-2,1)[0]
    A = modular_exp(g, a, p)
    b = bbs(g * p,p-2,1)[0]
    B = modular_exp(g, b, p)
    return (g,A,a,p) ,(g,B,b,p)
      

p = 157

alice,bob = keyGeneration(p)

a_s = pow(alice[1],bob[2],alice[3])
b_s = pow(bob[1],alice[2],bob[3])

print(a_s == b_s)
