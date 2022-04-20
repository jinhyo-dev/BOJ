B = int(input())
P = 5 * B - 400
print(P)
if P == 100:
  print(0)
else:
  print(1 if P < 100 else -1)