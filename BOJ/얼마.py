for _ in range(int(input())):
  price = int(input())
  for _ in range(int(input())):
    N, M = map(int, input().split())
    price += M * N
  print(price)