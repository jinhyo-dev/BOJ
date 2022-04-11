while True:
  sum = 0
  oct = list(input())
  squared = len(oct)-1
  if oct[0] == '#':
    break
  else:
    for i in oct:
      if i == '-':  sum += (0 * (8 ** squared))
      elif i == "\\": sum += (1 * (8 ** squared))
      elif i == "(": sum += (2 * (8 ** squared))
      elif i == "@": sum += (3 * (8 ** squared))
      elif i == "?": sum += (4 * (8 ** squared))
      elif i == ">": sum += (5 * (8 ** squared))
      elif i == "&": sum += (6 * (8 ** squared))
      elif i == "%": sum += (7 * (8 ** squared))
      else: sum += (-1 * (8 ** squared))
      squared -= 1
    print(sum)