def isPrime(num):
  if num == 1:
    return True
  else:
    for i in range(2, int(num**0.5) + 1):
      if num % i == 0:
        return False
      return True

sum = 0
word = list(input())

for i in word:
  if i.islower() == True:
    sum += ord(i) - 96
  else:
    sum += ord(i) - 64

print('It is a prime word.' if isPrime(sum) else 'It is not a prime word.')