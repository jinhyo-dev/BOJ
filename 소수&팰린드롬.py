def isPrime(num):
  if num == 1:
    return False
  else:
    for i in range(2, int(num**0.5) + 1):
      if num % i == 0:
        return False
    return True

i = int(input())

while True:
  i = list(str(i))
  if i == i[::-1]:
    if isPrime(int(''.join(i))):
      print(''.join(i))
      break
  
  i = int(''.join(i))
  i += 1