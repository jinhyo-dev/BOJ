from collections import deque
N, K = map(int, input().split())
q = deque([i for i in range(1, N+1)])

print('<', end='')
while len(q) != 1:
  for _ in range(K-1):
    q.append(q.popleft())
  print(q.popleft(), end=', ')
print(f'{q.popleft()}>')