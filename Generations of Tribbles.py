def koong(n):
  if n < 2:
    return 1
  elif n == 2:
    return 2
  elif n == 3:
    return 4
  if dp[n]:
    return dp[n]
  dp[n] = koong(n-1) + koong(n-2) + koong(n-3) + koong(n-4)
  return dp[n]

dp = [0] * 68

for _ in range(int(input())):
  print(koong(int(input())))
