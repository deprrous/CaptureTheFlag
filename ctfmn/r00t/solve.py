n = 26046973119089779238146179568037058178847368765775817109262324940261253768876388888531445408616646611667993798356515766617501652789688927099058500778050847714066276482449780467899639606175440260886214057219133560601139635289297473865668565723025134965707233942089651675208254009845038203599494602651279719243884447460744506634333423372924060546125315561611860921454679721308658383392555205300644041205570916918562231591290427667532611494109601293580416146116715081493172444016591876792016658764922362471575283422360364251603621082566116764187839936579006163073744996076253938706566657299676791856001480587441549808849
c = 14290868523866273964722480454351241742496754560770411287866364240545205465133043325415097954674683445124120335324232719175923240978375779243530160535829229086178248903329440614230610675335345826064222981484305680023762910468521758179930790834951288492018718972846049121232342421997987815082305525449350731633294447659179739916405181625437672017875404652046383617587566958516752387774586574593084952465343052712990377755070360561259844708365671296432329279932361229056549917569252501482023241743630155509891447991885551464388695508027519359609043392142324602693820342499324351788190775673176643254478610434807865494597
"""from gmpy2 import iroot

# a,b = iroot(c,3)

from Crypto.Util.number import long_to_bytes
phi = n-1

d = pow(3,-1,phi)
m = pow(c,d,n)
print(long_to_bytes(m))"""
e = 3
import owiener
from Crypto.Util.number import long_to_bytes
d = owiener.attack(e,n)
print(d)

