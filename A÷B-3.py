A, B = map(int, input().split())
C, D = divmod(A, B)
if A != 0 and D < 0:
  C, D = C+1, D-B 

print(C, D, sep='\n')