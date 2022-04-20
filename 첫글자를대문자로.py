for _ in range(int(input())):
  str = input()
  arr = list(str)
  for i in range(len(arr)):
    if i == 0:
      print(arr[i].upper(), end='')
    else:
      print(arr[i], end="")
  print()