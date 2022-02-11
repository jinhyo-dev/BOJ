T = int(input())
numbers = list(map(int, input().split(' ')))
primeNum = 0

for i in numbers:
  cnt = 0
  if i == 1:
    continue
  for j in range(2, i+1):
    if i % j == 0:
      cnt += 1
  if cnt == 1: 
    primeNum += 1
print(primeNum)