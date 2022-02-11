bomal = int(input())
A, B, C = map(int, input().split())
A *= bomal // 12
B *= A // 8
C *= B // 5

print(C)    