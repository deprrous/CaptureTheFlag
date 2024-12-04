def permutate(payload, pbox):
    return bytes([payload[x] for x in pbox])
salt = "Ohnpow=="
p = [7, 0, 8, 2, 4, 16, 18, 5, 9, 17, 13, 6, 1, 14, 10, 15, 11, 12, 19, 3]