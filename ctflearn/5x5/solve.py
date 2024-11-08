import string
a = string.ascii_lowercase
a = a[0:len(a)-1]
print(a)

b = "4-4,2-3,4-5,3-2,1-2,4-3,4-5,3-5"
c = b.split(",")
k = []
j = 0
for i in c:
    temp = i.split("-")
    k.append(temp)
    print(temp)
    
    j = j +1
