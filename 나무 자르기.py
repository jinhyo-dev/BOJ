import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
start, end = 0, max(arr)

while start <= end:
  middle = (start+end) // 2
  tree = 0
  for i in arr:
    if i > middle:
      tree += i - middle
  
  if tree >= M:
    start = middle + 1
  else:
    end = middle - 1

print(end)