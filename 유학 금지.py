cambridge = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']
sentence = list(input())
for i in range(len(sentence)):
  if sentence[i] in cambridge:
    sentence[i] = ''
print(*sentence, sep='')