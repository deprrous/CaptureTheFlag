import gmpy2
from gmpy2 import mpz
import sympy
from gmpy2 import is_prime
from sympy import divisors

def find_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors

def is_primitive_root(g, p):
    divisors = find_divisors(p - 1)
    for d in divisors:
        if gmpy2.powmod(g, d, p) == 1 and d != p - 1:
            return False
    return True

def generate_large_prime(digits):
    start = 10**(digits - 1)
    prime = sympy.nextprime(start)  
    return mpz(prime)

def find_primitive_roots_of_large_prime(prime_digits):
    prime = generate_large_prime(prime_digits)
    print(f"Found prime: {prime}")
    
    primitive_roots = []
    
    while len(primitive_roots) < 50:
        if is_primitive_root(g, prime):
            primitive_roots.append(g)
        g += 1
    
    return primitive_roots

if __name__ == "__main__":
    print("Finding 50 primitive roots for a 10-digit prime number...")
    primitive_roots_10_digit = find_primitive_roots_of_large_prime(10)
    print(f"First 50 primitive roots for 10-digit prime: {primitive_roots_10_digit}")

    print("\nFinding 50 primitive roots for a 100-digit prime number...")
    primitive_roots_100_digit = find_primitive_roots_of_large_prime(100)
    print(f"First 50 primitive roots for 100-digit prime: {primitive_roots_100_digit}")

    print("\nFinding 50 primitive roots for a 150-digit prime number...")
    primitive_roots_150_digit = find_primitive_roots_of_large_prime(150)
    print(f"First 50 primitive roots for 150-digit prime: {primitive_roots_150_digit}")
