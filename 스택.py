from collections import deque
from sys import stdin
input = stdin.readline
s = deque()
for _ in range(int(input())):
  command = list(input().split())
  if command[0] == 'push':
    s.appendleft(int(command[1]))
  elif command[0] == 'pop':
    if s:
      print(s.popleft())
    else:
      print(-1)
  elif command[0] == 'size':
    print(len(s))
  elif command[0] == 'empty':
    print(0 if s else 1)
  elif command[0] == 'top':
    print(s[0] if s else -1)