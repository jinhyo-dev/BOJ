i = 0
while True:
  i += 1
  word1 = list(input())
  word2 = list(input())
  
  if ''.join(word1) == 'END' and ''.join(word2) == 'END':
    break
  
  word1.sort()
  word2.sort()

  print(f'Case {i}: same' if word1 == word2 else f'Case {i}: different')