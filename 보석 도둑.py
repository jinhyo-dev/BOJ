from sys import stdin
import heapq
input = stdin.readline

N, K = map(int, input().split())
jewel = []
bag = []
for _ in range(N):
  heapq.heappush(jewel, list(map(int, input().split())))

for _ in range(K):
  bag.append(int(input()))
bag.sort()

answer = 0
tmp = []
for i in bag:
  while jewel and i >= jewel[0][0]:
    heapq.heappush(tmp, -heapq.heappop(jewel)[1])
  if tmp:
    answer -= heapq.heappop(tmp)
  elif not jewel:
    break
print(answer)