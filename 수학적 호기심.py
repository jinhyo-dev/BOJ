from sys import stdin
input = stdin.readline
for _ in range(int(input())):
  N, M = map(int, input().split())
  cnt = 0
  for a in range(N):
    for b in range(a+1, N):
      try:
        if ((a**2 + b**2 + M) / (a * b)).is_integer():
          cnt += 1
      except ZeroDivisionError:
        pass
  print(cnt)