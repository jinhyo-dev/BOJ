for _ in range(int(input())):
  answer = 0
  array = list(input().split())
  answer += float(array[0])
  for i in range(len(array)):
    if array[i] == '@':
      answer *= 3
    elif array[i] == '%':
      answer += 5
    elif array[i] == '#':
      answer -= 7
  print('%.2f'%(answer))
  array = []
