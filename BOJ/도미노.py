N = int(input())
cnt = 0
for i in range(N+1):
    for j in range(i, N+1):
        cnt += i + j
print(cnt)