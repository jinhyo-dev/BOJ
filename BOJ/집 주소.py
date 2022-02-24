while True:
  cm = 2
  N = input()
  if int(N) == 0:
    break
  for i in N:
    if i == '1':
      cm += 2
    elif i == '0':
      cm += 4
    else:
      cm += 3
  print(cm+len(N)-1)