N, M = map(int, input().split())
arr = sorted(map(int, input().split()))

visited = [False] * N
answer = []

def dfs(v):
  if v == M:
    print(*answer)
  for i in range(N):
    if not visited[i]:
      answer.append(arr[i])
      visited[i] = True
      dfs(v + 1)
      answer.pop()
      visited[i] = False

dfs(0)