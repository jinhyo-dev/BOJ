for _ in range(int(input())):
  A, B = input().split()
  arr = []
  for i in range(len(A)):
    if ord(A[i]) > ord(B[i]):
      arr.append(26 - (ord(A[i]) - ord(B[i])))
    else:
      arr.append(ord(B[i]) - ord(A[i]))
  print('Distances:', *arr)