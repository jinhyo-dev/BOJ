while True:
  sentece = list(input())
  alphabet = sentece[0]
  cnt = 0
  del sentece[0]

  if alphabet == '#':
    break

  else:
    for i in sentece:
      if i.lower() == alphabet:
        cnt += 1
  print(alphabet, cnt)
