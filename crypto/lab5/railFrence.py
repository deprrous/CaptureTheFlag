def rail_fence_encrypt(plain_text, num_rails):
    rail = ['' for _ in range(num_rails)]
    direction = None
    current_rail = 0

    for char in plain_text:
        rail[current_rail] += char
        if current_rail == 0:
            direction = 1
        elif current_rail == num_rails -1:
            direction = -1
        current_rail += direction

    return ''.join(rail)

def rail_fence_decrypt(cipher_text, num_rails):
    # Шатын дагуу үсгийн тоог тооцоолох
    rail_len = [0] * num_rails
    direction = None
    current_rail = 0
    for char in cipher_text:
        rail_len[current_rail] +=1
        if current_rail ==0:
            direction =1
        elif current_rail == num_rails -1:
            direction = -1
        current_rail += direction

    # Шатанд байрлуулах үсгийг хуваах
    rail = []
    index =0
    for r in range(num_rails):
        rail.append(cipher_text[index:index+rail_len[r]])
        index += rail_len[r]

    # Мессэжийг дахин бичих
    result = []
    direction = None
    current_rail =0
    rail_indices = [0] * num_rails
    for i in range(len(cipher_text)):
        result.append(rail[current_rail][rail_indices[current_rail]])
        rail_indices[current_rail] +=1
        if current_rail ==0:
            direction =1
        elif current_rail == num_rails -1:
            direction = -1
        current_rail += direction

    return ''.join(result)

# Жишээ ашиглалт
if __name__ == "__main__":
    plain_text = "WE ARE DISCOVERED FLEE AT ONCE"
    plain_text = plain_text.replace(" ", "").upper()
    num_rails = 3
    encrypted = rail_fence_encrypt(plain_text, num_rails)
    print(f"Нийтлэл: {plain_text}")
    print(f"Шифрлэгдсэн: {encrypted}")
    
    decrypted = rail_fence_decrypt(encrypted, num_rails)
    print(f"Тайлагдсан: {decrypted}")

