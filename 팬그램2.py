alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for t in range(int(input())):
  cnt = [0] * 26
  string = input()
  string = string.lower()
  for i in range(len(string)):
    if string[i] in alphabet:
      cnt[alphabet.index(string[i])] += 1
  if min(cnt) == 0:
    print(f'Case {t+1}: Not a pangram')
  elif min(cnt) == 1:
    print(f'Case {t+1}: Pangram!')
  elif min(cnt) == 2:
    print(f'Case {t+1}: Double pangram!!')
  else:
    print(f'Case {t+1}: Triple pangram!!!')