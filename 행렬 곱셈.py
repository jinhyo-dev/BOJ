N, M = map(int, input().split())
A_arr = []
B_arr = []

for _ in range(N):
  A_arr.append(list(map(int, input().split())))

M, K = map(int, input().split())

result = [[0 for _ in range(K)] for _ in range(N)]

for _ in range(M):
  B_arr.append(list(map(int, input().split())))

for i in range(N):
  for j in range(K):
    for k in range(M):
      result[i][j] += A_arr[i][k] * B_arr[k][j]

for i in result:
  print(*i)