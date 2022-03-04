arr = list(map(int, input().split()))
if sum(arr) >= 100:
  print('OK')
else:
  tmp = min(arr)
  index = arr.index(tmp)
  if index == 0:
    print('Soongsil')
  elif index == 1:
    print('Korea')
  else:
    print('Hanyang')