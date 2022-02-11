n = int(input())
tmp = 0
for i in range(1, n+1):
  if n % i == 0:
    tmp = tmp + 1

if tmp >= 3:
  print('not prime')
else:
  print('prime')
