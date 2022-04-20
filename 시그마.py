A, B = map(int, input().split())
print(int((A + B) * (abs(A - B) + 1) / 2))