for _ in range(int(input())):
  cnt = 0
  N, D = map(int, input().split())
  for _ in range(N):
    v, f, c = map(int, input().split())
    des = 0
    if f / c * v >= D:
      cnt += 1
  print(cnt)