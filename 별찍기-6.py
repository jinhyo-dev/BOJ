N = int(input())
for i in range(1, N+1):
  print(' ' * (i-1) + '*' * ((2*N)-i * 2 + 1))