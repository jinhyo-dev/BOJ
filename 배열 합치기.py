N, M = map(int, input().split())
A = list(map(int, input().rstrip().split()))
B = list(map(int, input().rstrip().split()))

answer = A + B
answer.sort()
print(*answer)