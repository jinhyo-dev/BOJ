for _ in range(int(input())):
  str = input()
  sum = 0
  for i in str:
    if i == '(':
      sum += 1
    elif i == ')':
      sum -= 1
    if sum < 0:
      break
  print('YES' if sum == 0 else 'NO')
