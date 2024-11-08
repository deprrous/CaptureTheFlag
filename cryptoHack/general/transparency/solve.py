from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
pubKey = ""
with open("transparency.pem","r") as f:
    pubKey = RSA.import_key(f.read())

if pubKey.has_private():
    print("this is priv")
else:
    cipher = PKCS1_OAEP.new(pubKey)
    # decrypted_message = cipher.decrypt(encrypted_message)
    # print("Decrypted message:", decrypted_message)

print(pubKey.n)
n = 23421622285641341405633616890150413771071492791662619237015532689271209254675255214187772835143801809039951016782376679973376782695533167272817148034946155291022588458116896449130547957859630601417029406537713697722216484126508404669492574651738700785323627803802967097814192155713988206765677255996453746570221203605464683698139759068201745805643226602309648177720842369737425307662674524530757570626970232537549824005998393609021861773134215542450556839250804799098903483152012713520167414613141526302727512388972623173809195225592109964416682348203058784103484962051844890398766510080562420295832329553237528041393
e = 65537
# print(pubKey.d)
# print()
# print(pubKey.e)
# print()
# print(pubKey.m)

# print()
print(pubKey.c)
