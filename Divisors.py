for _ in range(int(input())):
  N = int(input())
  cnt = 0
  for i in range(1, N+1):
    if N % i == 0:
      cnt += 1
  print(N, cnt)