f = '4728d7c027e2e172467dcafe2db3e8794b1df29038dcf3795a26ffd57fedee69'

f = bytearray.fromhex(f)
from pwn import xor
from Crypto.Util.number import *

# Define the target string and its length
target_string = b'mazala{'
target_length = len(target_string)

# Iterate through possible keys
for i in range(256):
    key = bytes(i)
    result = xor(f, target_string + bytes(i))
    flag = xor(f, result[0:8])
        
    # Check if the target string is present at the beginning of the result
  
    print(flag)
