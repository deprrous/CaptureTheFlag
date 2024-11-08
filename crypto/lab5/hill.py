import numpy as np

def mod_inverse(matrix, modulus):
    det = int(round(np.linalg.det(matrix)))  # Матрицын детерминант
    print("det: ",det)
    det_inv = pow(det, -1, modulus)  # Модулосон детерминантын инверс
    print("det_inv: ",det_inv)
    matrix_modulus_inv = det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    print("matrix_mod_inv:\n",matrix_modulus_inv)
    return matrix_modulus_inv

def prepare_text(text, n):
    text = text.upper().replace(" ", "")
    # Хэрвээ текстийн урт бүлгийн хэмжээтэй биш бол 'X' нэмнэ
    while len(text) % n != 0:
        text += 'X'
    return text

def text_to_numbers(text):
    return [ord(char) - ord('A') for char in text]

def numbers_to_text(numbers):
    return ''.join([chr(num + ord('A')) for num in numbers])

def hill_encrypt(plain_text, key_matrix):
    n = key_matrix.shape[0]
    print("n: ",n)
    plain_text = prepare_text(plain_text, n)
    numbers = text_to_numbers(plain_text)
    encrypted = []
    for i in range(0, len(numbers), n):
        block = np.array(numbers[i:i+n])
        print("check dot(): \n",key_matrix.dot(block))
        cipher_block = key_matrix.dot(block) % 26
        encrypted.extend(cipher_block)
    return numbers_to_text(encrypted)

def hill_decrypt(cipher_text, key_matrix):
    n = key_matrix.shape[0]
    cipher_text = prepare_text(cipher_text, n)
    numbers = text_to_numbers(cipher_text)
    inverse_key = mod_inverse(key_matrix, 26)
    decrypted = []
    for i in range(0, len(numbers), n):
        block = np.array(numbers[i:i+n])
        plain_block = inverse_key.dot(block) % 26
        decrypted.extend(plain_block)
    return numbers_to_text(decrypted)

# Жишээ ашиглалт
if __name__ == "__main__":
    key = [[6, 24, 1],
           [13, 16, 10],
           [20, 17, 15]]
    key_matrix = np.array(key)
    print("key_matrix: ",key_matrix)
    
    plain_text = "ACT"
    encrypted = hill_encrypt(plain_text, key_matrix)
    print(f"Нийтлэл: {plain_text}")
    print(f"Шифрлэгдсэн: {encrypted}")
    
    decrypted = hill_decrypt(encrypted, key_matrix)
    print(f"Тайлагдсан: {decrypted}")

