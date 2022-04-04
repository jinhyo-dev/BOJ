import sys
input = sys.stdin.readline
num = 1000001
arr = [True for _ in range(num)]

for i in range(2, int(num-1**0.5)+1):
  if arr[i]:
    for j in range(i*2, num, i):
      arr[j] = False

while True:
  N = int(input())

  if N == 0:
    break
  
  bool = False

  for i in range(3, len(arr)):
    if arr[i] and arr[N-i]:
      print(f'{N} = {i} + {N-i}')
      bool = True
      break

  if bool == False:
    print("Goldbach's conjecture is wrong.")