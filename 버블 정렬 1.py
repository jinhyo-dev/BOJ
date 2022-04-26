sum = 0      

A, K = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(A):
  for j in range(0, A - i -1):
    if arr[j] > arr[j+1]:
      arr[j], arr[j+1] = arr[j+1], arr[j]
      sum += 1
      if sum == K:
        print(min(arr[j], arr[j+1]), max(arr[j], arr[j+1]))

if sum < K:
  print(-1)