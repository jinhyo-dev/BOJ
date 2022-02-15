for _ in range(int(input())):
  N, S = input().split()
  arr= list(S)
  del arr[int(N)-1]
  print(*arr, sep='')