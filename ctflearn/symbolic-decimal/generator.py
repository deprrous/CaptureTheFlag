# a = "!)@,!)*,(&,!)#,#@,!)@,$*,!!$,!)(,(&,!!^,^%,^%,#@,!!),!!&,!!&,$(,%@,%@,#@,((,((,!!%,^&,*$,&),!@#,^%,!!$,(&,$(,(%,%@,!)(,(&,!!$,!)$,(&,!!),(%,(*,$*,!)),!)*,$*,!)#,$*,(%,$*,!!$,!!&,!!&,$(,$(,(&,(&,(&,(%,!!%,!)$,!!&,!!&,!!&,##,##,##,!@%,!!@,^%,!)),!)),$(,!!),!)#"
f = open("d.txt",'r')
a = f.read() 
f.close()
per = [')','!','@','#','$','%','^','&','*','(']

sym = []
for char in a:
    ascii_val = str(ord(char))  # Convert character to ASCII value
    symbol_rep = ""    
    for digit in ascii_val:
        symbol_rep += per[int(digit)]  # Convert each digit to a corresponding symbol
    sym.append(symbol_rep)

# ccsCTF{4raii_amarhan_b0dl0g0_0ruu11aaaaaa_shuuuuuu!!!}

# # print("".join(chr(i) for i in sym))
# a = ['^%', '!!$', '(&', '$(', '(%', '%@', '!)(', '(&', '!!$', '!)$', '(&', '!!)', '(%', '(*', '$*', '!))', '!)*', '$*', '!)#', '$*', '(%', '$*', '!!$', '!!&', '!!&', '$(', '$(', '(&', '(&', '(&', '(%', '!!%', '!)$', '!!&', '!!&', '!!&', '##', '##', '##']
a = ",".join(sym)

f = open("flag.txt",'w')
a = f.write(a) 
f.close()