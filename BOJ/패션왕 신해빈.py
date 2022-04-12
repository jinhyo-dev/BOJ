from collections import Counter

for _ in range(int(input())):
  wear = []
  for _ in range(int(input())):
    A, B = input().split()
    wear.append(B)
  
  num = 1
  result = Counter(wear)

  for key in result:
    num *= result[key] + 1
  print(num - 1)