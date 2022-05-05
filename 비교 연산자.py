i = 0
while True:
  i += 1
  A, operator, B = input().split()
  boolean = True
  A = int(A)
  B = int(B)
  if operator == '>':
    if A <= B:
      boolean = False
  elif operator == '<':
    if A >= B:
      boolean = False
  elif operator == '>=':
    if A < B:
      boolean = False
  elif operator == '<=':
    if A > B:
      boolean = False
  elif operator == '==':
    if A != B:
      boolean = False
  elif operator == '!=':
    if A == B:
      boolean = False
  else:
    break
  print(f'Case {i}: {str(boolean).lower()}')