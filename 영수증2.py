price = int(input())
sumOfValues = 0
for i in range(int(input())):
  A, B = map(int, input().split())
  sumOfValues += (A * B)

print('Yes' if price == sumOfValues else 'No')
