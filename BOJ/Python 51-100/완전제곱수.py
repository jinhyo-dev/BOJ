import sys
from math import ceil
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
arr = []
for i in range(ceil(N**0.5), int(M**0.5)+1):
  arr.append(i**2)  
if arr: 
  print(sum(arr))
  print(arr[0])
else: print(-1)