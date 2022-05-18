for _ in range(int(input())):
  L_list = []
  R_list = []
  string = input()
  for i in string:
    if i == '-':
      if L_list:
        L_list.pop()
    elif i == '<':
      if L_list:
        R_list.append(L_list.pop())
    elif i == '>':
      if R_list:
        L_list.append(R_list.pop())
    else:
      L_list.append(i)
  L_list.extend(reversed(R_list))
  print(''.join(L_list))