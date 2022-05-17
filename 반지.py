string = input()
cnt = 0
for _ in range(int(input())):
  ring = input()
  ring += ring
  if string in ring:
    cnt += 1
print(cnt)