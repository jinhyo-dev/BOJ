N, M = map(int, input().split())
people = N * M
arr = list(map(int, input().split()))
for i in arr:
  print(i - people, end=' ')
