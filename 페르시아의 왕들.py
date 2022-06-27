while True:
  A, B, C, D = map(int, input().split())
  if A == B == C == D == 0:
    break
  print(C - B, D - A)
