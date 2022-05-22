for _ in range(int(input())):
  N, M = map(int, input().split())
  U = (M * 2) - N
  T = N - M
  print(U, T)