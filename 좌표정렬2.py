points = []
N = int(input())
for _ in range(N):
  [x, y] = map(int, input().split())
  points.append([y, x])

points.sort()

for i in range(N):
  print(points[i][1], points[i][0])