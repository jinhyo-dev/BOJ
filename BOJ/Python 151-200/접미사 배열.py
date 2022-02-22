str = list(input())
arr = []
while len(str):
  S = ''.join(str)
  arr.append(S)
  del str[0]
arr.sort()
print(*arr, sep='\n')