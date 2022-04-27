for _ in range(int(input())):
  A, B = map(int, input().split())

  print('Yes' if A >= 0 and A < 24 and B < 60 and B >= 0 else 'No',  end = ' ')

  if A >= 1 and A < 13:
    if A == 2:
      print('Yes' if B >= 1 and B < 30 else 'No')
    elif A in [4, 6, 9, 11]:
      print('Yes' if B >= 1 and B < 31 else 'No')
    else:
      print('Yes' if B >= 1 and B < 32 else 'No')

  else:
    print('No')