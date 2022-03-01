vowel = ['a', 'e', 'i', 'o', 'u']
while True:
  cnt = 0
  str = input()
  if str == '#':
    break
  for i in str:
    if i.lower() in vowel:
      cnt += 1
  print(cnt)