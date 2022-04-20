import sys
from collections import deque
input = sys.stdin.readline
dq = deque()

for _ in range(int(input())):
  A = input().split()
  
  if A[0] == 'push_front': dq.appendleft(A[1])
  elif A[0] == 'push_back' : dq.append(A[1])
  elif A[0] == 'pop_front': print(dq.popleft() if len(dq) else -1)
  elif A[0] == 'pop_back': print(dq.pop() if len(dq) else -1)
  elif A[0] == 'size': print(len(dq))
  elif A[0] == 'empty': print(int(len(dq) == 0))
  elif A[0] == 'front': print(dq[0] if len(dq) else -1)
  elif A[0] == 'back': print(dq[-1] if len(dq) else -1)