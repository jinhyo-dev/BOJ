N = int(input())
result = 0
K = 1

while N > 0:
  if N < K:
    K = 1
  N -= K
  K += 1
  result += 1
print(result)