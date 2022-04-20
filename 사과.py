cnt = 0
for _ in range(int(input())):
  N, M = map(int, input().split())
  cnt += M % N
print(cnt)