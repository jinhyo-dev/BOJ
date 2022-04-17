while True:
  A, B, C = map(int, input().split())
  if A == B == C == 0:
    break
  if B - A == C - B:
    print(f'AP {C + C-B}')
  else:
    print(f'GP {C * (C // B)}')