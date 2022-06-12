string = list(input())
start = 'A'
cnt = 0
for i in string:
  left = ord(i) - ord(start)
  right = ord(start) - ord(i)

  if left < 0:
    left += 26
  if right < 0:
    right += 26

  cnt += min(left, right)
  start = i
print(cnt)