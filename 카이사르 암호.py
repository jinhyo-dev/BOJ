str = input()

for s in str:
  if ord(s) >= 65 and ord(s) < 68:
    print(chr(ord(s)+23), end='')
  else:
    print(chr(ord(s)-3), end='')