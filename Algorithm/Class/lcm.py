def gcd(N, M):
    if M == 0:
        return N
    else:
        return gcd(M, N % M)


def lcm(N, M):
    return N * M // gcd(N, M)


N, M = 36, 48
a = lcm(N, M)
print(a)
