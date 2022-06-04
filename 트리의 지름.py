import sys
from collections import deque

q = deque()
input = sys.stdin.readline
V = int(input())
graph = [[] for _ in range(V+1)]

for _ in range(V):
  arr = list(map(int, input().split()))
  for i in range(1, len(arr)-2, 2):
    graph[arr[0]].append([arr[i], arr[i+1]])

def dfs(start):
  visited = [False] * (V+1)
  q.append(start)
  visited[start] = True
  max_val = [0, 0]
  while q:
    node = q.popleft()
    for e, w in graph[node]:
      if not visited[e]:
        visited[e] = visited[node] + w
        q.append(e)
        if visited[e] > max_val[0]:
          max_val = visited[e], e
  return max_val

distance, n = dfs(1)
distance, n = dfs(n)
print(distance - 1)