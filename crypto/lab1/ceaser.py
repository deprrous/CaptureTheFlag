import string
def ceaser_cipher1(key,m):
	a = string.ascii_lowercase
	output = ""
	for i in m:
		if i == " ":
			output += i
		elif i != " ":
			p = a.index(i)
			c = (p + key) % len(a)
			cl = a[c]
		output += cl
		cl = ""
	return output




def ceaser_cipher2(key,m):
	a = string.ascii_letters + string.digits 
	output = ""
	for i in m:
		if i == " ":
			output += i
		elif i != " ":
			p = a.index(i)
			c = (p + key) % len(a)
			cl = a[c]
		output += cl
		cl = ""
	return output

def ceaser_cipher3(key,m):
	a =  string.ascii_letters
	output = ""
	for i in m:
		if i == " ":
			output += " "
		elif i != " ":
			p = a.index(i)
			c = (p + key) % len(a)
			cl = a[c]
		output += cl 
		cl = ""
	return output

def ceaser_cipher4(key,m):
	a =  string.ascii_lowercase + string.digits
	output = ""
	for i in m:
		if i == " ":
			output += " "
		elif i != " ":
			p = a.index(i)
			c = (p + key) % len(a)
			cl = a[c]
		output += cl 
		cl = ""
	return output


st1 = "WKLV LV FDHVHU FLSKHU"
st2 = "qefp fp ZXbpbo Zfmebo"
st3 = "r52326OZ k1QZ8RS6 MFCC hW1S T25 r529WRS56N MDNCCC"
st4 = "g67f 7f 1Z3f3e 17c63e"

for key in range(1,27):
	print("task 1 key:" , key , " " + ceaser_cipher1(key,st1.lower()))

for key in range(1,53):
	print("task 2key:" , key , " " , ceaser_cipher3(key,st2))
# -----------------------------------------------------
	
for key in range(1,37):
	print(" task 3key:" , key , " " , ceaser_cipher4(key,st3.lower()))

for key in range(1,63):
	print("key:" , key , " " , ceaser_cipher2(key,st3))