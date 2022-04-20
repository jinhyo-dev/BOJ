from collections import deque
q = deque()
for i in range(int(input())):
    N = int(input())
    q.pop() if N == 0 else q.append(N)
print(sum(q))