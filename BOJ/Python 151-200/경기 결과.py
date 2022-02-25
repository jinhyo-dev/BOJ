import sys
input = sys.stdin.readline
A = B = 0
for _ in range(int(input())):
  sA, sB = map(int, input().split())
  if sA > sB: A += 1
  elif sA < sB: B += 1
print(A, B)