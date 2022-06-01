import sys
input = sys.stdin.readline
N = int(input())
card_dict = {}

for _ in range(N):
  card = int(input())
  if card in card_dict:
    card_dict[card] += 1
  else:
    card_dict[card] = 1

result = sorted(card_dict.items(), key=lambda x: ( -x[1], x[0]))
print(result[0][0])