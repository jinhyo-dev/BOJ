import sys
from collections import deque
input = sys.stdin.readline
q = deque()

for _ in range(int(input())):
  A = input().split()
  
  if A[0] == 'push': q.append(A[1])
  elif A[0] == 'pop': print(q.popleft() if len(q) else -1)
  elif A[0] == 'size': print(len(q))
  elif A[0] == 'empty': print(int(len(q) == 0))
  elif A[0] == 'front': print(q[0] if len(q) else -1)
  elif A[0] == 'back': print(q[-1] if len(q) else -1)