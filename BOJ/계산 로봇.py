N, M = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(N)] + [[0] * M]
dp = [[0] * M for _ in range(N + 1)]

for j in range(M):
  for i in range(N):
    if j == 0:
      dp[i][j] = 0
    
    else:
      dp[i][j] = max (
        dp[i-1][j-1] + arr[i-1][j-1],
        dp[i][j-1] + arr[i][j-1],
        dp[i+1][j-1] + arr[i+1][j-1]
      )

print(max(map(max, dp)))