A, B = 0, 1
for i in range(int(input())):
  A, B = B, A+B
print(A)