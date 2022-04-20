N, D = map(int, input().split())
cnt = 0
for i in range(1, N+1):
  for j in str(i):
    if int(j) == D:
      cnt += 1
print(cnt)