p = 28151
phi = p - 1
for num in range(1, p):
    temp = 1
    for power in range(1, phi):
        if pow(num, power, p) == 1:
            temp = 0
    if temp == 1 and pow(num, phi, p) == 1:
        print(num)
