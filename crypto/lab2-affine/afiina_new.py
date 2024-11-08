# Caesar Cipher 2
def affina(realText,key):
    outText=""
    st="abcdefghijklmnopqrstuvwxyz" 
    #st+="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #st+="0123456789"	    
    for eachLetter in realText:
        if eachLetter!=' ':
            p = st.index(eachLetter)
            C = (p * key) % len(st)
            newLetter = st[C]
        else:
            newLetter = eachLetter
        outText+=newLetter
    return outText
st1='lpgu gu ahhgna igvpqd'
st2='vfCY CY allCNa UCHfOB'
st3='1ng8 g8 aBBgHa WgtnIf'
key,d=3,9
k26=[3,5,7,9,11,15,17,19,21,23,25]
k52=[3,5,7,9,11,15,17,19,21,23,25,27,29,31,33,35,37,41,43,45,47,49,51]
k62=[3,5,7,9,11,13,15,17,19,21,23,25,27,29,33,35,37,39,41,43,45,47,49,51,53,55,57,59,61]
testa,testb,tc='abc','alpha','fqumf'
P='this is affina cipher'
C='fvyc yc appyna gytvmz'

for key in k26:
    print("key: ",key,affina(st1,key))














