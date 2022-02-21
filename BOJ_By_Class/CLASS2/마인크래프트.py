import sys
input = sys.stdin.readline
N, M, B = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
time, height = 9223372036854775807, 0
for h in range(257):
  bot = top = 0
  for i in range(N):
    for j in range(M):
      if table[i][j] < h:
        bot += h-table[i][j]
      else:
        top += table[i][j]-h
  if bot > top + B:
    continue
  t = bot + top*2
  if t <= time:
    time = t
    height = h
print(time, height)