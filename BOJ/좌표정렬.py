points = []
N = int(input())
for _ in range(N):
  [x, y] = map(int, input().split())
  points.append([x, y])

points.sort()

for i in range(N):
  print(points[i][0], points[i][1])
