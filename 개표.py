N = int(input())
str = input()
arr = list(str)
A = 0
B = 0
for i in range(N):
  if arr[i] == 'A':
    A += 1
  else: 
    B += 1

if A > B:
  print('A')
elif A < B:
  print('B')
else:
  print('Tie')