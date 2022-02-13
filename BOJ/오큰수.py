import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
answer = [-1] * N
s = []
s.append(0)
for i in range(1, N):
  while s and arr[s[-1]] < arr[i]:
    answer[s.pop()] = arr[i]
  s.append(i)

print(*answer)