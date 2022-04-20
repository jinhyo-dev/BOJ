from math import ceil
A = [int(input()) for _ in range(5)]
print(A[0] - max(ceil(A[1]/A[3]), ceil(A[2]/A[4])))