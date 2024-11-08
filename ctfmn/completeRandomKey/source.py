import os
from secret import flag

def xor(x, y):
    result = []
    length = max(len(x), len(y))
    for i in range(length):
        result.append(x[i % len(x)] ^ y[i % len(y)])
    return bytes(result)

key = os.urandom(8)
with open('output.txt', 'w') as f:
    f.write(xor(flag, key).hex())
