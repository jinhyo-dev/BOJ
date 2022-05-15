from math import ceil
N = int(input())
arr = list(map(int, input().split()))
Y = M = 0
for i in range(N):
  if arr[i] % 60 == 0:
    arr[i] += 1
  Y += ceil(arr[i] / 30) * 10
  M += ceil(arr[i] / 60) * 15

if Y == M:
  print(f'Y M {Y}')
else:
  print(f'M {M}' if Y > M else f'Y {Y}')