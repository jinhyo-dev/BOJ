import heapq

arr = []

for _ in range(int(input())):
  heapq.heappush(arr, float(input()))
print(arr)