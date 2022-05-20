A_card = list(map(int, input().split()))
B_card = list(map(int, input().split()))
A_sum = B_sum = 0
for i in range(10):
  if A_card[i] > B_card[i]:
    A_sum += 1
  elif A_card[i] < B_card[i]:
    B_sum += 1

if A_sum == B_sum:
  print("D")
else:
  print('A' if A_sum > B_sum else 'B')