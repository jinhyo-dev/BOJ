for _ in range(int(input())):
  score = list(map(int, input().split()))
  score.sort()
  del score[0]
  del score[-1]
  if (score[-1] - score[0]) >= 4:
    print('KIN')
  else:
    print(sum(score))