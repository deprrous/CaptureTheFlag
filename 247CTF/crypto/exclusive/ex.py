from itertools import cycle

def xor(a, b):
  x = [i ^ j for i, j in zip(a, b)]
  return bytes(x)

with open('exclusive_key','rb') as fp:
  key = '<!DOCTYPE html>\n<html class="client-nojs'.encode("utf-8")
  fp = fp.read()
  result = xor(fp,cycle(key))

with open('result.bin','wb') as fp:
  fp.write(result)