str = list(input())
for i in range(len(str)):
  if (i+1) % 10 == 0:
    print(str[i], end='') 
    print()
  else:
    print(str[i], end='')