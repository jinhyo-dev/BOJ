A, B = map(int, input().split())
C, D = map(int, input().split())
sumValues = []

sumValues.append(A / C + B / D)
sumValues.append(C / D + A / B)
sumValues.append(D / B + C / A)
sumValues.append(B / A + D / C)

print(sumValues.index(max(sumValues)))