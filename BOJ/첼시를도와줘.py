for _ in range(int(input())):
  arr = []
  for _ in range(int(input())):
    [cost, player] = input().split()
    arr.append([int(cost), player])
    arr.sort()
  print(arr[-1][1])