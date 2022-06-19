N, M = map(int, input().split())
for _ in range(N):
  string = list(input())
  string.reverse()
  print(*string, sep='')