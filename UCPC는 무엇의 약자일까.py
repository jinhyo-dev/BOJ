string = input()
check_list = ['U', 'C', 'P', 'C']
isContain = True

for i in check_list:
  if i in string:
    string = string[string.find(i)+1:]
  else:
    isContain = False
    break

print('I love UCPC' if isContain else 'I hate UCPC')