from sys import stdin
input = stdin.readline
N = int(input())
arr = [int(input()) for _ in range(N)]
sideStick = arr[-1]
cnt = 1

for i in range(N-2, -1, -1):
  if arr[i] > sideStick:
    sideStick = arr[i]
    cnt += 1

print(cnt)