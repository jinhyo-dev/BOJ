def star(n):
  if n <= 0: 
    return
  star(n-1)
  print('*', end='')

n = int(input())
star(n)
print()