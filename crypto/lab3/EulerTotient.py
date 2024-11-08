n = 7
k = 2
nk = 49
N = [7, 2]


def EulerFunction(N):
    if miller_rabin(N[0]):
        return (N[0] - 1) * N[0] ** (N[1] - 1)
