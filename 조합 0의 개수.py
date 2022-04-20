N, M = map(int, input().split())
five = [5**i for i in range(1, 15)]
two = [2**i for i in range(1, 32)]

def sollution(N, arr):
  result = 0
  for i in arr:
    if N // i == 0:
      return result
    result += N // i

print(min(sollution(N, five) - (sollution(N-M, five) + sollution(M, five)), sollution(N, two) - (sollution(N-M, two) + sollution(M, two))))