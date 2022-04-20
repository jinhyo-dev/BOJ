import sys
input = sys.stdin.readline
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.sort(reverse=True)
tmp = 0
cnt = 0
C = K
while True:
  if tmp == K:
    break
  for i in coins:
    if C - i >= 0:
      tmp += i
      cnt += 1
      C -= i
      break
print(cnt)