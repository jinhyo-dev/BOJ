result = []
N = int(input())
for i in range(N):
  card = list(map(int, input().split()))
  maxNum = 0
  for i in range(5):
    for j in range(i+1, 5):
      for k in range(j+1, 5):
        tmp = (card[i] + card[j] + card[k]) % 10
        if tmp >= maxNum:
          maxNum = tmp
  result.append(maxNum)

for i in range(N-1, -1, -1):
  if result[i] == max(result):
    print(i + 1)
    break