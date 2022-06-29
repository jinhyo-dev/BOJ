import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = []
for _ in range(N):
  arr.append(list(map(int, input().split())))
for _ in range(int(input())):
  i, j, x, y = map(int, input().split())
  cnt = 0
  for a in range(i-1, x):
    for b in range(j-1, y):
      cnt += arr[a][b]

  print(cnt)
