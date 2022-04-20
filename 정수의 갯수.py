interger = list(input().split(','))
cnt = 0
for num in interger:
  if int(num) % 1 == 0:
    cnt += 1
print(cnt)