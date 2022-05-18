string = list(input())
isTag = False
word = ''
result = ''

for s in string:
  if not isTag:
    if s == '<':
      isTag = True
      word += s
    elif s == ' ':
      word += s
      result += word
      word = ''
    else:
      word = s + word
  elif isTag:
    word += s
    if s == '>':
      isTag = False
      result += word
      word = ''

print(result + word)