import re
cnt = {}
p = re.compile("[^0-9]")
word = p.findall(input())
word = list(filter(str.isalnum, word))
word.sort()

for i in word:
  try: cnt[i] += 1
  except: cnt[i] = 1

for i in cnt.keys():
  print(f'{i} : {cnt[i]}개')