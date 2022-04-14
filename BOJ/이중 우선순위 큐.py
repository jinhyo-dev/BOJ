import heapq
import sys
input = sys.stdin.readline

for _ in range(int(input())):
  K = int(input())
  q1, q2 = [], []
  visited = [False] * K

  for i in range(K):
    cmd, N = input().split()

    if cmd == 'I':
      heapq.heappush(q1, (int(N), i))
      heapq.heappush(q2, (-int(N), i))
      visited[i] = True
    
    else:
      if N == '1':
        while q2 and not visited[q2[0][1]]:
          heapq.heappop(q2)
        if q2:
          visited[q2[0][1]] = False
          heapq.heappop(q2)
      else:
        while q1 and not visited[q1[0][1]]:
          heapq.heappop(q1)
        if q1:
          visited[q1[0][1]] = False
          heapq.heappop(q1)

  while q1 and not visited[q1[0][1]]:
    heapq.heappop(q1)
  
  while q2 and not visited[q2[0][1]]:
    heapq.heappop(q2)
  
  print("EMPTY" if not q1 or not q2 else f"{-q2[0][0]} {q1[0][0]}")