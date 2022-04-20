pay, price = map(int, input().split())
coin = 0
pay -= price
while True:
  if pay == 0:
    break
  elif pay >= 500:
    pay -= 500
    coin += 1
    continue
  elif pay >= 100:
    pay -= 100
    coin += 1
    continue
  elif pay >= 50:
    pay -= 50
    coin += 1
    continue
  elif pay >= 10:
    pay -= 10
    coin += 1
    continue
  elif pay >= 5:
    pay -= 5
    coin += 1
    continue
  elif pay >= 1:
    pay -= 1
    coin += 1
    continue
print(coin)