import heapq

N = int(input())
arr = []
for i in range(N):
  arr.append(list(map(int, input().split())))

arr.sort()
pq = []
for i in arr:
  heapq.heappush(pq, i[1])
  if (len(pq) > i[0]):
    heapq.heappop(pq)

print(sum(pq))