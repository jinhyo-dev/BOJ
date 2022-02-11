total_price = int(input())
price = []
for _ in range(9):
  prices = int(input())
  price.append(prices)

print(total_price - sum(price))
