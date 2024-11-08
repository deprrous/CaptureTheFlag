c = "4A3E374A4973483F3D3E4A"
c = c.lower()
l = []
for i in range(len(c)):
	if i == 0:
		continue
	elif i % 2 == 1:
		temp = (c[i-1] + c[i])
		l.append(int(temp,16))
print(ord("A"))
print(0x51)

for i in l:
	if int(i) <= 80:
		print(chr((i+42)),end="")
	elif int(i) > 80:
		print(chr((i-16)),end="")



