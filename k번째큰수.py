N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
for i in range(M):
  print(arr[i], end=' ')