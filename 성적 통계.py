for i in range(int(input())):
  Max = 0
  arr = list(map(int, input().split()))
  del arr[0]
  arr.sort(reverse=True)
  print(f'Class {i+1}\nMax {max(arr)}, Min {min(arr)},', end=' ')
  for j in range(len(arr)-1):
    if (arr[j] - arr[j+1]) >= Max:
      Max = arr[j] - arr[j+1]
  print(f'Largest gap {Max}')