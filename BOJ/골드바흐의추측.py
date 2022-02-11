def is_prime(n):
  for i in range(2, int(n ** 0.5+1)):
    if n % i == 0:
      return False
  return True

arr = []
for i in range(2, 10000):
  if is_prime(i):
    arr.append(i)

for _ in range(int(input())):
  N = int(input())
  for i in range(N//2, 1, -1):
    if i in arr and N-i in arr:
      A, B = i, N-i
      break
    else:
      pass
  print(A, B)