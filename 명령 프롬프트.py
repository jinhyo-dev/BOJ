N = int(input())
last_cmd = list(input())
for i in range(N-1):
  cmd = list(input())
  for w in range(len(cmd)):
    if cmd[w] != last_cmd[w] and cmd[w] != '?':
      last_cmd[w] = '?'
print(''.join(last_cmd))