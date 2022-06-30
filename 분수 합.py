from math import gcd

A, B = map(int, input().split())
C, D = map(int, input().split())

N = gcd(A * D + C * B, B * D)
print((A * D + C * B) // N, B * D // N)
