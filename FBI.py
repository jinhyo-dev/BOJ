arr = []
for i in range(1,6):
  str = input()
  if 'FBI' in str:
    arr.append(i)
print(*arr) if len(arr) else print('HE GOT AWAY!')