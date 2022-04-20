big = [chr(i) for i in range(65, 91)]
small = [chr(i) for i in range(97, 123)]
num = [str(i) for i in range(0, 10)]

while True:
  try:
    A, B, C, D = 0, 0, 0, 0
    str = list(input())
    for word in str:
      if word in small:
        A += 1
      elif word in big:
        B += 1
      elif word in num:
        C += 1
      elif word == ' ':
        D += 1
    print(A, B, C, D)
  except EOFError:
    break
