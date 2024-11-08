from pwn import *
import json
import re
import string
import base64
import codecs


io = remote("socket.cryptohack.org", 13377)
dec = ""
step = 0
while step < 102:
    step += 1
    res = io.recv().decode()
    print(res)
    if not ("utf-8" in res):
        x = re.split('"*"', res)
        for i in x:
            if i[0] in string.punctuation or i in ",}:":
                x.remove(i)
        if x[1] == "base64":
            dec = base64.b64decode(x[3])
        elif x[1] == "rot13":
            dec = codecs.decode(x[3], "rot_13").encode()
        elif x[1] == "hex":
            dec = bytes.fromhex(x[3])
        elif x[1] == "bigint":
            m = x[3][2:]
            dec = bytes.fromhex(m)
    else:
        encoded_numbers = re.findall(r"\d+", res)
        encoded_numbers = list(map(int, encoded_numbers))
        decoded_string = "".join(chr(num) for num in encoded_numbers)
        dec = decoded_string.encode()[1:]

    # print(dec)
    last = b'{"decoded": "' + dec + b'"}'
    print(last)
    io.send(last)
