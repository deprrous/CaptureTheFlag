from Crypto.Util.number import *
from pwn import *
hex_data = bytes.fromhex('141414141414141414141414141414141414141414141414141414141414')
hex_data1 = bytes.fromhex('7f393a8c9cb7b29b8a0b07aec927919b0465474f4d926bbacb56d158d83a')
# print(hex_data1)
a= []
# key=xor(hex_data,hex_data1)
for i in range(len(hex_data)):
	a.append(hex_data[i]^hex_data1[i])

flag = bytes.fromhex('085f57e8fcccddfbae2f4cdce940f1d0644163043ff30dc7ef37f031')
res = []
try: 
	for i in range(len(a)):
		res.append(chr(a[i] ^ flag[i]))
# print(xor(key,flag))
except:
	print("".join(res))
print("".join(res))

# flag bdddf593ccc1ef366a205102261d4d081dcc1cd87264033eb3466a84
# data cabb98f7acba80564e041a70067a2d437de838930005654397274b
