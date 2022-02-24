N = int(input())
while True:
  num = int(input())
  if num == 0:
    break
  print(f'{num} is a multiple of {N}.' if num % N == 0 else f'{num} is NOT a multiple of {N}.')