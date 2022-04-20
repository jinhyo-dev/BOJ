import sys
input = sys.stdin.readline
N, M = map(int, input().split())
dict = {}

for i in range(1, N + 1):
  pocketmon = input().rstrip()
  dict[i] = pocketmon
  dict[pocketmon] = i

for i in range(M):
  question = input().rstrip()
  print(dict[int(question)] if question.isdigit() else dict[question])