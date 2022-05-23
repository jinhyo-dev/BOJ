from queue import PriorityQueue
pq = PriorityQueue()

N, K = map(int, input().split())
jewel = bag = []
for _ in range(N):
  M, V = map(int, input().split())
  jewel.append([M, V])

for _ in range(K):
  bag.append(int(input()))

jewel.sort()
bag.sort()

for i in range(K):
  j = 0
  while j < N and jewel[j][0] < bag[i]:
    pq.put(jewel[j][1])
    j += 1
  V += pq.top()
  pq.pop()
