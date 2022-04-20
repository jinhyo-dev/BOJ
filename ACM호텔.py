T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    aptNum = N//H + 1
    floor = N % H
    if N % H == 0:
        aptNum = N//H
        floor = H
    print(f'{floor*100+aptNum}')