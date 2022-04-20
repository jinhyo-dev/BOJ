N = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in arr:
    if i%10 == N:
        cnt += 1
print(cnt)