string = input()
sumOfJOI = sumOfIOI = 0
for i in range(len(string) -2):
  if string[i] != 'J' and string[i] != 'I':
    continue
  elif string[i] == 'J':
    if string[i:i+3] == 'JOI':
      sumOfJOI += 1
  elif string[i] == 'I':
    if string[i:i+3] == 'IOI':
      sumOfIOI += 1
print(sumOfJOI, sumOfIOI, sep='\n')