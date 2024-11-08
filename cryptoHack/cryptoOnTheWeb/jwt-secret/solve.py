import jwt
key = 'secret'
enc = jwt.encode({"username":"admin","admin":True},key,algorithm="HS256")
print(enc)
