n = int(input())
num = 1
sum = 0
while True:
  if sum >= n:
    print(num - 1)
    break
  sum = sum + num
  num = num + 1
