alphabet =  [chr(i) for i in range(97, 123)]
for _ in range(int(input())):
  missing = []
  isPangram = True
  string = list(input())
  for i in alphabet:
    if i.lower() not in string and i.upper() not in string:
      missing.append(i)
      isPangram = False

  if isPangram:
    print('pangram')
  else:
    print('missing', ''.join(missing))