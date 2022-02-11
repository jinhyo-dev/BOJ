list = []
for i in range(1, 1001):
  for j in range(i):
    list.append(i)

A, B = map(int, input().split())
cnt = 0

for i in range(A-1, B):
  cnt += list[i]

print(cnt)
