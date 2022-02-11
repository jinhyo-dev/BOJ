str = input()
a, b = map(int, input().split())
arr = list(str)
for i in range(len(arr)):
  if i+1 == a:
    print(arr[b-1], end='')
  elif i+1 == b:
    print(arr[a-1], end='')
  else:
    print(arr[i], end='') 
