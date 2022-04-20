for _ in range(int(input())):
  maxUniv = maxLitter = 0
  for _ in range(int(input())):
    univ, litter = input().split()
    if int(litter) > maxLitter:
      maxLitter = int(litter)
      maxUniv = univ
  print(maxUniv)