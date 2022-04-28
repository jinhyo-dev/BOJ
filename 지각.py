for _ in range(int(input())):
  N = int(input())
  maxValue = 0
  for i in range(N):
    if i * i + 1 <= N:
      maxValue = i
    else:
      break
  print(maxValue)