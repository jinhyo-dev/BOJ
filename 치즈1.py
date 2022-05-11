from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
q = deque()

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
cheese = []
time = 0

def bfs():
  visited = [[False] * M for _ in range(N)]
  q.append([0, 0])
  cnt = 0

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if 0 <= nx < N and 0 <= ny < M:
        if graph[nx][ny] == 0 and visited[nx][ny] == False:
          visited[nx][ny] = True
          q.append([nx, ny])
        elif graph[nx][ny] == 1:
          graph[nx][ny] = 0
          cnt += 1
          visited[nx][ny] = True
  return cnt

while True:
  cnt = bfs()
  cheese.append(cnt)
  if cnt == 0:
    break
  time += 1

print(time)
print(cheese[-2])