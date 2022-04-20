for _ in range(3):
  p = c = m = 0
  for i in input():
    c = c + 1 if p == i else 0
    m, p = c if c > m else m , i
  print(m+1)