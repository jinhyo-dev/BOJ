for _ in range(int(input())):
  try:
    A, B = map(int, input().split('+'))
    print(A+B)
  except:
    print('skipped')