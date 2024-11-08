h = "131017171A48221A1D170F"
h = h.lower()
print(h)
l = []
for i in range(len(h)):
	if i == 0:
		continue
	elif i % 2 == 1:
		temp = (h[i-1] + h[i])
		l.append(int(temp,16))


for i in l:
	print(chr((i+85)),end = "")