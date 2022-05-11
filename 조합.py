from math import factorial
N, M = map(int, input().split())
Fac1 = factorial(N)
Fac2 = (factorial(N - M)) * (factorial(M))
print(Fac1 // Fac2)