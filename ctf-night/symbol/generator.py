f = open("d.txt",'r')
a = f.read() 
f.close()
per = [')','!','@','#','$','%','^','&','*','(']

sym = []
for char in a:
    ascii_val = str(ord(char)) 
    symbol_rep = ""    
    for digit in ascii_val:
        symbol_rep += per[int(digit)]  
    sym.append(symbol_rep)

a = ",".join(sym)

f = open("flag.txt",'w')
a = f.write(a) 
f.close()