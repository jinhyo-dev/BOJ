N = int(input())

if N % 10 != 0:
  print(-1)
else:
  A = B = C = 0
  A = N // 300
  B = (N % 300) // 60
  C = (N % 300) % 60 // 10
  print(A, B, C)