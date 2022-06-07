N, M = map(int, input().split())
arr = list(map(int, input().split()))
sumValue = 0
for i in range(1, N + 1):
  for j in arr:
    if i % j == 0:
      sumValue += i
      break
print(sumValue)