import sys
input = sys.stdin.readline
S = set()
for _ in range(int(input())):
  command = input().strip().split()

  if len(command) == 1:
    if command[0] == 'all':
      S = set([i for i in range(1, 21)]) 
    else:
      S = set()
  
  else:
    if command[0] == 'add': S.add(int(command[1]))
    elif command[0] == 'remove': S.discard(int(command[1]))
    elif command[0] == 'check': print(1 if int(command[1]) in S else 0)
    elif command[0] == 'toggle':
      if int(command[1]) in S:
        S.discard(int(command[1]))
      else:
        S.add(int(command[1]))