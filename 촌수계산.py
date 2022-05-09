from collections import deque

def BFS(V):
    q = deque()
    q.append(V)
    while q:
        V = q.popleft()
        for w in graph[V]:
          if checked[w] == 0:
            checked[w] = checked[V] + 1
            q.append(w)

N = int(input())
graph = [[] for _ in range(N+1)]
A, B = map(int, input().split())
for _ in range(int(input())):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)
checked = [0] * (N+1)
BFS(A)
print(checked[B] if checked[B] > 0 else -1)