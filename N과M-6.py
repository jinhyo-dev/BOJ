N, M = map(int, input().split())
arr = sorted(map(int, input().split()))
visited = [False] * N
answer = []

def dfs(depth):
  if depth == M:
    print(*answer)
    return

  for i in range(N):
    if not visited[i]:
      if depth == 0 or arr[i] > answer[depth - 1]:
        answer.append(arr[i])
        visited[i] = True
        dfs(depth + 1)
        visited[i] = False
        answer.pop()

dfs(0)
