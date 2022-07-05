N = int(input())
arr = list(input())
d = '0123456789'
hiddenNumber = ''

for i in arr:
  if i in d:
    hiddenNumber += i
  else:
    hiddenNumber += ' '

print(sum(list(map(int, hiddenNumber.split()))))
