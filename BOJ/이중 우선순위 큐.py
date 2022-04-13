import heapq

for _ in range(int(input())):
  K = int(input())
  q1, q2 =[], []
  visited = [False] * K
  
  for i in range(K):
    cmd, N = input().split()

    if cmd == 'I':
      heapq.heappush(q1, int(N), i)
      heapq.heappush(q2, int(N), i)
      visited[i] = True
    
    else:
      
