N = int(input())
A = [1, 0]
B = [0, 1]
for i in range(2, N+1):
  a_num = A[i-1] + A[i-2]
  b_num = B[i-1] + B[i-2]
  A.append(a_num)
  B.append(b_num)

print(A[N], B[N])