T = int(input())
for _ in range(T):
  X, Y = map(int, input().split())
  distance = Y - X
  cnt = 0
  move = 1
  move_plus = 0
  while move_plus < distance:
    cnt += 1
    move_plus += move
    if cnt % 2 == 0:
      move += 1
  print(cnt)