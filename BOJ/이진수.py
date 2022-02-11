for _ in range(int(input())):
  N = int(input())
  N = format(N, 'b')
  binary_list = list(N)
  binary_list.reverse()
  for j in range(len(binary_list)):
    if int(binary_list[j]) == 1:
      print(j, end=' ')
  print()