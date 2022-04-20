import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
start, end = 1, max(arr)

while start <= end:
  mid = (start + end) // 2
  lan = 0
  for i in arr:
    lan += i // mid
  
  if lan >= M:
    start = mid + 1
  else:
    end = mid - 1

print(end)