names = [input() for _ in range(int(input()))]

sortedName = sorted(names)
reverseSortedNames = sorted(names, reverse=True)

if sortedName == names:
  print('INCREASING')
elif reverseSortedNames == names:
  print('DECREASING')
else:
  print('NEITHER')