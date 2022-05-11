from collections import deque
from sys import stdin
q = deque([])
input = stdin.readline
graph = []
M, N, H = map(int, input().split())
answer = 0

for i in range(H):
  tmp = []
  for j in range(N):
    tmp.append(list(map(int, input().split())))
    for k in range(M):
      if tmp[j][k] == 1:
        q.append([i, j, k])
  graph.append(tmp)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while q:
  x, y, z = q.popleft()
  for i in range(6):
    nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
    if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M and graph[nx][ny][nz] == 0:
      q.append([nx, ny, nz])
      graph[nx][ny][nz] = graph[x][y][z] + 1

for i in graph:
  for j in i:
    for k in j:
      if k == 0:
        print(-1)
        exit(0)
    answer = max(answer, max(j))
print(answer - 1)