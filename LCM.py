from math import lcm

for _ in range(int(input())):
  A, B = map(int, input().split())
  print(lcm(A, B))