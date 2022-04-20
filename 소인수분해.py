N = int(input())
M = 2
while N != 1:
    if N % M == 0:
        print(M)
        N = N // M
    else:
        M += 1