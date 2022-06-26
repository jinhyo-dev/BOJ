for _ in range(int(input())):
  arr = list(input())
  N = len(arr)
  N //= 2
  if arr[N - 1] == arr[N]:
    print('Do-it')
  else:
    print('Do-it-Not')
