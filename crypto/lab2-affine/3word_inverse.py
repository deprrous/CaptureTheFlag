p='Шуурхай мэдээ Майкрософттой холбоотой мэдээллийн технологийн тасалдал Шинэ мэдээИх уншсан сэтгэгдэлтэй'
p=p.lower()
p1=p.split()
for el in p1:
    el1=el[0:3][::-1]+el[3:]
    el2=el1[0:3][::-1]+el1[3:]
    print(el1)
    print(el2)
    print()
