from pwn import xor
file1 = open('CTFLearn.pdf', 'rb')
file2 = open('CTFLearn.txt', 'rb') 
var1 = file1.read() 
var2 = file2.read() 
flag = xor(var1, var2) 
res = open('result.pdf', 'wb') 
res.write(flag)