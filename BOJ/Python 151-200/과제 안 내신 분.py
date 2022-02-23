arr = [int(input()) for _ in range(28)]
find_arr = [i for i in range(1, 31)]
for i in find_arr:
  if i in arr:
    continue
  else:
    print(i)