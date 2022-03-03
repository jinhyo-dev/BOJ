i = 1
while True:
  N = int(input())
  if N == 0:
    break
  N1 = N * 3
  N2 = (N1 + 1) // 2 if N1 % 2 else N1 // 2
  N3 = 3*N2
  N4 = N3 // 9
  print(f'{i}. even {N4}' if N == 2*N4 else f'{i}. odd {N4}')
  i += 1