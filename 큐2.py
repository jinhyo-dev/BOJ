import sys
from collections import deque
q = deque()
for _ in range(int(input())):
  str = list(sys.stdin.readline().split())

  if str[0] == 'push': q.append(str[1])
  elif str[0] == 'pop': print(q.popleft()) if q else print(-1)
  elif str[0] == 'size': print(len(q))
  elif str[0] == 'empty': print(0 if q else 1)
  elif str[0] == 'front': print(q[0]) if q else print(-1)
  elif str[0] == 'back': print(q[-1])  if q else print(-1)