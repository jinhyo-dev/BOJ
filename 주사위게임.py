p1 = 100
p2 = 100
for i in range(int(input())):
  A, B = map(int, input().split())
  if A > B:
    p2 -= A
  elif A < B:
    p1 -= B
  else:
    pass
  arr = []
  A, B = 0, 0
print(p1)
print(p2)