N = int(input())

def sollution(n):
  return sum(int(i) for i in str(n))

for i in range(1, 1000001):
  if i + sollution(i) == N:
    print(i)
    break
  if i == 1000000:
    print(0)