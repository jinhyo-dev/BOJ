from collections import deque
import sys
k = 1
arr = []
q = deque()
input = sys.stdin.readline
N = int(input())

for i in range(N):
    num = int(input())
    q.append(num)

while len(q):
    if q[0] not in arr:
        print('+')
        arr.append(k)
        k += 1
    else:
        print('-')
        q.popleft()

        