key = 42
for i in range(1000000000):
	if (key * i) % 52 == 1:
		print(i)
		break