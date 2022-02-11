T = int(input())
for i in range(T):
  F = int(input())
  N = int(input())
  zero_F = [x for x in range(1, N+1)]
  for j in range(F):
    for k in range(1, N):
      zero_F[k] += zero_F[k-1]
    #print(zero_F)
  print(zero_F[-1])