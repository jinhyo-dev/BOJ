from itertools import product

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
pd = list(product(arr, repeat=M))

for i in pd:
  print(str(i).replace('(', '').replace(')', '').replace(',', ''))
