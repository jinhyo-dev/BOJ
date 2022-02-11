import math

def isPrime(n) :
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

N = 100000
count = 0
for n in range (2, N+1):
    if isPrime(n):
        count += 1
print(count)