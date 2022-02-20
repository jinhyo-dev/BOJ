str = list(input())
arr = []
arr.append(str[0])
for i in range(len(str)-1):
  if str[i] == '-':
    arr.append(str[i+1])
print(*arr, sep='')