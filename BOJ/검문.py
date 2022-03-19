import sys
from math import gcd
input = sys.stdin.readline

arr = sorted([int(input()) for _ in range(int(input()))])
result = []

for i in range(1, len(arr)):
  result.append(abs(arr[i] - arr[i - 1]))

target = gcd(*result)
i = 2
result_list = []

while i <= (target**(1/2))+1:
  if target % i == 0:
    result_list.append(i)
    if i != (target//i):
      result_list.append(target//i)
  i += 1

for i in sorted(list(set(result_list))):
    print(i, end=' ')
print(target)