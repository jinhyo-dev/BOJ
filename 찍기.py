N = int(input())
A = ['A', 'B', 'C']
B = ['B', 'A', 'B', 'C']
G = ['C', 'C', 'A', 'A', 'B', 'B']
A *= N // 2
B *= N // 2
G *= N // 3

score = {'Adrian': 0, 'Bruno': 0, 'Goran': 0}
answer = list(input())

for i in range(N):
  if answer[i] == A[i]:
    score['Adrian'] += 1
  if answer[i] == B[i]:
    score['Bruno'] += 1
  if answer[i] == G[i]:
    score['Goran'] += 1

maxValue = max(score.values())

print(maxValue)

if maxValue == score['Adrian']:
  print('Adrian')
if maxValue == score['Bruno']:
  print('Bruno')
if maxValue == score['Goran']:
  print('Goran')