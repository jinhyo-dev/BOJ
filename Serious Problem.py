S = int(input())
str = input()
two = 0
e = 0
for i in str:
  if i == '2':
    two += 1
  elif i == 'e':
    e += 1

if two > e:
  print(2)
elif two < e:
  print('e')
else:
  print('yee')