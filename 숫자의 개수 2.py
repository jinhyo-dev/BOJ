A = int(input())
B = int(input())
C = int(input())
result = str(A * B * C)
arr = [0] * 10
for i in result:
  arr[int(i)] += 1

print(*arr, sep='\n')