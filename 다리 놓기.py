from math import factorial
for _ in range(int(input())):
  N, M = map(int, input().split())
  print(factorial(M) // (factorial(N) * factorial(M - N)))