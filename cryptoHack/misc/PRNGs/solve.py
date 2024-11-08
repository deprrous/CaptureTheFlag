import sympy

a  = sympy.nextprime(2<<512)
b = sympy.nextprime(2 << 512)


# print(a==b)

c = sympy.nextprime(a * 10) 
# print(c) 
print((23 ** (c-1))% c ==1)
# i = 10
# while True:
        
#     d = sympy.nextprime(c // i)
    
#     i = i * 10
#     print(i)
#     if d ==a:
#         print("True")
#         break
