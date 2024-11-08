def GCD(a,b):
    gcd=0
    if b!=0:
        print(f'd=gcd({a}, {b})')
    if (b==0):
        gcd=a;
    else:
        gcd=GCD(b, a % b);
    return gcd
a,b=18,12
a,b=1160718174, 316258250
print('GCD:',GCD(a,b))


