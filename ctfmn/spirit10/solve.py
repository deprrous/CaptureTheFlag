import base64
import codecs
spirit = 'RUt1MVpUNGpyR0laWkh5ZUVHQUdGMEkzSDJjbkYwODBwUnVPbnliakFKTVNyVVNZb3pTS0FIRVhGSUVpRlNBWXBSZ3ZaSFNWSTFNbkZKQWZweGdHQVJJSFpKNWhyUlNGRDBwakNEPT0='
def decrypt(spirit):
	 
	for floor in range(5):
		spirit = base64.b64decode(spirit.decode()).encode()
		spirit = codecs.decode(spirit, 'rot_13')
	return spirit
print(decrypt(spirit))