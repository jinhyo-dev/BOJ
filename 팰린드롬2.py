for _ in range(int(input())):
  s = input()
  if s.lower() == s[::-1].lower():
    print('Yes')
  else:
    print('No')