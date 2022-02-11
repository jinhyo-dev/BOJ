N, M = map(int, input().split())
list = list(map(int, input().split()))
cnt = 0
for i in range(N):
  for j in range(i+1, N):
    for k in range(j+1, N):
      if list[i] + list[j] + list[k] > M:
        continue
      else:
        cnt = max(cnt, list[i] + list[j] + list[k])
print(cnt) 