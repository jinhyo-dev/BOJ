i = 1
while True:
  day = 0
  L, P, V = map(int, input().split())
  if L == 0 and P == 0 and V == 0:
    break
  else:
    day = (V // P) * L
    day += min(V % P, L)

    print(f'Case {i}: {day}')
    i += 1