N = int(input())
arr = list(map(int, input().split()))
uphill = []
tmp = 0
for i in range(1, N):
  if arr[i] > arr[i-1]:
    tmp += arr[i] - arr[i-1]
    if i == N-1:
      uphill.append(tmp)
  else:
    uphill.append(tmp)
    tmp = 0

print(max(uphill))