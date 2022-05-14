N, K = map(int, input().split())
sum =  K * (K+1) // 2
if sum > N:
  print(-1)
elif (N - sum) % K == 0:
  print(K - 1)
else:
  print(K)