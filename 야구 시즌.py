for _ in range(int(input())):
  N, M, K, D = map(int, input().split())
  exp = 2 * D // (K * N * M * (M - 1) + M * M * N * (N - 1))
  if exp:
    print(M * (M - 1) * N * K * exp // 2 + M * M * N * (N - 1) * exp // 2)
  else:
    print(-1)