decoded = jwt.decode(token, PUBLIC_KEY, algorithms=['HS256', 'RS256'])

# decoded["admin"] = True
# print(decoded)

# f979cd4e43a925ef64963e7c4bb8b589493dc07d828d161c59ad13cf9bcfeb71