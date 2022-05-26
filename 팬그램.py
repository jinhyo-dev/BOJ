while True:
  isPangram = True
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']
  string = input()
  if string == '*':
    break

  for i in string:
    if i in alphabet:
      alphabet[alphabet.index(i)] = True

  for i in alphabet:
    if not i == True:
      isPangram = False
      break

  print('Y' if isPangram else 'N')
