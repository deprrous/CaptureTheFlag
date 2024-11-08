import string

def generate_playfair_matrix(key):
    # Түлхүүр үсгийг боловсруулж, давтагдашгүй үсгүүдийг хадгална
    key = key.upper().replace('J', 'I')
    seen = set()
    matrix = []
    for char in key:
        if char in string.ascii_uppercase and char not in seen:
            seen.add(char)
            matrix.append(char)
    # Бусад үсгүүдийг нэмнэ
    for char in string.ascii_uppercase:
        if char == 'J':
            continue
        if char not in seen:
            seen.add(char)
            matrix.append(char)
    # 5x5 квадрат үүсгэнэ
    playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
    return playfair_matrix

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(row))
    print()

def find_position(matrix, char):
    for row_idx, row in enumerate(matrix):
        if char in row:
            return row_idx, row.index(char)
    return None

def process_text(text, for_encryption=True):
    text = text.upper().replace('J', 'I')
    # Буква бус тэмдэгтүүдийг арилгах
    text = ''.join([c for c in text if c in string.ascii_uppercase])
    processed = ""
    i = 0
    while i < len(text):
        a = text[i]
        b = ''
        if (i + 1) < len(text):
            b = text[i + 1]
            if a == b:
                b = 'X'
                i += 1
            else:
                i += 2
        else:
            b = 'X'
            i += 1
        processed += a + b
    return processed

def playfair_encrypt(plain_text, key):
    matrix = generate_playfair_matrix(key)
    # print("Playfair Matrix:")
    # print_matrix(matrix)
    plain_text = process_text(plain_text)
    cipher_text = ""
    for i in range(0, len(plain_text), 2):
        a = plain_text[i]
        b = plain_text[i+1]
        pos_a = find_position(matrix, a)
        pos_b = find_position(matrix, b)
        
        if pos_a is None or pos_b is None:
            raise ValueError(f"Тухайн үсэг матрицад байхгүй: '{a}' эсвэл '{b}'")
        
        row_a, col_a = pos_a
        row_b, col_b = pos_b
        
        if row_a == row_b:
            cipher_text += matrix[row_a][(col_a + 1) % 5]
            cipher_text += matrix[row_b][(col_b + 1) % 5]
        elif col_a == col_b:
            cipher_text += matrix[(row_a + 1) % 5][col_a]
            cipher_text += matrix[(row_b + 1) % 5][col_b]
        else:
            cipher_text += matrix[row_a][col_b]
            cipher_text += matrix[row_b][col_a]
    return cipher_text

def playfair_decrypt(cipher_text, key):
    matrix = generate_playfair_matrix(key)
    # print("Playfair Matrix:")
    # print_matrix(matrix)
    cipher_text = process_text(cipher_text, for_encryption=False)
    plain_text = ""
    for i in range(0, len(cipher_text), 2):
        a = cipher_text[i]
        b = cipher_text[i+1]
        pos_a = find_position(matrix, a)
        pos_b = find_position(matrix, b)
        
        if pos_a is None or pos_b is None:
            raise ValueError(f"Тухайн үсэг матрицад байхгүй: '{a}' эсвэл '{b}'")
        
        row_a, col_a = pos_a
        row_b, col_b = pos_b
        
        if row_a == row_b:
            plain_text += matrix[row_a][(col_a - 1) % 5]
            plain_text += matrix[row_b][(col_b - 1) % 5]
        elif col_a == col_b:
            plain_text += matrix[(row_a - 1) % 5][col_a]
            plain_text += matrix[(row_b - 1) % 5][col_b]
        else:
            plain_text += matrix[row_a][col_b]
            plain_text += matrix[row_b][col_a]
    # Удирдах 'X' тэмдэгтүүдийг хасах
    plain_text = plain_text.replace('X', '')
    return plain_text

# Жишээ ашиглалт:
if __name__ == "__main__":
    key = "PLAYFAIREXAMPLE"
    print(f"Түлхүүр: {key}\n")

    print("Playfair Матриц:")
    matrix = generate_playfair_matrix(key)
    print_matrix(matrix)

    plain_text = "HELLO WORLD"
    print(f"Нийтлэл: {plain_text}")
    try:
        encrypted = playfair_encrypt(plain_text, key)
        print(f"Шифрлэгдсэн: {encrypted}")
    except ValueError as ve:
        print(f"Алдаа: {ve}")

    try:
        decrypted = playfair_decrypt(encrypted, key)
        print(f"Тайлагдсан: {decrypted}")
    except ValueError as ve:
        print(f"Алдаа: {ve}")

