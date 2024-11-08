import base64

# Файлаас base64 шифрлэгдсэн текст унших
b = b''
with open("data.txt", 'rb') as f:
    b = f.read().strip()  # Хоосон зайг устгах

# Алдааг засах
while True:
    # base64 шифрлэгдсэн текстийг 4-ийн хуваагддаг болгох
    padding_length = (-len(b) % 4)
    if padding_length:  # Хэрэв нэмэх шаардлагатай байвал
        b += b'=' * padding_length

    try:
        b = base64.b64decode(b)  # base64 шифрлэгдсэн текстийг задлах
        if b'CTFlearn' in b:      # "CTFlearn" текст байгаа эсэхийг шалгах
            print(b.decode())     # Олдсон текстийг хэвлэх
            break                 # Циклыг зогсоох
    except Exception as e:
        print(f"Error decoding: {e}")
        break
