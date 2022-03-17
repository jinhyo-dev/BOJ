cnt = 0
N = int(input())
tea = list(map(int, input().split()))
for i in tea:
    if i == N:
        cnt += 1
print(cnt)