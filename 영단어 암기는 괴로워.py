words = {}
N, M = map(int, input().split())
for _ in range(N):
  w = input()
  if len(w) >= M:
    if w in words:
      words[w][0] += 1
    else:
      words[w] = [1, len(w), w]
answer = sorted(words.items(), key=lambda x: (-x[1][0], -x[1][1], x[1][2]))
for i in answer:
  print(i[0])
