N = int(input())
M = int(input())
arr = []
cnt = 0

for i in range(N, M+1):
    for j in range(2,i+1):
        if i % j == 0:
            cnt += 1
    if cnt == 1:
        arr.append(i)
    cnt = 0

if not arr:
    print(-1)
if arr:
    print(sum(arr))
    print(arr[0])