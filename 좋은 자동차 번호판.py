for _ in range(int(input())):
  price = 0
  word, n = input().split('-')
  num = int(n)
  for i in range(3):
    price += (ord(word[i])-65) * 26**(2-i)
  print("nice" if abs(price - num) <= 100 else "not nice")