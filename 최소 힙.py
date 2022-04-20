import sys
import heapq
input = sys.stdin.readline
heap = []
for _ in range(int(input())):
  N = int(input())
  if N == 0:
    if not heap:
      print(0)
    else:
      print(heapq.heappop(heap))
  else:
    heapq.heappush(heap, N)