e=62895773587676709375416894609009828307181046790386631380225909085247764483330712838119732737968106312930354304958236890091063087611968693854623053319527552160005051500839789097307659468506693959126497307196535243659873492952032255916656957904235379845074668340991518970076361028974969686354786774071385237031
n=110553301559811869270400695904667508650148290037914523427839870828574921049233976899107028234597824291703443398198262313982352991068747117399650490687855763687503242652110464245169791388110452102261447378123132295904875821906253847563381646822606338964366173004785815183948348466862375620156267465072729961359
c=72230954434201537962042735242114774388304233641471782183750814473213046869700737444380907526841567266616291229996491073860991567496046357811665883282533679022743261696179937896549613499797623206561903768777533664988384745854998142753552120724793659942545751265242379819673304683944280728292087317773521641421
from Crypto.Util.number import long_to_bytes

phi = n-1

d = pow(e,-1,phi)
print(d)
# m = long_to_bytes(pow(c,d,n))

# print(m)

