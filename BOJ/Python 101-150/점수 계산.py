score = []
cnt = 0
tmp = []

for i in range(8):
  score.append([int(input()) ,i+1])
score.sort()

for i in range(3, 8):
  tmp.append(score[i][1])
  cnt += score[i][0]
tmp.sort()
print(cnt)
print(*tmp)