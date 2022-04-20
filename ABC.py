arr = list(map(int, input().split()))
alphabet = list(input())
arr.sort()

for i in range(3):
  if alphabet[i] == 'A':
    print(arr[0], end=' ')
  
  elif alphabet[i] == 'B':
    print(arr[1], end=' ')
  
  else:
    print(arr[2], end=' ')