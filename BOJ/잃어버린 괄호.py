equation = input().split('-')
num = []
for i in equation:
  cnt = 0
  plus = i.split('+')
  for j in plus:
    cnt += int(j)
  num.append(cnt)
N = num[0]
for i in range(1, len(num)):
  N -= num[i]
print(N)