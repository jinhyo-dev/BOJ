N = int(input())
M = int(input())
arr = sorted(map(int, input().split()))
cnt = 0
i, j = 0, N - 1
while i < j:
  if arr[i] + arr[j] == M:
    cnt += 1
    i += 1
    j -= 1
  elif arr[i] + arr[j] < M:
    i += 1
  else: j -= 1
print(cnt)