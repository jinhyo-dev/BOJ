from itertools import combinations_with_replacement

N, M = map(int, input().split())
arr = sorted(map(int, input().split()))
C = combinations_with_replacement(arr, M)

for i in C:
  print(' '.join(map(str, i)))
