# N = int(input())
# fib = [i for i in range(N + 1)]
# fib[1] = 1
# for i in range(2, N + 1):
#   fib[i] = fib[i-1] + fib[i-2]
# print(fib[-1])

A, B=0,1
for i in range(int(input())):
  A, B = B, A+B
print(A)