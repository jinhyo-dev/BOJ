N, M = map(int, input().split())
arr = []

def dfs(cnt, index):
  if cnt - 1 == M:
    print(' '.join(map(str, arr)))
    return
  
  for i in range(index, N+1):
    arr.append(i)
    dfs(cnt+1, i)
    arr.pop()

dfs(1, 1)