N = int(input())
arr = []
name = []
for i in range(N):
  player = list(input())
  arr.append(player[0])

tmp = set(arr)

for i in tmp:
  if arr.count(i) >= 5:
    name.append(i)

name.sort()
if len(name) == 0:
  print("PREDAJA")
else:
  print(''.join(name))