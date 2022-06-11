import sys
input = sys.stdin.readline
for _ in range(int(input())):
  k = 0
  square = []
  x = [] * 5
  y = [] * 5
  for _ in range(4):
    n, m = map(int, input().split())
    x.append(n)
    y.append(m)
  for i in range(4):
    for j in range(i + 1, 4):
      square.append((x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j]))
      k += 1
  square.sort()
  print(
    1 if square[0] == square[1] and square[1] == square[2] and square[2] == square[3] and square[4] == square[5] else 0)