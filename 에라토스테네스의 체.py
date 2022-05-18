def isPrime(N):
  if N == 1 or N == 0:
    return False
  for i in range(2, int(N ** 0.5) + 1):
    if N % i == 0:
      return False
  return True

def solution():
  for i in range(len(arr)):
    if isPrime(arr[i]):
      delete(arr[i])
      arr[i] = 0
      break

def delete(n):
  for i in range(len(arr)):
    if arr[i] % n == 0 and arr[i] != 0:
      delete_num.append(arr[i])
      arr[i] = 0
  if arr:
    solution()
  else:
    return

N, K = map(int, input().split())
arr = [i for i in range(2, N + 1)]
delete_num = []
solution()
print(delete_num[K-1])