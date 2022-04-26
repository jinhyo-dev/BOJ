for _ in range(int(input())):
  sumOfG = sumOfB = 0
  String = input()
  for i in String:
    if i.lower() == 'g':
      sumOfG += 1
    elif i.lower() == 'b':
      sumOfB += 1
  if sumOfG == sumOfB:
    print(f'{String} is NEUTRAL')
  else:
    print(f'{String} is GOOD' if sumOfG > sumOfB else f'{String} is A BADDY')