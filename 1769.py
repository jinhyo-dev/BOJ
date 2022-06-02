num = list(input())
cnt = 0

while len(num) != 1:
  tmp = 0
  for i in num:
    tmp += int(i)
  num = list(str(tmp))
  cnt += 1

print(cnt)
print('NO 'if int(''.join(num)) % 3 else 'YES')