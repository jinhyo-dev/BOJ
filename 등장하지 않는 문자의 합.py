for _ in range(int(input())):
  alphabet = [i for i in range(65, 91)]
  str = list(input())

  for s in str:
    alphabet[ord(s)-65] = 0

  print(sum(alphabet))