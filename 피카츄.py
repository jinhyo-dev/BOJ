from sys import stdin

s = stdin.readline().rstrip()
pikachu = ['pi', 'ka', 'chu']

for i in pikachu:
  s = s.replace(i, ' ')

for c in s:
  if ord('a') <= ord(c) <= ord('z'):
    print('NO')
    break

else:
  print('YES')