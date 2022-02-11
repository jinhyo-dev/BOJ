import sys
A, B = map(int, sys.stdin.readline().split())

list = []

for i in range(1, A+1):
  if A % i == 0:
    list.append(i)

try:
  print(list[B-1])
except:
  print(0)