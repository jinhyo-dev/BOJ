def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

while True:
  A, B = map(int, input().split())
  if A == 0 and B == 0:
    break
