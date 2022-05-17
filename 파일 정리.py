dic = {}
for _ in range(int(input())):
  file, extension = input().split('.')
  if extension in dic:
    dic[extension] += 1
  else:
    dic[extension] = 1

for key, value in sorted(dic.items()):
  print(key, value)