import sys
sys.setrecursionlimit(10 ** 6) #파이썬은 재귀 깊이 제한이 있어 그 제한을 늘려주기 위한 코드
input = sys.stdin.readline
N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
  a, b = map(int, input().split())
  tree[a].append(b)
  tree[b].append(a)

visited = [False] * (N + 1)

def dfs(node):
  for i in tree[node]:
    if visited[i] == False:
      visited[i] = node
      dfs(i)

dfs(1)

for i in range(2, N + 1):
  print(visited[i])