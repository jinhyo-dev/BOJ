N = int(input())
graph = [[]*N for _ in range(N+1)]
visited = [False] * (N+1)
cnt = 0

def dfs(start):
  global cnt
  visited[start] = True
  for i in graph[start]:
    if visited[i] == 0:
      dfs(i)
      cnt += 1

for _ in range(int(input())):
  A, B = map(int, input().split())
  graph[A].append(B)
  graph[B].append(A)

dfs(1)
print(cnt)