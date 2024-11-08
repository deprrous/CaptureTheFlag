from collections import Counter

m = (2**31) - 1  
a = 1103515245   
c = 12345        
seed_lcg = 42    

p = 383
q = 503
M = p * q      
seed_bbs = 123  

def lcg(seed, a, c, m, n=1000):
    numbers = []
    x = seed
    for _ in range(n):
        x = (a * x + c) % m
        numbers.append(x / m) 
    return numbers

# Blum Blum Shub ашиглан 1000 тоо үүсгэх функц
def bbs(seed, M, n=1000):
    numbers = []
    x = (seed**2) % M
    for _ in range(n):
        x = (x**2) % M
        numbers.append(x / M)  # [0, 1) интервалд нормчлох
    return numbers

def calculate_frequencies(numbers):
    freq_counts = Counter(int(num * 10) for num in numbers)
    frequencies = {f"{i/10}-{(i+1)/10}": freq_counts[i] for i in range(10)}
    return frequencies

# Тоо үүсгэх
lcg_numbers = lcg(seed_lcg, a, c, m)
bbs_numbers = bbs(seed_bbs, M)

# Давтамжийн тархалтыг тооцоолох
lcg_frequencies = calculate_frequencies(lcg_numbers)
bbs_frequencies = calculate_frequencies(bbs_numbers)

print("LCG Давтамжийн Тархалт:")
for interval, count in lcg_frequencies.items():
    print(f"{interval}: {count} тоо")

print("\nBlum Blum Shub Давтамжийн Тархалт:")
for interval, count in bbs_frequencies.items():
    print(f"{interval}: {count} тоо")
