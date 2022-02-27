from collections import deque
cnt = 0
N, M = map(int, input().split())
value = list(map(int, input().split()))
q = deque([k+1 for k in range(N)])

for i in value:
  while True:
    if q.index(i) == 0:
      q.popleft()
      break
    if q.index(i) - 0 <= len(q) - q.index(i):
      q.append(q.popleft())
      cnt += 1
    else:
      q.appendleft(q.pop())
      cnt += 1
print(cnt)