N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()
time = 0
for i in range(N):
  x, y = arr[i]
  if time < x:
    time = x
  time += y
print(time)