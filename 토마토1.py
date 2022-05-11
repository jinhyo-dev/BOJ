from collections import deque
from sys import stdin
input = stdin.readline

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
q = deque([])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0

for i in range(N):
  for j in range(M):
    if graph[i][j] == 1:
      q.append([i, j])

def bfs():
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx, ny = dx[i] + x, dy[i] + y
      if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
        graph[nx][ny] = graph[x][y] + 1
        q.append([nx, ny])

bfs()
for i in graph:
  for j in i:
    if j == 0:
      print(-1)
      exit(0)
  answer = max(answer, max(i))
print(answer -1)