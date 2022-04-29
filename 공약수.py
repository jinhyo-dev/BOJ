N = int(input())
arr = list(map(int, input().split()))
if N == 2:
  for i in range(1, min(arr)+1):
    if arr[0] % i == 0 and arr[1] % i == 0:
     print(i)
elif N == 3:
  for i in range(1, min(arr)+1):
    if arr[0] % i == 0 and arr[1] % i == 0 and arr[2] % i == 0:
      print(i)