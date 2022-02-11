import sys

N = int(sys.stdin.readline())
wordList = []

for i in range(N):
  word = sys.stdin.readline().strip()
  wordList.append(word)

set_list = list(set(wordList))
sorted_list = []

for i in set_list:
  sorted_list.append((len(i),i))

sorted_list.sort()

for length, word in sorted_list:
  print(word)

