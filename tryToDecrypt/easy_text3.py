# a = FC == 252
# c = FE == 254
# d = 00 == 0
# z = 16 == 22
# A = 17 == 23
# Z = 30 == 48

text = "0A0B1339150B1139070A0B13390510"
h = "0A0B1339150B1139070A0B13390510"
h = h.lower()
print(h)
l = []
for i in range(len(h)):
	if i == 0:
		continue
	elif i % 2 == 1:
		temp = (h[i-1] + h[i])
		temp = int(temp,16)
		l.append(temp)
print(l)
print(0xf3)


for i in  range(len(l)):
	if i >= 252 and i <= 254:
		print(chr(i-155),end="")

	elif i >= 0 and i <= 22:
		print(chr(i+100),end="")


	elif i >= 23 and i <= 48:
		print(chr(i+42),end="")








