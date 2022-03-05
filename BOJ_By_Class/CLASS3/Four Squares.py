N = int(input())
dp = [0, 1]
for i in range(2, N+1):
  minor = 1e9
  j = 1
  while (j**2) <= i:
    minor = min(minor, dp[i - (j**2)])
    j += 1
  dp.append(minor+1)
print(dp[N])