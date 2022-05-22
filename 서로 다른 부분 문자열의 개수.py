string = input()
answer = set()
for i in range (len(string)):
  for j in range (i, len(string)):
    tmp = string[i:j + 1]
    answer.add(tmp)
print(len(answer))