for _ in range(int(input())):
  N = int(input())
  for i in range(2, N + 1):
    cnt = 0
    if N % i == 0:
      while N % i == 0:
        N //= i
        cnt += 1
      print(i, cnt)
    elif N == 1:
      break
