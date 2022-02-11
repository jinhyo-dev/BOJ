# n = int(input())
# for i in range(n):
#     H, W, N = map(int, input().split())
#     aptNum = n//H + 1
#     floor = n % H
#     if n % H == 0:
#         aptNum = n//H
#         floor = H
#     print(f'{floor*100+aptNum}')
    
T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    aptNum = N//H + 1
    floor = N % H
    if N % H == 0:
        aptNum = N//H
        floor = H
    print(f'{floor*100+aptNum}')