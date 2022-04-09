from math import gcd
for _ in range(int(input())):
  sum = 0
  arr = list(map(int, input().split()))

  for i in range(1, len(arr)):
    for j in range(i+1, len(arr)):
      sum += gcd(arr[i], arr[j])
  print(sum)