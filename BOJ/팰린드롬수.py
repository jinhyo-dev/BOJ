while True:
  N = input()
  if int(N) == 0:
    break
  
  arr = list(N)
  print('yes') if arr == list(reversed(arr)) else print('no')