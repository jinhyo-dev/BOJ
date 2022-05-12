A, B, C = map(int, input().split())
N = int(input())
score = []
for _ in range(N):
  sum = 0
  for _ in range(3):
    x, y, z = map(int, input().split())
    sum += (x * A) +  (y * B) + (z * C)
  score.append(sum)
print(max(score))