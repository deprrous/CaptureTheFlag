
from urllib.parse import unquote

url = "%66%6c%61%67%7b%61%6e%64%20%31%3d%31%7d"

d = unquote(url)
print(d)