import sys

input = sys.stdin.readline

N = int(input())
candy = []
for _ in range(N):
  candy.append(list(input()))

result = 1

def check():
  global result
  for i in range(N):
    cnt = 1
    for j in range(1, N):
      if candy[i][j] == candy[i][j-1]:
        cnt += 1
      else:
        result = max(result, cnt)
        cnt = 1
    result = max(result, cnt)

  for i in range(N):
    cnt = 1
    for j in range(1, N):
      if candy[j][i] == candy[j-1][i]:
        cnt += 1
      else:
        result = max(result, cnt)
        cnt = 1
    result = max(result, cnt)

for i in range(N):
  for j in range(1, N):
      if candy[i][j] != candy[i][j-1]:
        candy[i][j], candy[i][j-1] = candy[i][j-1], candy[i][j]
        check()
        candy[i][j], candy[i][j-1] = candy[i][j-1], candy[i][j]

for i in range(N):
  for j in range(1, N):
      if candy[j][i] != candy[j-1][i]:
        candy[j][i], candy[j-1][i] = candy[j-1][i], candy[j][i]
        check()
        candy[j][i], candy[j-1][i] = candy[j-1][i], candy[j][i]

print(result)