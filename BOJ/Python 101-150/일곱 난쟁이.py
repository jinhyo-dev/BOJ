dwarfs = [int(input()) for _ in range(9)]
dwarfs.sort()

for i in range(9):
  for j in range(i+1, 9):
    if sum(dwarfs) - (dwarfs[i] + dwarfs[j]) == 100:
      for k in range(9):
        if i == k or j == k:
          continue
        print(dwarfs[k])
      exit()