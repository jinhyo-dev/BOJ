for _ in range(int(input())):
  arr = list(map(int, input().split()))
  even_list = []
  for i in arr:
    if i % 2 == 0:
      even_list.append(i)
  print(sum(even_list), min(even_list))