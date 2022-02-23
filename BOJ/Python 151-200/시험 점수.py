N = list(map(int, input().split()))
M = list(map(int, input().split()))
print(sum(M) if sum(M) > sum(N) else sum(N))