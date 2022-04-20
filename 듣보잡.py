import sys
N, M = map(int, input().split())

list_N = set()
for _ in range(N):
  list_N.add(input())

list_M = set()
for _ in range(M):
  list_M.add(input())

list_NM = sorted(list(list_N & list_M))
print(len(list_NM), *list_NM, sep='\n')