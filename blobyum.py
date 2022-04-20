from collections import deque
import sys
input = sys.stdin.readline
dq = deque()
answer = 0
N, K = map(int, input().split())
dp = [0] * (N * 2)

arr = list(map(int, input().split()))

for i in range(2):
  for j in arr:
    dq.append(j)

dp[0] = dq[0]

for i in range(1, K):
  dp[i] = dp[i-1] + dq[i]

for i in range(K, 2*N):
  dp[i] = dp[i-1] - dq[i-K] + dq[i]
  answer = max(answer, dp[i])

print(answer)