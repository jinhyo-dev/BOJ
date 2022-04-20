while True:
  side = list(map(int, input().split()))
  if side[0] == side[1] == side[2] == 0:
    break
  side.sort()
  longestSide = (side[2] ** 2)
  theotherSide = (side[0] ** 2 + side[1] ** 2)
  if longestSide == theotherSide:
    print('right')
  else:
    print('wrong')