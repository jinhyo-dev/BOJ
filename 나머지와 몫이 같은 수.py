N = int(input())
cnt = 0
for i in range(N + 1, N ** 2, N + 1):
  cnt += i
print(cnt)