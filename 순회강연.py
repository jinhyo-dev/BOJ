import heapq

N = int(input())
arr = []
for i in range(N):
  arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: x[1])
pq = []
for i in arr:
  heapq.heappush(pq, i[0])
  if (len(pq) > i[1]):
    heapq.heappop(pq)

print(sum(pq))