yonsei = 0
korea = 0
for _ in range(int(input())):
  for _ in range(9):
    A, B = map(int, input().split())
    yonsei += A
    korea += B
  if yonsei > korea:
    print('Yonsei')
  elif yonsei < korea:
    print('Korea')
  else:
    print('draw')