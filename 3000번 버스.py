for _ in range(int(input())):
  N = int(input())
  tmp = 1
  for i in range(N - 1):
    tmp = tmp * 2 + 1
  print(tmp)
