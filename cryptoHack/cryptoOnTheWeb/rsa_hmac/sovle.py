import jwt

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VybmFtZSI6InVzZXIiLCJhZG1pbiI6ZmFsc2V9.axUTiZm-iXft3UG7PldwBYaHYVxL0AEnurDueibKHsGFIJrb5Jw8USbWyW2uSjJ2JX7BcpwsQXhX4IUAC1y03Q9HU-iBRk845woZETiJSMlGb5rFoH6TyWCkLld9jIf8-0r-1exj2nCRzHk8NRHBjzsSowbLwkB8GEE-iruU3XBhS67oixpP_3Gbx2QAe3xp7IxQcod1bucqqM9AfZl9-2xdc8khe-ZzEsg9jDgfmWJILxOxOUZ2s9lsEaQF5ih7kCdE0ED2vM6zoivQ5NMuA0vSrQn75qfhsOpAgrqoV1MusF9oyP0KXg41hLoB0AiFZLFJ8zJfFSldLr45rfv06g"


from Crypto.PublicKey import RSA

# Your public key
public_key_str = """-----BEGIN RSA PUBLIC KEY-----
MIIBCgKCAQEAvoOtsfF5Gtkr2Swy0xzuUp5J3w8bJY5oF7TgDrkAhg1sFUEaCMlR
YltE8jobFTyPo5cciBHD7huZVHLtRqdhkmPD4FSlKaaX2DfzqyiZaPhZZT62w7Hi
gJlwG7M0xTUljQ6WBiIFW9By3amqYxyR2rOq8Y68ewN000VSFXy7FZjQ/CDA3wSl
Q4KI40YEHBNeCl6QWXWxBb8AvHo4lkJ5zZyNje+uxq8St1WlZ8/5v55eavshcfD1
0NSHaYIIilh9yic/xK4t20qvyZKe6Gpdw6vTyefw4+Hhp1gROwOrIa0X0alVepg9
Jddv6V/d/qjDRzpJIop9DSB8qcF1X23pkQIDAQAB
-----END RSA PUBLIC KEY-----"""

# Load the public key
key = RSA.import_key(public_key_str)

# Show the modulus and exponent of the public key
print(f"Public Key Modulus: {key.n}")
print(f"Public Key Exponent: {key.e}")



# decoded = jwt.decode(token, PUBLIC_KEY, algorithms=['HS256', 'RS256'])

# decoded["admin"] = True
# print(decoded)

# f979cd4e43a925ef64963e7c4bb8b589493dc07d828d161c59ad13cf9bcfeb71

n = 24050211030239216188802288366362217662480433802624310761127878134597668372924234482046646170921386405599288094150679241490153384664076927603060141272460337234289054592391045587705062293563577056646724886238008467470514960058892954958201313175223093165860145037984636214895781785206245700790689589211768947778773449957463613873726569953911141629168067428305350816029911766849656621467226132565294295011015512107110995166838427597251833188017289525786156286820103948075012643118694344565570220900901414202285145944733715288313682018702924320764226559071124926270986854282661795362411522920297696004809790452107808991633
e = 65537