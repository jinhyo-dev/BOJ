def isPrime(n):
  if n == 1:
    return False
  else:
    for i in range(2, int(n**0.5) + 1):
      if n % i == 0:
        return False
    return True

n, m = input().split()
phoneNumber = int(m + n)
print('Yes' if isPrime(phoneNumber) and isPrime(int(n)) else 'No')