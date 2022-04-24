def isPrime(num):
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True

N, M = map(int, input().split())
if M > 10000000:  M = 10000000 
palindrome = [i for i in range(N, M+1) if str(i) == str(i)[::-1]]
for i in palindrome:
  if isPrime(i):
    print(i)
print(-1)