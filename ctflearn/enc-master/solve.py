f = open("data.txt","r")
b = f.read() 

import base64
c = base64.b64decode(b).decode()
print(c)
d = c.replace("Nice! Now keep going. ", "")
print(bytes.fromhex(d))