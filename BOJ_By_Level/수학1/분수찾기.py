n = int(input())
i = 0
while True:
  i += 1  # 1 2
  n -= i  # 2 0
  if n <= 0:
    n += i  # 2
    i += 1  # 3
    break
if i % 2 == 0:
  print((i-n), '/', n, sep='')
else:
  print(n, '/', (i-n), sep='')
