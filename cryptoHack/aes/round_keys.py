state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

def addRoundKey(s, k):
    result = []
    for i in range(4):
        for j in range(4):
            result.append(s[i][j] ^ k[i][j])
    return result
a = "".join((chr(i) for i in addRoundKey(state, round_key)))
print(a)
