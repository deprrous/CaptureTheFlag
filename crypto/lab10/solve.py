m = (2**31) - 1  
a = 1103515245   
c = 12345
seed_lcg = 42    

p = 383          
q = 503           
M = p * q         
seed_bbs = 123   

def lcg(seed, a, c, m, n=10000):
    numbers = []   
    x = seed       
    for _ in range(n):
        x = (a * x + c) % m 
        numbers.append(x / m)  
    return numbers

def bbs(seed, M, n=10000):
    numbers = []  
    x = (seed**2) % M  
    for _ in range(n):
        x = (x**2) % M  
        numbers.append(x / M) 
    return numbers

lcg_numbers = lcg(seed_lcg, a, c, m)
bbs_numbers = bbs(seed_bbs, M)

def calculate_frequency(numbers):
    freq_dict = {}
    for number in numbers:
        key = round(number, 4)  
        if key in freq_dict:
            freq_dict[key] += 1
        else:
            freq_dict[key] = 1
    return freq_dict

lcg_frequency = calculate_frequency(lcg_numbers)
bbs_frequency = calculate_frequency(bbs_numbers)

print("LCG Frequency Count:")
for number, freq in lcg_frequency.items():
    print(f"{number:.4f}: {freq}")

print("\nBBS Frequency Count:")
for number, freq in bbs_frequency.items():
    print(f"{number:.4f}: {freq}")
