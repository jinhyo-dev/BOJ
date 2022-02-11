import sys
input = sys.stdin.readline
arr = []
for _ in range(int(input())):
  n = int(input())
  arr.append(n)

for i in range(2, max(arr)):
  tmp = []
  for j in arr:
    tmp.append(j % i)
    tmp.sort() 
  if tmp[0] == tmp[-1]:
    print(i, end=' ')